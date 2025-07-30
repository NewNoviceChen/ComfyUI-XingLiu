import json
import os

from ..server.generateServer import GenerateServer

CATEGORY_NAME = "ComfyUI-XingLiu"


class MakeLoraNode:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "modelId": ("STRING",),
                "weight": ("FLOAT", {
                    "default": 0.8,
                    "min": -4.0,
                    "max": 4.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ('LORA',)
    RETURN_NAMES = ('LORA',)
    FUNCTION = "make_lora"

    def make_lora(self,
                  auth,
                  modelId,
                  weight,
                  ):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        json_data = {
            "versionUuid": modelId,
        }
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/model/version/get", json_data)
        if data is None:
            raise Exception("模型不存在")
        if data["commercialUse"] != 1:
            raise Exception("模型不可商用")
        lora = {
            "modelId": modelId,
            "weight": weight,
        }
        return (json.dumps(lora),)


class MergeLoraNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Lora_1": ("LORA", {"forceInput": True})
            },
            "optional": {
                "Lora_2": ("LORA", {"forceInput": True}),
                "Lora_3": ("LORA", {"forceInput": True}),
                "Lora_4": ("LORA", {"forceInput": True}),
                "Lora_5": ("LORA", {"forceInput": True})
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ('LORA_LIST',)
    RETURN_NAMES = ('lora_list',)
    FUNCTION = "make_lora_list"

    def make_lora_list(self, Lora_1, Lora_2=None, Lora_3=None,
                       Lora_4=None, Lora_5=None):
        # 创建一个空列表
        lora_list = []
        # 添加所有非None的controlnet_info到列表中
        if Lora_1 is not None and Lora_1 != '':
            info = json.loads(Lora_1)
            lora_list.append(info)
        if Lora_2 is not None and Lora_2 != '':
            info = json.loads(Lora_2)
            lora_list.append(info)
        if Lora_3 is not None and Lora_3 != '':
            info = json.loads(Lora_3)
            lora_list.append(info)
        if Lora_4 is not None and Lora_4 != '':
            info = json.loads(Lora_4)
            lora_list.append(info)
        if Lora_5 is not None and Lora_5 != '':
            info = json.loads(Lora_5)
            lora_list.append(info)
        return (lora_list,)
