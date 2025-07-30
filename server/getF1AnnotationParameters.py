annotationParametersMap = {
    "线稿类 - Canny（硬边缘）": {
        "preprocessor": 1,
        "annotationParameters": {
            "canny": {
                "preprocessorResolution": 512,
                "lowThreshold": 100,
                "highThreshold": 200
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - SoftEdge（软边缘）- hed": {
        "preprocessor": 5,
        "annotationParameters": {
            "hed": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - SoftEdge（软边缘）- hed_safe": {
        "preprocessor": 6,
        "annotationParameters": {
            "hedSafe": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - SoftEdge（软边缘）- pidinet": {
        "preprocessor": 17,
        "annotationParameters": {
            "pidinet": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - SoftEdge（软边缘）- pidinet_safe": {
        "preprocessor": 18,
        "annotationParameters": {
            "pidinetSafe": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - SoftEdge（软边缘）- softedge_teed": {
        "preprocessor": 58,
        "annotationParameters": {
            "softedgeTeed": {
                "preprocessorResolution": 512,
                "safeSteps": 2
            }
        },
        "model": "3e6860a3b9444f25ae07d9c1b5d1ba9e"
    },
    "线稿类 - SoftEdge（软边缘）- softedge_anyline": {
        "preprocessor": 65,
        "annotationParameters": {
            "softedgeAnyline": {
                "preprocessorResolution": 512,
                "safeSteps": 2
            }
        },
        "model": "3e6860a3b9444f25ae07d9c1b5d1ba9e"
    },
    # "线稿类 - MLSD（直线） - mlsd (M-LSD 直线线条检测)": {
    #     "preprocessor": 8,
    #     "annotationParameters": {
    #         "mlsd": {
    #             "preprocessorResolution": 512,
    #             "valueThreshold": 0.1,
    #             "distanceThreshold": 0.1
    #         }
    #     }
    # },
    "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_pidinet(涂鸦- 手绘)": {
        "preprocessor": 20,
        "annotationParameters": {
            "scribblePidinet": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_xdog (涂鸦- 强化边缘)": {
        "preprocessor": 21,
        "annotationParameters": {
            "scribbleXdog": {
                "preprocessorResolution": 512,
                "XDoGThreshold": 32
            }
        }
    },
    "线稿类 - Scribble/Sketch（涂鸦/草图）- scribble_hed(涂鸦 -合成)": {
        "preprocessor": 22,
        "annotationParameters": {
            "scribbleHed": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Lineart（线稿）- lineart_realistic (写实线稿提取)": {
        "preprocessor": 29,
        "annotationParameters": {
            "lineartRealistic": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Lineart（线稿）- lineart standard (标准线稿提取 -白底黑线反色)": {
        "preprocessor": 32,
        "annotationParameters": {
            "lineartStandard": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Lineart（线稿）- lineart coarse (粗略线稿提取)": {
        "preprocessor": 30,
        "annotationParameters": {
            "lineartCoarse": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Lineart（线稿）- lineart_anime (动漫线稿提取)": {
        "preprocessor": 31,
        "annotationParameters": {
            "lineartAnime": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "线稿类 - Lineart（线稿）- lineart_anime_denoise(动漫线稿提取-去噪)": {
        "preprocessor": 36,
        "annotationParameters": {
            "lineartAnimeDenoise": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_midas": {
        "preprocessor": 2,
        "annotationParameters": {
            "depthMidas": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_leres (LeRes 深度图估算)": {
        "preprocessor": 3,
        "annotationParameters": {
            "depthLeres": {
                "preprocessorResolution": 512,
                "removeNear": 0,
                "removeBackground": 0
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_leres++": {
        "preprocessor": 4,
        "annotationParameters": {
            "depthLeresPlus": {
                "preprocessorResolution": 512,
                "removeNear": 0,
                "removeBackground": 0
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_zoe (ZoE 深度图估算)": {
        "preprocessor": 25,
        "annotationParameters": {
            "depthZoe": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_hand_refiner": {
        "preprocessor": 57,
        "annotationParameters": {
            "depthHandRefiner": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "空间关系类 - Depth（深度图）- depth_anything": {
        "preprocessor": 64,
        "annotationParameters": {
            "depthAnything": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    # "segmentation": {
    #     "preprocessor": 23,
    #     "annotationParameters": {
    #         "segmentation": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # },
    # "oneformer_coco": {
    #     "preprocessor": 27,
    #     "annotationParameters": {
    #         "oneformerCoco": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # },
    # "oneformer_ade20k": {
    #     "preprocessor": 28,
    #     "annotationParameters": {
    #         "oneformerAde20k": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # },
    # "anime_face_segment": {
    #     "preprocessor": 54,
    #     "annotationParameters": {
    #         "animeFaceSegment": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # },
    "空间关系类 - Normal（正态）- normal_map": {
        "preprocessor": 9,
        "annotationParameters": {
            "normalMap": {
                "preprocessorResolution": 512,
                "backgroundThreshold": 0.4
            }
        },
        "model": "e51fdccdf3b8417aab246bde40b5f360"
    },
    "空间关系类 - Normal（正态）- normal bae (Bae 法线贴图提取)": {
        "preprocessor": 26,
        "annotationParameters": {
            "normalBae": {
                "preprocessorResolution": 512
            }
        },
        "model": "e51fdccdf3b8417aab246bde40b5f360"
    },
    "姿态类 - OpenPose（姿态）- mediapipe_face": {
        "preprocessor": 7,
        "annotationParameters": {
            "mediapipeFace": {
                "preprocessorResolution": 512,
                "maxFaces": 1,
                "minConfidence": 0.5
            }
        },
        "model": "7c6d889cb9c04b78858d8fece80f9f85"
    },
    "姿态类 - OpenPose（姿态）- openpose (OpenPose 姿态)": {
        "preprocessor": 10,
        "annotationParameters": {
            "openpose": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "姿态类 - OpenPose（姿态）- openpose hand (OpenPose 姿态及手部)": {
        "preprocessor": 11,
        "annotationParameters": {
            "openposeHand": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "姿态类 - OpenPose（姿态）- openpose face (OpenPose 姿态及脸部)": {
        "preprocessor": 12,
        "annotationParameters": {
            "openposeFace": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "姿态类 - OpenPose（姿态）- openpose_faceonly (OpenPose 仅脸部)": {
        "preprocessor": 13,
        "annotationParameters": {
            "openposeFaceonly": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "姿态类 - OpenPose（姿态）- openpose_full (OpenPose 姿态、手部及脸部)": {
        "preprocessor": 14,
        "annotationParameters": {
            "openposeFull": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    "姿态类 - OpenPose（姿态）- dw_openpose_full": {
        "preprocessor": 45,
        "annotationParameters": {
            "dwOpenposeFull": {
                "preprocessorResolution": 512
            }
        },
        "model": "13c1e1b96ba64f9cbb2b54f89b5fe873"
    },
    # "姿态类 - OpenPose（姿态）- animal_openpose": {
    #     "preprocessor": 53,
    #     "annotationParameters": {
    #         "animalOpenpose": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # },
    # "姿态类 - OpenPose（姿态）- densepose_parula": {
    #     "preprocessor": 56,
    #     "annotationParameters": {
    #         "denseposeParula": {
    #             "preprocessorResolution": 512
    #         }
    #     }
    # }
    "画面参考 - Tile/Blur（分块/模糊）- tile_resample(分块重采样)": {
        "preprocessor": 34,
        "annotationParameters": {
            "tileResample": {
                "downSamplingRate": 1
            }
        },
        "model": "a696b5bdadc740119fd76505b33d6898"
    },
    "画面参考 - Tile/Blur（分块/模糊）- tile_colorfix": {
        "preprocessor": 43,
        "annotationParameters": {
            "tileColorfix": {
                "variation": 8
            }
        },
        "model": "a696b5bdadc740119fd76505b33d6898"
    },
    "画面参考 - Tile/Blur（分块/模糊）- tile_colorfix+sharp": {
        "preprocessor": 44,
        "annotationParameters": {
            "tileColorfixSharp": {
                "variation": 8,
                "sharpness": 1
            }
        },
        "model": "a696b5bdadc740119fd76505b33d6898"
    },
    "画面参考 - Tile/Blur（分块/模糊）- blur_gaussian": {
        "preprocessor": 52,
        "annotationParameters": {
            "blurGaussian": {
                "preprocessorResolution": 512,
                "sigma": 9
            }
        },
        "model": "a696b5bdadc740119fd76505b33d6898"
    },
    "风格迁移 - IP-Adapter - ip-adapter-siglip": {
        "preprocessor": 66,
        "annotationParameters": {
            "ipAdapterSiglip": {
                "preprocessorResolution": 512
            }
        },
        "model": "c6ed70879cf011ef96d600163e37ec70"
    },
    "局部重绘 - Inpaint（局部重绘）- inpaint_global_harmonious": {
        "preprocessor": 40,
        "annotationParameters": {
            "inpaintGlobalHarmonious": {}
        },
        "model": "31df01fc271d484ca4d496179d69a665"
    },
    "局部重绘 - Inpaint（局部重绘）- inpaint_only": {
        "preprocessor": 41,
        "annotationParameters": {
            "inpaintOnly": {}
        },
        "model": "31df01fc271d484ca4d496179d69a665"
    },
    "局部重绘 - Inpaint（局部重绘）- inpaint_only+lama": {
        "preprocessor": 42,
        "annotationParameters": {
            "inpaintOnlyLama": {}
        },
        "model": "31df01fc271d484ca4d496179d69a665"
    }
}

def get_annotation_parameters_by_namer(preprocessor):
    return annotationParametersMap[preprocessor]
