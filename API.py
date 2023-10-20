import time

API_KEY = 'eCPemseijSmlpjCWbm59D5fc3zQEaoI40rSvq5Rm0f1wY1ok3D6Hhvlhi0a5V2B2'
SECRET = 'o5YmoZb8AamTH0gPcfU4Y7C90xxtWrJJxRutXLtEl80sFI9FsPAfXKB6ksHiB3fS'
BASE_URL = 'https://testnet.binancefuture.com'


import requests
import json
import hashlib
import hmac

def getVelas(market, interval, limit):
    params = {
        'symbol': market,
        'interval': interval,
        'limit': limit,
    }
    response = requests.get(BASE_URL+'/dapi/v1/klines', params=params)
    return list(map(lambda x: { 'open_time': int(x[0]), 'open': float(x[1]), 'high': float(x[2]), 'low': float(x[3]), 'close': float(x[4]) }, json.loads(response.text)))

def anadirVela(market, interval, velas):
    params = {
        'symbol': market,
        'interval': interval,
        'limit': 1,
    }
    response = requests.get(BASE_URL+'/dapi/v1/klines', params=params)
    data = json.loads(response.text)[0]
    velaObject = { 'open_time': int(data[0]), 'open': float(data[1]), 'high': float(data[2]), 'low': float(data[3]), 'close': float(data[4]) }
    velas.append(velaObject)
    velas.pop(0)
    return velas

def new_trade(market, op_type, quantity):
    params = {
        'symbol': market,
        'side': op_type,
        'type': 'MARKET',
        'quantity': quantity,
        'timestamp': int(time.time() * 1000)
    }
    query_string = '&'.join([f'{key}={params[key]}' for key in params ])
    signature = hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    params['signature'] = signature
    response = requests.post(BASE_URL, params=params, headers={'X-MBX-APIKEY': API_KEY})

    if response.status_code == 200:
        print(f'Operación de tipo {op_type} abierta en {market}. Cantidad = {quantity}')
    else:
        print(f'Error abriendo operación de tipo {op_type} en {market}. Cantidad = {quantity}')
