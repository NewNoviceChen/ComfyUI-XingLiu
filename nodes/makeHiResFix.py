import json

from ..server.getModel import get_upscaler_keys

CATEGORY_NAME = "ComfyUI-XingLiu"


class MakeHiResFixNode:

    def __init__(self):
        pass

    CATEGORY = CATEGORY_NAME

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "hiresSteps": ("INT", {
                    "default": 20,
                    "min": 1,
                    "max": 30,
                    "step": 1,
                    "display": "number"}),
                "hiresDenoisingStrength": ("FLOAT", {
                    "default": 0.75,
                    "min": 0.00,
                    "max": 1.00,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "number"}),
                "upscaler": (["Latent", "Latent (antialiased)", "Latent (bicubic)", "Latent (bicubic antialiased)",
                              "Latent (nearest)", "Latent (nearest-exact)", "Lanczos", "Nearest", "ESRGAN_4x", "LDSR",
                              "R-ESRGAN_4x+", "R-ESRGAN_4x+ Anime6B", "ScuNET GAN", "ScuNET PSNR", "SwinIR_4x",
                              "4x-UltraSharp", "8x-NMKD-Superscale", "4x_NMKD-Siax_200k",
                              "4x_NMKD-Superscale-SP_178000_G", "4x-AnimeSharp",
                              "4x_foolhardy_Remacri", "BSRGAN", "DAT 2", "DAT 3", "DAT 4", "4x-DeCompress",
                              "4x-DeCompress Strong"],),
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
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ('HIRESFIX',)
    RETURN_NAMES = ('hiResFix',)
    FUNCTION = "make_hiresfix"

    def make_hiresfix(self,
                      hiresSteps,
                      hiresDenoisingStrength,
                      upscaler,
                      resizedWidth,
                      resizedHeight
                      ):
        upscaler = ["Latent", "Latent (antialiased)", "Latent (bicubic)", "Latent (bicubic antialiased)",
                    "Latent (nearest)", "Latent (nearest-exact)", "Lanczos", "Nearest", "ESRGAN_4x", "LDSR",
                    "R-ESRGAN_4x+", "R-ESRGAN_4x+ Anime6B", "ScuNET GAN", "ScuNET PSNR", "SwinIR_4x",
                    "4x-UltraSharp", "8x-NMKD-Superscale", "4x_NMKD-Siax_200k",
                    "4x_NMKD-Superscale-SP_178000_G", "4x-AnimeSharp",
                    "4x_foolhardy_Remacri", "BSRGAN", "DAT 2", "DAT 3", "DAT 4", "4x-DeCompress",
                    "4x-DeCompress Strong"].index(upscaler)
        hiresfix = {
            "hiresSteps": hiresSteps,
            "hiresDenoisingStrength": hiresDenoisingStrength,
            "upscaler": upscaler,
            "resizedWidth": resizedWidth,
            "resizedHeight": resizedHeight
        }
        return (json.dumps(hiresfix),)
