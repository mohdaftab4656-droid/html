import requests

headers = {
    'User-Agent': 'CCBot'
}

response = requests.get('https://ccbot.thundercipher.tech/', headers=headers)
print(response.text)
