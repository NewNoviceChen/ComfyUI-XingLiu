import base64
import hmac
import time
import uuid
from hashlib import sha1

import requests

_BASE_URL = 'https://openapi.liblibai.cloud'


class GenerateServer:
    def __init__(self, accessKey, secretKey):
        self._accessKey = accessKey
        self._secretKey = secretKey

    def _create_signature_uri(self, uri):
        # 当前毫秒时间戳
        timestamp = str(int(time.time() * 1000))
        # 随机字符串
        signature_nonce = str(uuid.uuid4())
        content = '&'.join((uri, timestamp, signature_nonce))

        # 生成签名
        digest = hmac.new(self._secretKey.encode(), content.encode(), sha1).digest()
        # 移除为了补全base64位数而填充的尾部等号
        sign = base64.urlsafe_b64encode(digest).rstrip(b'=').decode()
        signature_uri = f'{_BASE_URL}{uri}?AccessKey={self._accessKey}&Signature={sign}&Timestamp={timestamp}&SignatureNonce={signature_nonce}'
        return signature_uri

    def _request_signature_uri(self, uri, params):
        signature_uri = self._create_signature_uri(uri)
        response = requests.post(signature_uri,
                                 headers={'Content-Type': 'application/json'},
                                 json=params)
        if response.status_code != 200:
            raise ValueError(f"Request failed with status code {response.status_code}", response.text)

        data = response.json()
        if data.get('code') != 0:
            raise ValueError(data.get('msg', 'Unknown error'))

        return data['data']


