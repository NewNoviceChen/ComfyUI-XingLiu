import json
import os
import time

import torch

from ..server.getModel import get_vad_uuid_by_vad_name
from ..server.uploadLibLib import uploadLibLib
from ..server.imagesUtils import image_to_tensor_by_url
from ..server.generateServer import GenerateServer

CATEGORY_NAME = "ComfyUI-XingLiu"


class Image2ImageByAlphaNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "prompt": ("STRING", {"multiline": True}),
                "imgCount": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 4,
                    "step": 1,
                    "display": "number"}),
                "sourceImage": ("IMAGE",),

            },
            "optional": {
                "controlType": (["line", "depth", "pose", "IPAdapter"],),
                "controlImage": ("IMAGE",),
            }
        }

    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "img2img"

    def img2img(self,
                auth,
                prompt,
                imgCount,
                sourceImage,
                controlType=None,
                controlImage=None):

        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        sourceImage = uploadLibLib(sourceImage, accessKey, secretKey)
        if controlImage != None:
            controlImage = uploadLibLib(controlImage, accessKey, secretKey)
        json_data = {
            "templateUuid": "07e00af4fc464c7ab55ff906f8acf1b7",
            "generateParams": {
                "prompt": prompt,
                "imgCount": imgCount,
                "sourceImage": sourceImage,
                "controlnet": {
                    "controlType": controlType,
                    "controlImage": controlImage,
                } if controlType is not None and controlImage is not None else {},
            }
        }

        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/img2img/ultra", json_data)
        generateUuid = data["generateUuid"]
        json_data = {"generateUuid": generateUuid}
        image_tensors = []
        batched = None
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for image in data["images"]:
                    image_tensor = image_to_tensor_by_url(image["imageUrl"])
                    image_tensors.append(image_tensor)
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("执行失败")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)


class Image2ImageCustomNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "checkPointId": ("STRING",),
                "prompt": ("STRING", {"multiline": True}),
                "negativePrompt": ("STRING", {"multiline": True}),
                "clipSkip": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 12,
                    "step": 1,
                    "defaultInput": True,
                    "display": "number"}),
                "sampler": (
                    ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                     "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                     "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                     "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                     "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"],),
                "steps": ("INT", {
                    "default": 20,
                    "min": 1,
                    "max": 60,
                    "step": 1,
                    "display": "number"}),
                "cfgScale": ("FLOAT", {
                    "default": 7.0,
                    "min": 1.0,
                    "max": 15.0,
                    "step": 0.1,
                    "round": 0.1,
                    "display": "number"}),
                "randSource": (["cpu", "gpu"],),
                "seed": ("INT", {
                    "default": -1,
                    "display": "number"}),
                "imgCount": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 4,
                    "step": 1,
                    "display": "number"}),
                "restoreFaces": (["关闭", "开启"],),
                "image": ("IMAGE",),
                "resizeMode": (["just_resize", "crop_and_resize ", "resize_and_fill"],),
                "resizedWidth": ("INT", {
                    "default": 1024,
                    "min": 128,
                    "max": 2048,
                    "step": 1,
                    "display": "number"}),
                "resizedHeight": ("INT", {
                    "default": 1536,
                    "min": 128,
                    "max": 2048,
                    "step": 1,
                    "display": "number"}),
                "denoisingStrength": ("FLOAT", {
                    "default": 0.75,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
            },
            "optional": {
                "vaeId": (
                    ["通用 - Automatic",
                     "基础算法 1.5 - vae-ft-mse-840000-ema-pruned.safetensors",
                     "基础算法 1.5 - klF8Anime2VAE_klF8Anime2VAE.ckpt",
                     "基础算法 1.5 - color101VAE_v1.pt", "基础算法 1.5 - cute vae.safetensors",
                     "基础算法 1.5 - ClearVAE_V2.3.safetensors",
                     "基础算法 1.5 - difconsistencyRAWVAE_v10.pt",
                     "基础算法 XL - sd_xl_vae_1.0"],),
                "lora_list": ("LORA_LIST", {"forceInput": True}),
                "controlnet_list": ("CONTROLNET_LIST", {"forceInput": True})
            }
        }

    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "img2img"

    def img2img(self,
                auth,
                checkPointId,
                vaeId,
                prompt,
                negativePrompt,
                clipSkip,
                sampler,
                steps,
                cfgScale,
                randSource,
                seed,
                imgCount,
                restoreFaces,
                image,
                resizeMode,
                resizedWidth,
                resizedHeight,
                denoisingStrength,
                lora_list=None,
                controlnet_list=None):
        sampler = ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                   "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                   "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                   "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                   "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"].index(sampler)
        randSource = ["cpu", "gpu"].index(randSource)
        restoreFaces = ["关闭", "开启"].index(restoreFaces)
        resizeMode = ["just_resize", "crop_and_resize ", "resize_and_fill"].index(resizeMode)
        vaeId = get_vad_uuid_by_vad_name(vaeId)

        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        sourceImage = uploadLibLib(image, accessKey, secretKey)
        json_data = {
            "templateUuid": "9c7d531dc75f476aa833b3d452b8f7ad",
            "generateParams": {
                "checkPointId": checkPointId,
                "vaeId": vaeId,
                "prompt": prompt,
                "negativePrompt": negativePrompt,
                "clipSkip": clipSkip,
                "sampler": sampler,
                "steps": steps,
                "cfgScale": cfgScale,
                "randSource": randSource,
                "seed": seed,
                "imgCount": imgCount,
                "restoreFaces": restoreFaces,
                "sourceImage": sourceImage,
                "resizeMode": resizeMode,
                "resizedWidth": resizedWidth,
                "resizedHeight": resizedHeight,
                "mode": 0,
                "denoisingStrength": denoisingStrength,
                "inpaintParam": {},
                "additionalNetwork": lora_list,
                "controlNet": controlnet_list if controlnet_list else None
            }
        }
        print(json_data)
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/img2img", json_data)
        generateUuid = data["generateUuid"]
        print(generateUuid)
        json_data = {"generateUuid": generateUuid}
        image_tensors = []
        batched = None
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for image in data["images"]:
                    image_tensor = image_to_tensor_by_url(image["imageUrl"])
                    image_tensors.append(image_tensor)
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("执行失败")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)

