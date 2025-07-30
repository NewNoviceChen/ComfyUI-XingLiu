import os
from io import BytesIO
from urllib.parse import urlparse

import requests
from PIL import Image
from torchvision import transforms


def get_image_name_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    filename = os.path.basename(path)
    return filename


def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"图片已成功下载到: {save_path}")
    else:
        print(f"下载失败，HTTP 状态码: {response.status_code}")


def image_to_tensor_by_url(url):
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content))
    image_tensor = transforms.ToTensor()(img)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.permute(0, 2, 3, 1)
    return image_tensor


def image_to_tensor(path, image_name):
    image = Image.open(os.path.join(path, image_name)).convert("RGB")
    image_tensor = transforms.ToTensor()(image)
    image_tensor = image_tensor.unsqueeze(0)
    image_tensor = image_tensor.permute(0, 2, 3, 1)
    return image_tensor
