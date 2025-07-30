checkPointUuidMap = {
    "星流Star-3 Alpha文生图": "5d7e67009b344550bc1aa6ccbfa1d7f4",
    "星流Star-3 Alpha图生图": "07e00af4fc464c7ab55ff906f8acf1b7",
    "F.1文生图": "6f7c4652458d4802969f8d089cf5b91f",
    "F.1图生图": "63b72710c9574457ba303d9d9b8df8bd",
}

vad_map = {
    '通用 - Automatic': '',
    '基础算法 1.5 - vae-ft-mse-840000-ema-pruned.safetensors': '2c1a337416e029dd65ab58784e8a4763',
    '基础算法 1.5 - klF8Anime2VAE_klF8Anime2VAE.ckpt': 'd4a03b32d8d59552194a9453297180c1',
    '基础算法 1.5 - color101VAE_v1.pt': 'd9be20ad5a7195ff0d97925e5afc7912',
    '基础算法 1.5 - cute vae.safetensors': '88ae7501f5194e691a1dc32d6f7c6f1a',
    '基础算法 1.5 - ClearVAE_V2.3.safetensors': '73f6e055eade7a85bda2856421d786fe',
    '基础算法 1.5 - difconsistencyRAWVAE_v10.pt': '5e93d0d2a64143a9d28988e75f28cb29',
    '基础算法 XL - sd_xl_vae_1.0': '3cefd3e4af2b8effb230b960da41a980',
}

lora_map = {
    "人像摄影 - 基础算法 F.1 - Filmfotos_日系胶片写真": "b59f7eb734864a74ba476af3aa28c2f3",
    "人像摄影 - 基础算法 F.1 - 极氪白白酱F.1-人像V6MAX": "169505112cee468b95d5e4a5db0e5669",
    "电商场景 - 基础算法 F.1 - 电商-F.1- | 运营启动页": "76af914cc3434937aa13aeb038aae838",
    "视觉海报 - 基础算法 F.1 - UNIT-F.1-MandelaEffect-LoRA": "50284151e507431facc2325cd62f73a3",
    "创意插画 - 基础算法 F.1 - 万物调节丨Flux 情绪插画": "be3909c5d7114d3b8717e966c884d3e1",
    "创意插画 - 基础算法 F.1 - 嘉嘉_国潮插画_F.1": "be3909c5d7114d3b8717e966c884d3e1",
    "创意插画 - 基础算法 F.1 - 风月无边illustrations": "be3909c5d7114d3b8717e966c884d3e1",
    "创意插画 - 基础算法 F.1 - 岩彩材质绘画": "be3909c5d7114d3b8717e966c884d3e1",
}
upscaler_map = {
    "Latent": 0,
    "Latent (antialiased)": 1,
    "Latent (bicubic)": 2,
    "Latent (bicubic antialiased)": 3,
    "Latent (nearest)": 4,
    "Latent (nearest-exact)": 5,
    "Lanczos": 6,
    "Nearest": 7,
    "ESRGAN_4x": 8,
    "LDSR": 9,
    "R-ESRGAN_4x+": 10,
    "R-ESRGAN_4x+ Anime6B": 11,
    "ScuNET GAN": 12,
    "ScuNET PSNR": 13,
    "SwinIR_4x": 14,
    "4x-UltraSharp": 15,
    "8x-NMKD-Superscale": 16,
    "4x_NMKD-Siax_200k": 17,
    "4x_NMKD-Superscale-SP_178000_G": 18,
    "4x-AnimeSharp": 19,
    "4x_foolhardy_Remacri": 20,
    "BSRGAN": 21,
    "DAT 2": 22,
    "DAT 3": 23,
    "DAT 4": 24,
    "4x-DeCompress": 25,
    "4x-DeCompress Strong": 26,
}


def get_vad_uuid_by_vad_name(vad_name):
    return vad_map[vad_name]


def get_check_point(check_point_name):
    return checkPointUuidMap[check_point_name]


def get_lora(lora_name):
    return lora_map[lora_name]


def get_upscaler(upscaler_name):
    return upscaler_map[upscaler_name]

def get_upscaler_keys():
    return upscaler_map.keys()