class Image2ImageCustomAlphaNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "prompt": ("STRING", {"multiline": True}),
                "negativePrompt": ("STRING", {"multiline": True}),
                "clipSkip": ("INT", {
                    "default": 2,
                    "min": 1,
                    "max": 12,
                    "step": 1,
                    "display": "slider"}),
                "sampler": (
                    ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                     "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                     "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                     "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                     "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"],),
                "steps": ("INT", {
                    "default": 20,
                    "min": 1,
                    "max": 60,
                    "step": 1,
                    "display": "slider"}),
                "cfgScale": ("FLOAT", {
                    "default": 7.0,
                    "min": 1.0,
                    "max": 15.0,
                    "step": 0.1,
                    "round": 0.1,
                    "display": "slider"}),
                "randSource": (["cpu", "gpu"],),
                "seed": ("INT", {
                    "default": -1,
                    "display": "number"}),
                "imgCount": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 4,
                    "step": 1,
                    "display": "number"}),
                "restoreFaces": (["关闭", "开启"],),
                "image": ("IMAGE",),
                # "resizeMode": (["just_resize", "crop_and_resize ", "resize_and_fill"],),
                # "resizedWidth": ("INT", {
                #     "default": 1024,
                #     "min": 128,
                #     "max": 2048,
                #     "step": 1,
                #     "display": "slider"}),
                # "resizedHeight": ("INT", {
                #     "default": 1536,
                #     "min": 128,
                #     "max": 2048,
                #     "step": 1,
                #     "display": "slider"}),
                "denoisingStrength": ("FLOAT", {
                    "default": 0.75,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "slider"}),
            },
            "optional": {
                "vaeId": (
                    ["通用 - Automatic",
                     "基础算法 1.5 - vae-ft-mse-840000-ema-pruned.safetensors",
                     "基础算法 1.5 - klF8Anime2VAE_klF8Anime2VAE.ckpt",
                     "基础算法 1.5 - color101VAE_v1.pt", "基础算法 1.5 - cute vae.safetensors",
                     "基础算法 1.5 - ClearVAE_V2.3.safetensors",
                     "基础算法 1.5 - difconsistencyRAWVAE_v10.pt",
                     "基础算法 XL - sd_xl_vae_1.0"],),
                "lora_list": ("LORA_LIST", {"forceInput": True}),
                "controlnet_list": ("CONTROLNET_LIST", {"forceInput": True})
            }
        }
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "img2img"

    def img2img(self,
                auth,
                vaeId,
                prompt,
                negativePrompt,
                clipSkip,
                sampler,
                steps,
                cfgScale,
                randSource,
                seed,
                imgCount,
                restoreFaces,
                image,
                # resizeMode,
                # resizedWidth,
                # resizedHeight,
                denoisingStrength,
                lora_list=None,
                controlnet_list=None):
        sampler = ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                   "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                   "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                   "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                   "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"].index(sampler)
        randSource = ["cpu", "gpu"].index(randSource)
        restoreFaces = ["关闭", "开启"].index(restoreFaces)
        # resizeMode = ["just_resize", "crop_and_resize ", "resize_and_fill"].index(resizeMode)
        vaeId = get_vad_uuid_by_vad_name(vaeId)

        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        sourceImage = uploadLibLib(image, accessKey, secretKey)
        json_data = {
            "templateUuid": "07e00af4fc464c7ab55ff906f8acf1b7",
            "generateParams": {
                "vaeId": vaeId,
                "prompt": prompt,
                "negativePrompt": negativePrompt,
                "clipSkip": clipSkip,
                "sampler": sampler,
                "steps": steps,
                "cfgScale": cfgScale,
                "randSource": randSource,
                "seed": seed,
                "imgCount": imgCount,
                "restoreFaces": restoreFaces,
                "sourceImage": sourceImage,
                # "resizeMode": resizeMode,
                # "resizedWidth": resizedWidth,
                # "resizedHeight": resizedHeight,
                "mode": 0,
                "denoisingStrength": denoisingStrength,
                "inpaintParam": {},
                "additionalNetwork": lora_list,
                "controlNet": controlnet_list if controlnet_list else None
            }
        }
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/img2img/ultra", json_data)
        generateUuid = data["generateUuid"]
        json_data = {"generateUuid": generateUuid}
        image_tensors = []
        batched = None
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for image in data["images"]:
                    image_tensor = image_to_tensor_by_url(image["imageUrl"])
                    image_tensors.append(image_tensor)
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("执行失败")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)
