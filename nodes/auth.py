import os

CATEGORY_NAME = "ComfyUI-XingLiu"


class MakeAuthNode:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "accessKey": ("STRING", {'default': ''}),
                "secretKey": ("STRING", {'default': ''}),
            },
        }

    OUTPUT_NODE = True  # 表明它是一个输出节点
    # 输出的数据类型，需要大写
    RETURN_TYPES = ('AUTH',)
    RETURN_NAMES = ('auth',)
    FUNCTION = "save_auth_info"  # 核心功能函数名称，将运行这个类中的这个方法

    def save_auth_info(self, accessKey, secretKey):
        if not accessKey or not secretKey:
            raise ValueError('Appkey and Appsecret are required')
        os.environ['LibLibAccessKey'] = accessKey
        os.environ['LibLibSecretKey'] = secretKey
        auth = {
            'accessKey': accessKey,
            'secretKey': secretKey
        }
        return (auth,)
