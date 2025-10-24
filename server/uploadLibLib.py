import os
import uuid

import requests
from torchvision.utils import save_image

from ..server.generateServer import GenerateServer


def uploadLibLib(image,accessKey,secretKey):
    save_image(image[0], "__temp.png")
    file_name_uuid = uuid.uuid4()
    json_data = {
        "name": str(file_name_uuid),
        "extension": "png"
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
    with open('__temp.png', 'rb') as f:
        files = {'file': (f'{file_name_uuid}.png', f, 'image/png')}
        response = requests.post(data["postUrl"], data=json_data, files=files)
    sourceImage = data["postUrl"] + "/" + data["key"]
    os.remove(f"__temp.png")
    return sourceImage
