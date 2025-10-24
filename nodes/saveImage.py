import os
import time

import torch

from ..server.generateServer import GenerateServer
from ..server.mediaUtils import image_to_tensor_by_url

CATEGORY_NAME = "ComfyUI-XingLiu"


class SaveImage:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "generateUuid": ("STRING", {'default': ''}),
            },
            "optional": {
                "save_path": ("STRING", {'default': 'default'}),
            }
        }

    OUTPUT_NODE = True  # 表明它是一个输出节点
    RETURN_TYPES = ("IMAGE",)
    # 自定义输出名称
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "save_image"  # 核心功能函数名称，将运行这个类中的这个方法

    def save_image(self, generateUuid, save_path):
        image_tensors = []
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        json_data = {"generateUuid": generateUuid}
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        batched = None
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for image in data["images"]:
                    images_dir = save_path
                    if save_path == "default" or save_path == "" or save_path is None:
                        current_file_path = os.path.abspath(__file__)
                        current_dir = os.path.dirname(current_file_path)
                        parent_dir = os.path.dirname(current_dir)  # 上一级目录
                        images_dir = os.path.join(parent_dir, "images").replace("\\", "/")  # 上一级的 images 目录
                    image_tensor = image_to_tensor_by_url(images_dir, image["imageUrl"])
                    image_tensors.append(image_tensor)
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("error")
            time.sleep(5)
        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)
