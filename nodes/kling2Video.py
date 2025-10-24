import os
import time

from ..server.uploadLibLib import uploadLibLib
from ..server.mediaUtils import download_video
from ..server.generateServer import GenerateServer
from comfy_api.input_impl import VideoFromFile
import folder_paths

CATEGORY_NAME = "ComfyUI-XingLiu"


class Text2VideoKlingNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "model": (["kling-v2-master", "kling-v1-6", "kling-v2-1-master"], {"default": "kling-v2-1-master"}),
                "prompt": ("STRING", {"multiline": True}),
                "aspectRatio": (["1:1", "9:16", "16:9"], {"default": "16:9"}),
                "duration": ("INT", {
                    "default": 5,
                    "min": 5,
                    "max": 10,
                    "step": 1,
                    "display": "number"}),
            }
        }

    RETURN_TYPES = ('VIDEO',)
    RETURN_NAMES = ('VIDEO',)
    FUNCTION = "text2video"

    def text2video(self, auth, model, prompt, aspectRatio, duration):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        json_data = {
            "templateUuid": "61cd8b60d340404394f2a545eeaf197a",
            "generateParams": {
                "model": model,
                "prompt": prompt,
                "promptMagic": 1,
                "aspectRatio": aspectRatio,
                "duration": duration
            }
        }
        data = generateServer._request_signature_uri("/api/generate/video/kling/text2video", json_data)
        generateUuid = data["generateUuid"]
        json_data = {"generateUuid": generateUuid}
        video_path = ""
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for video in data["videos"]:
                    video_path = download_video(video["videoUrl"], folder_paths.get_temp_directory())
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("error")
            time.sleep(5)
        return (VideoFromFile(video_path),)


class Image2VideoKlingNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "model": (
                ["kling-v2-master", "kling-v1-6", "kling-v2-1-master", "kling-v2-1"], {"default": "kling-v2-1"}),
                "prompt": ("STRING", {"multiline": True}),
                "mode": (["std", "pro"], {"default": "std"}),
                "duration": ("INT", {
                    "default": 5,
                    "min": 5,
                    "max": 10,
                    "step": 1,
                    "display": "number"}),
            },
            "optional": {
                "startFrame": ("IMAGE",),
                "endFrame": ("IMAGE",),
            }
        }

    RETURN_TYPES = ('VIDEO',)
    RETURN_NAMES = ('VIDEO',)
    FUNCTION = "image2video"

    def image2video(self, auth, model, prompt, mode, duration, startFrame=None, endFrame=None):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        generateServer = GenerateServer(accessKey=accessKey, secretKey=secretKey)
        if startFrame is not None:
            startFrame = uploadLibLib(startFrame, accessKey, secretKey)
        if endFrame is not None:
            endFrame = uploadLibLib(endFrame, accessKey, secretKey)
        json_data = {
            "templateUuid": "180f33c6748041b48593030156d2a71d",
            "generateParams": {
                "model": model,
                "prompt": prompt,
                "promptMagic": 1,
                "mode": mode,
                "startFrame": startFrame,
                "endFrame": endFrame,
                "duration": duration
            }
        }
        data = generateServer._request_signature_uri("/api/generate/video/kling/img2video", json_data)
        generateUuid = data["generateUuid"]
        json_data = {"generateUuid": generateUuid}
        video_path = ""
        while True:
            data = generateServer._request_signature_uri("/api/generate/webui/status", json_data)
            if data["generateStatus"] == 5:
                for video in data["videos"]:
                    video_path = download_video(video["videoUrl"], folder_paths.get_temp_directory())
                break
            if data["generateStatus"] == 6 or data["generateStatus"] == 7:
                raise Exception("error")
            time.sleep(5)
        return (VideoFromFile(video_path),)
