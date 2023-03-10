# -*- coding: utf-8 -*-
"""connect node.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1bI8GCrnA2Gi4_EmCE2TbNsoy8vrhKK
"""

import json
import requests

def connect_node(rpc_user:str, rpc_pass:str, rpc_port=8332) -> str:
    auth = requests.auth.HTTPBasicAuth(rpc_user, rpc_pass)
    headers = {'content-type': 'application/json'}
    url = f'http://localhost:{rpc_port}/'

    method = 'getblockcount'
    params = []

    # เตรียมข้อมูลสำหรับส่งคำขอไปยัง Bitcoin node
    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 0,
    }

    try:
        # ส่งคำขอไปยัง Bitcoin node
        response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
        # ตรวจสอบสถานะการเชื่อมต่อ
        if response.status_code == 200:
            status = "Node Connected!!"
            data = response.json()
            result = json.dumps(data['result'])

            if result == 'null':
                error = json.dumps(response)
                print(error)
            else:
                result = 'Block Height : ' + result

        else:
            pass
    except requests.exceptions.RequestException as e:
        status = "Node Disconnected!!"
    except UnboundLocalError:
        status = "Node Disconnected!!"

    return status


# ────────────────────────────────────────────────────────────────────────────────── #


def Block_Height(rpc_user:str, rpc_pass:str, rpc_port=8332) -> str:
    auth = requests.auth.HTTPBasicAuth(rpc_user, rpc_pass)
    headers = {'content-type': 'application/json'}
    url = f'http://localhost:{rpc_port}/'

    method = 'getblockcount'
    params = []

    # เตรียมข้อมูลสำหรับส่งคำขอไปยัง Bitcoin node
    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 1,
    }

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
        data = response.json()
        result = json.dumps(data['result'])
        if result == 'null':
            error = json.dumps(response)
            print(error)
        else:
            result = 'Block Height : ' + result
    except requests.exceptions.RequestException as e:
        result = "Node Disconnected!!"
    return result


# ────────────────────────────────────────────────────────────────────────────────── #


def __run__():
    rpc_user = 'milko1215'
    rpc_password = 'milkoNode'
    send = connect_node(rpc_user, rpc_password)
    print(send)

    get_getblockcount = Block_Height(rpc_user, rpc_password)
    print(get_getblockcount)


# ────────────────────────────────────────────────────────────────────────────────── #
def say_hello():
   print( 'Hello, world!' )

if __name__=="__main__":
    __run__()