import os
import time

import torch

from ..server.generateServer import GenerateServer
from ..server.getModel import get_vad_uuid_by_vad_name
from ..server.imagesUtils import image_to_tensor_by_url
from ..server.uploadLibLib import uploadLibLib

CATEGORY_NAME = "ComfyUI-XingLiu"


class Text2ImageByAlphaNode:
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
                "width": ("INT", {
                    "default": 768,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
                    "display": "number"}),
                "height": ("INT", {
                    "default": 1024,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
                    "display": "number"}),
            },
            "optional": {
                "controlType": (["line", "depth", "pose", "IPAdapter"],),
                "controlImage": ("IMAGE",),
            }
        }

    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "text2img"

    def text2img(self,
                 auth,
                 prompt,
                 imgCount,
                 width,
                 height,
                 controlType=None,
                 controlImage=None):

        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        if controlImage != None:
            controlImage = uploadLibLib(controlImage, accessKey, secretKey)
        json_data = {
            "templateUuid": "5d7e67009b344550bc1aa6ccbfa1d7f4",
            "generateParams": {
                "prompt": prompt,
                "imageSize": {
                    "width": width,
                    "height": height,
                },
                "imgCount": imgCount,
                "steps": 30,
                "controlnet": {
                    "controlType": controlType,
                    "controlImage": controlImage,
                } if controlType is not None and controlImage is not None else {},
            }
        }

        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/text2img/ultra", json_data)
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
                raise Exception("error")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)


class Text2ImageCustomNode:
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
                "width": ("INT", {
                    "default": 768,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
                    "display": "number"}),
                "height": ("INT", {
                    "default": 1024,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
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
                "restoreFaces": (["off", "on"],),
                "resizeMode": (["just_resize", "crop_and_resize ", "resize_and_fill"],),
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
                    ["Automatic",
                     "1.5 - vae-ft-mse-840000-ema-pruned.safetensors",
                     "1.5 - klF8Anime2VAE_klF8Anime2VAE.ckpt",
                     "1.5 - color101VAE_v1.pt",
                     "1.5 - cute vae.safetensors",
                     "1.5 - ClearVAE_V2.3.safetensors",
                     "1.5 - difconsistencyRAWVAE_v10.pt",
                     "XL - sd_xl_vae_1.0"],),
                "hiResFix": ("HIRESFIX", {"forceInput": True}),
                "lora_list": ("LORA_LIST", {"forceInput": True}),
                "controlnet_list": ("CONTROLNET_LIST", {"forceInput": True})
            }
        }

    OUTPUT_NODE = True  # 表明它是一个输出节点
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "img2img"  # 核心功能函数名称，将运行这个类中的这个方法

    def img2img(self,
                auth,
                vaeId,
                checkPointId,
                prompt,
                negativePrompt,
                clipSkip,
                sampler,
                steps,
                cfgScale,
                width,
                height,
                randSource,
                seed,
                imgCount,
                restoreFaces,
                resizeMode,
                denoisingStrength,
                hiResFix=None,
                lora_list=None,
                controlnet_list=None):
        sampler = ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                   "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                   "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                   "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                   "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"].index(sampler)
        randSource = ["cpu", "gpu"].index(randSource)
        restoreFaces = ["off", "on"].index(restoreFaces)
        resizeMode = ["just_resize", "crop_and_resize ", "resize_and_fill"].index(resizeMode)
        vaeId = get_vad_uuid_by_vad_name(vaeId)
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        json_data = {
            "templateUuid": "e10adc3949ba59abbe56e057f20f883e",
            "generateParams": {
                "checkPointId": checkPointId,
                "vaeId": vaeId,
                "prompt": prompt,
                "negativePrompt": negativePrompt,
                "clipSkip": clipSkip,
                "sampler": sampler,
                "steps": steps,
                "cfgScale": cfgScale,
                "imageSize": {
                    "width": width,
                    "height": height,
                },
                "randSource": randSource,
                "seed": seed,
                "imgCount": imgCount,
                "restoreFaces": restoreFaces,
                "resizeMode": resizeMode,
                "mode": 0,
                "denoisingStrength": denoisingStrength,
                "hiResFixInfo": hiResFix,
                "additionalNetwork": lora_list,
                "controlNet": controlnet_list if controlnet_list else None
            }
        }
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/text2img", json_data)
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
                raise Exception("error")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)

