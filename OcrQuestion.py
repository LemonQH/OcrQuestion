# -*- coding: utf-8 -*-
import sys
import uuid
import requests
import base64
import hashlib
import json

from imp import reload


import time

reload(sys)

YOUDAO_URL = 'https://openapi.youdao.com/ocrquestionapi'
APP_KEY = 'your id'
APP_SECRET = 'your secret'


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers)


def connect(pic_path):
    f = open(pic_path, 'rb')  # 二进制方式打开图文件
    q = base64.b64encode(f.read()).decode('utf-8')  # 读取文件内容，转换为base64编码
    f.close()

    data = {}
    data['q'] = q
    data['signType'] = 'v2'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(q) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['salt'] = salt
    data['sign'] = sign

    response = do_request(data)
    result=json.loads(str(response.content, 'utf-8'))
    if result['errorCode']=='0':
        #print(result['data'])
        return result['data']

