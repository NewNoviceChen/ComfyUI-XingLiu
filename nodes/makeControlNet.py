import json
import os

from ..server.getF1AnnotationParameters import get_annotation_parameters_by_namer
from ..server.uploadLibLib import uploadLibLib

CATEGORY_NAME = "ComfyUI-XingLiu"


class MakeControlNetNode:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "auth": ("AUTH",),
                "image": ("IMAGE", {'default': '', "display_name": "图像"}),
                "preprocessor": (
                    ["线稿类 - Canny（硬边缘）",
                     "线稿类 - SoftEdge（软边缘）- hed",
                     "线稿类 - SoftEdge（软边缘）- hed_safe",
                     "线稿类 - SoftEdge（软边缘）- pidinet",
                     "线稿类 - SoftEdge（软边缘）- pidinet_safe",
                     "线稿类 - SoftEdge（软边缘）- softedge_teed",
                     "线稿类 - SoftEdge（软边缘）- softedge_anyline",
                     "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_pidinet(涂鸦- 手绘)",
                     "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_xdog (涂鸦- 强化边缘)",
                     "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_hed(涂鸦 -合成)",
                     "线稿类 - Lineart（线稿）- lineart_realistic (写实线稿提取)",
                     "线稿类 - Lineart（线稿）- lineart standard (标准线稿提取 -白底黑线反色)",
                     "线稿类 - Lineart（线稿）- lineart coarse (粗略线稿提取)",
                     "线稿类 - Lineart（线稿）- lineart_anime (动漫线稿提取)",
                     "线稿类 - Lineart（线稿）- lineart_anime_denoise(动漫线稿提取-去噪)",
                     "空间关系类 - Depth（深度图）- depth_midas",
                     "空间关系类 - Depth（深度图）- depth_leres (LeRes 深度图估算)",
                     "空间关系类 - Depth（深度图）- depth_leres++",
                     "空间关系类 - Depth（深度图）- depth_zoe (ZoE 深度图估算)",
                     "空间关系类 - Depth（深度图）- depth_hand_refiner", "空间关系类 - Depth（深度图）- depth_anything",
                     "空间关系类 - Normal（正态）- normal_map",
                     "空间关系类 - Normal（正态）- normal bae (Bae 法线贴图提取)",
                     "姿态类 - OpenPose（姿态）- mediapipe_face",
                     "姿态类 - OpenPose（姿态）- openpose (OpenPose 姿态)",
                     "姿态类 - OpenPose（姿态）- openpose hand (OpenPose 姿态及手部)",
                     "姿态类 - OpenPose（姿态）- openpose face (OpenPose 姿态及脸部)",
                     "姿态类 - OpenPose（姿态）- openpose_faceonly (OpenPose 仅脸部)",
                     "姿态类 - OpenPose（姿态）- openpose_full (OpenPose 姿态、手部及脸部)",
                     "姿态类 - OpenPose（姿态）- dw_openpose_full",
                     "画面参考 - Tile/Blur（分块/模糊）- tile_resample(分块重采样)",
                     "画面参考 - Tile/Blur（分块/模糊）- tile_colorfix",
                     "画面参考 - Tile/Blur（分块/模糊）- tile_colorfix+sharp",
                     "画面参考 - Tile/Blur（分块/模糊）- blur_gaussian",
                     "风格迁移 - IP-Adapter - ip-adapter-siglip",
                     "局部重绘 - Inpaint（局部重绘）- inpaint_global_harmonious",
                     "局部重绘 - Inpaint（局部重绘）- inpaint_only",
                     "局部重绘 - Inpaint（局部重绘）- inpaint_only+lama"
                     ], {"display_name": "预处理器"}
                ),
                "controlWeight": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
                "startingControlStep": ("FLOAT", {
                    "default": 0.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
                "endingControlStep": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
                "pixelPerfect": (["on", "off"],),
                "controlMode": (["balanced", "prompt_important", "controlnet_important"],),
                "resizeMode": (["just_resize", "crop_and_resize", "resize_and_fill"],),
            }
        }

    OUTPUT_NODE = True  # 表明它是一个输出节点
    # 输出的数据类型，需要大写
    RETURN_TYPES = ('CONTROLNET',)
    RETURN_NAMES = ('ControlNet',)
    FUNCTION = "make_controlnet"  # 核心功能函数名称，将运行这个类中的这个方法

    def make_controlnet(self,
                        auth,
                        image,
                        preprocessor,
                        controlWeight,
                        startingControlStep,
                        endingControlStep,
                        pixelPerfect,
                        controlMode,
                        resizeMode,
                        ):
        accessKey = os.getenv("LibLibAccessKey")
        secretKey = os.getenv("LibLibSecretKey")
        # 映射枚举值到实际参数
        pixel_perfect = 1 if pixelPerfect == "on" else 0
        control_mode = ["balanced", "prompt_important", "controlnet_important"].index(controlMode)
        resize_mode = ["just_resize", "crop_and_resize", "resize_and_fill"].index(resizeMode)
        batch_size, height, width, channels = image.shape
        sourceImage = uploadLibLib(image, accessKey, secretKey)
        preprocessor_detail = get_annotation_parameters_by_namer(preprocessor)
        controlNet = {
            "sourceImage": sourceImage,
            "width": width,
            "height": height,
            "control_weight": controlWeight,
            "starting_control_step": startingControlStep,
            "ending_control_step": endingControlStep,
            "pixel_perfect": pixel_perfect,
            "control_mode": control_mode,
            "resize_mode": resize_mode,
        }
        json1 = json.dumps(controlNet)
        json2 = json.dumps(preprocessor_detail)

        dict1 = json.loads(json1)
        dict2 = json.loads(json2)
        dict1.update(dict2)  # 相同键会被 dict2 的值覆盖
        json_data = json.dumps(dict1)
        return (json_data,)


class MergeControlNetNode:
    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ControlNet_1": ("CONTROLNET", {"forceInput": True})
            },
            "optional": {
                "ControlNet_2": ("CONTROLNET", {"forceInput": True}),
                "ControlNet_3": ("CONTROLNET", {"forceInput": True}),
                "ControlNet_4": ("CONTROLNET", {"forceInput": True})
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ('CONTROLNET_LIST',)
    RETURN_NAMES = ('ControlNet组合',)
    FUNCTION = "make_controlnet_list"

    def make_controlnet_list(self, ControlNet_1, ControlNet_2=None, ControlNet_3=None,
                             ControlNet_4=None):
        # 创建一个空列表
        controlnet_list = []
        # 添加所有非None的controlnet_info到列表中
        if ControlNet_1 is not None and ControlNet_1 != '':
            info = json.loads(ControlNet_1)
            info["unitOrder"] = 1
            controlnet_list.append(info)
        if ControlNet_2 is not None and ControlNet_2 != '':
            info = json.loads(ControlNet_2)
            info["unitOrder"] = 2
            controlnet_list.append(info)
        if ControlNet_3 is not None and ControlNet_3 != '':
            info = json.loads(ControlNet_3)
            info["unitOrder"] = 3
            controlnet_list.append(info)
        if ControlNet_4 is not None and ControlNet_4 != '':
            info = json.loads(ControlNet_4)
            info["unitOrder"] = 4
            controlnet_list.append(info)
        return (controlnet_list,)