class Text2ImageCustomAlphaNode:
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
                "width": ("INT", {
                    "default": 768,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
                    "display": "number"}),
                "height": ("INT", {
                    "default": 1024,
                    "min": 128,
                    "max": 1536,
                    "step": 1,
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
                "restoreFaces": (["off", "on"],),
                "resizeMode": (["just_resize", "crop_and_resize ", "resize_and_fill"],),
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
                    ["Automatic",
                     "1.5 - vae-ft-mse-840000-ema-pruned.safetensors",
                     "1.5 - klF8Anime2VAE_klF8Anime2VAE.ckpt",
                     "1.5 - color101VAE_v1.pt",
                     "1.5 - cute vae.safetensors",
                     "1.5 - ClearVAE_V2.3.safetensors",
                     "1.5 - difconsistencyRAWVAE_v10.pt",
                     "XL - sd_xl_vae_1.0"],),
                "hiResFix": ("HIRESFIX", {"forceInput": True}),
                "lora_list": ("LORA_LIST", {"forceInput": True}),
                "controlnet_list": ("CONTROLNET_LIST", {"forceInput": True})
            }
        }

    OUTPUT_NODE = True  # 表明它是一个输出节点
    RETURN_TYPES = ('IMAGE',)
    RETURN_NAMES = ('IMAGE',)
    FUNCTION = "img2img"  # 核心功能函数名称，将运行这个类中的这个方法

    def img2img(self,
                auth,
                vaeId,
                prompt,
                negativePrompt,
                clipSkip,
                sampler,
                steps,
                cfgScale,
                width,
                height,
                randSource,
                seed,
                imgCount,
                restoreFaces,
                resizeMode,
                denoisingStrength,
                hiResFix=None,
                lora_list=None,
                controlnet_list=None):
        sampler = ["Euler a", "Euler", "LMS", "HEUN", "DPM2", "DPM2 a", "DPM++ 2S a", "DPM++ 2M", "DPM++ SDE",
                   "DPM++ FAST", "DPM++ Adaptive", "LMS Karras", "DPM2 Karras", "DPM2 a Karras", "DPM++ 2S a",
                   "DPM++ 2M Karras", "DPM++ SDE Karras", "DDIM", "PLMS", "UNIPC", "DPM++ 2M SDE Karras",
                   "DPM++ 2M SDE EXPONENTIAL", "DPM++ 2M SDE Heun Karras", "DPM++ 2M SDE Heun Exponential",
                   "DPM++ 3M SDE Karras", "DPM++ 3M SDE Exponential", "Restart", "LCM"].index(sampler)
        randSource = ["cpu", "gpu"].index(randSource)
        restoreFaces = ["off", "on"].index(restoreFaces)
        resizeMode = ["just_resize", "crop_and_resize ", "resize_and_fill"].index(resizeMode)
        vaeId = get_vad_uuid_by_vad_name(vaeId)
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        json_data = {
            "templateUuid": "5d7e67009b344550bc1aa6ccbfa1d7f4",
            "generateParams": {
                "vaeId": vaeId,
                "prompt": prompt,
                "negativePrompt": negativePrompt,
                "clipSkip": clipSkip,
                "sampler": sampler,
                "steps": steps,
                "cfgScale": cfgScale,
                "imageSize": {
                    "width": width,
                    "height": height,
                },
                "randSource": randSource,
                "seed": seed,
                "imgCount": imgCount,
                "restoreFaces": restoreFaces,
                "resizeMode": resizeMode,
                "mode": 0,
                "denoisingStrength": denoisingStrength,
                "hiResFixInfo": hiResFix,
                "additionalNetwork": lora_list,
                "controlNet": controlnet_list if controlnet_list else None
            }
        }
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        data = generateServer._request_signature_uri("/api/generate/webui/text2img/ultra", json_data)
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
                raise Exception("error")
            time.sleep(5)

        if image_tensors:  # 确保列表不为空
            batched = torch.cat(image_tensors, dim=0)
        return (batched,)