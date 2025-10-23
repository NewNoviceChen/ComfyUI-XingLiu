import json
import os

from ..server.uploadLibLib import uploadLibLib

CATEGORY_NAME = "ComfyUI-XingLiu"


class MergeImageListNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "image_1": ("IMAGE", {"forceInput": True}),
            },
            "optional": {
                "image_2": ("IMAGE", {"forceInput": True}),
                "image_3": ("IMAGE", {"forceInput": True}),
                "image_4": ("IMAGE", {"forceInput": True}),
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ('IMAGE_LIST',)
    RETURN_NAMES = ('IMAGE_LIST',)
    FUNCTION = "make_image_list"

    def make_image_list(self, auth, image_1, image_2=None, image_3=None,
                        image_4=None, image_5=None):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        imageList = []
        if image_1 is not None and image_1 != '':
            image_1_url = uploadLibLib(image_1, accessKey, secretKey)
            imageList.append(image_1_url)
        if image_2 is not None and image_2 != '':
            image_2_url = uploadLibLib(image_2, accessKey, secretKey)
            imageList.append(image_2_url)
        if image_3 is not None and image_3 != '':
            image_3_url = uploadLibLib(image_3, accessKey, secretKey)
            imageList.append(image_3_url)
        if image_4 is not None and image_4 != '':
            image_4_url = uploadLibLib(image_4, accessKey, secretKey)
            imageList.append(image_4_url)
        return (imageList,)
