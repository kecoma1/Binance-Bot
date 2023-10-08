import hashlib
import hmac
import requests
import time
from datetime import datetime

api_key = 'mlnsfeYmkrf4rh8tJnZtttCQ5DYNcLZ61Ujc0RBqSWxh0477J3YSlJ8zKpshSzTl'
api_secret = 'wLqsXNCgU9mIUe0OtScueIQBcM9acV2PuEvF3deYqhGPnUJxyETcCQKMAkjyTBNe'
base_url = 'https://testnet.binance.vision/api/v3/order'

quantity = 20

while True:
    # Parámetros de la solicitud
    params = {
        'symbol': 'ADAUSDT',
        'side': 'BUY',
        'type': 'MARKET',
        'timestamp': int(time.time() * 1000),
        'quantity': quantity,
    }

    # Crear cadena de consulta ordenada
    query_string = '&'.join([f'{key}={params[key]}' for key in params])

    # Concatenar con la clave secreta y calcular la firma
    signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

    # Agregar la firma a los parámetros de la solicitud
    params['signature'] = signature

    # Enviar la solicitud POST
    response = requests.post(base_url, params=params, headers={'X-MBX-APIKEY': api_key})

    now = datetime.now()
    print(f'Comprados {quantity} ADA {now.strftime("%m/%d/%Y, %H:%M:%S")}')

    time.sleep(24*3600)
