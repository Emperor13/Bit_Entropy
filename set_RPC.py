import json
import requests

def write_json_file(username, password):
    data = {
        "username": username,
        "password": password
    }

    with open("setup_connect.json", "w") as file:
        json.dump(data, file)

def read_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def connect():
    read = read_json_file("setup_connect.json")
    rpc_user = read["username"]
    rpc_password = read["password"]
    rpc_port = 8332

    auth = requests.auth.HTTPBasicAuth(rpc_user, rpc_password)
    headers = {'content-type': 'application/json'}

    url = f'http://localhost:{rpc_port}/'

    method = 'getblockcount'
    params = []

    payload = {
        'method': method,
        'params': params,
        'jsonrpc': '2.0',
        'id': 0,
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth).json()
    result = json.dumps(response['result'], indent=3)

    if result == 'null':
        error = json.dumps(response, indent=3)
        print(error)

    else:
        print("%s Block" % result)


if __name__ == "__main__":

    #RPC_USR = input()
    #RPC_PASS = input()
    #write_json_file(RPC_USR, RPC_PASS)

    read = read_json_file("setup_connect.json")
    username = read["username"]
    password = read["password"]
    #print(username)
    #print(password)
    connect()