import os
import uuid

import requests
from torchvision.utils import save_image

from ..server.generateServer import GenerateServer

CATEGORY_NAME = "ComfyUI-XingLiu"


class UploadLibLibNode:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth_info": ("AUTH_INFO", {'default': ''}),
                "image": ("IMAGE", {'default': ''}),
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("URL",)
    RETURN_NAMES = ("url",)
    FUNCTION = "upload_to_liblib"

    def upload_to_liblib(self, auth_info, image):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
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
        files = {'file': (f'{file_name_uuid}.jpg',
                          open(f'__temp.jpg', 'rb'), 'image/jpg')}
        response = requests.post(data["postUrl"], data=json_data, files=files)
        url = data["postUrl"] + "/" + data["key"]
        os.remove(f"__temp.jpg")
        return ("url",)