API_KEY = 'eCPemseijSmlpjCWbm59D5fc3zQEaoI40rSvq5Rm0f1wY1ok3D6Hhvlhi0a5V2B2'
SECRET = 'o5YmoZb8AamTH0gPcfU4Y7C90xxtWrJJxRutXLtEl80sFI9FsPAfXKB6ksHiB3fS'
BASE_URL = 'https://testnet.binance.vision/api/v3/order'

from datetime import datetime
import requests
import hashlib
import hmac
import time

quantity = 20
symbol = 'ADAUSDT'


while True:
    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'MARKET',
        'quantity': quantity,
        'timestamp': int(time.time() * 1000)
    }

    query_string = '&'.join([f'{key}={params[key]}' for key in params ])

    signature = hmac.new(SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    params['signature'] = signature

    response = requests.post(BASE_URL, params=params, headers={'X-MBX-APIKEY': API_KEY})

    now = datetime.now()

    print(f'Compra de {quantity} {symbol} efectuada {now.strftime("%d/%m/%Y, %H:%M:%S")}')

    time.sleep(24*3600)