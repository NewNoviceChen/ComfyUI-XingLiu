import os
import uuid

import requests
from torchvision.utils import save_image

from ..server.generateServer import GenerateServer


def uploadLibLib(image,accessKey,secretKey):
    save_image(image[0].permute(2, 0, 1), "__temp.jpg")
    file_name_uuid = uuid.uuid4()
    json_data = {
        "name": str(file_name_uuid),
        "extension": "jpg"
    }
    generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
    data = generateServer._request_signature_uri("/api/generate/upload/signature", json_data)
    json_data = {
        'key': data["key"],
        'policy': data["policy"],
        'x-oss-date': data["xOssDate"],
        'x-oss-expires': data["xOssExpires"],
        'x-oss-signature': data["xOssSignature"],
        'x-oss-credential': data["xOssCredential"],
        'x-oss-signature-version': data["xOssSignatureVersion"],
    }
    with open('__temp.jpg', 'rb') as f:
        files = {'file': (f'{file_name_uuid}.jpg', f, 'image/jpg')}
        response = requests.post(data["postUrl"], data=json_data, files=files)
    sourceImage = data["postUrl"] + "/" + data["key"]
    os.remove(f"__temp.jpg")
    return sourceImage
