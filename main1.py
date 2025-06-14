import json
import requests
from datetime import datetime
from wireguard_tools import WireguardKey

private_key = WireguardKey.generate()
public_key = private_key.public_key()

# curr_time = datetime.now(timezone.utc).strftime('%Y%m%d%H%M')
api_link = f'https://api.cloudflareclient.com/v0i2503030000/reg'

headers = {
    'user-agent' : '',
    'content-type' : 'application/json'
}

d = {
    'install_id' : '',
    'tos' : datetime.now().isoformat()[:-7] + '.000Z',
    'key': str(public_key),
    'fcm_token' : '',
    'type' : 'android',
    'locale' : 'en_US'
}

print(json.dumps(d).replace(' ', ''))

r = requests.post(url=api_link, data=json.dumps(d).replace(' ', ''), headers=headers)

print(r.content)
