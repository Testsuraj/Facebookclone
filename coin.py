import base64
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

# Function to encode event data
def encode_event(e, t):
    r = f"{e}|{t}|{int(time.time())}"
    n = "tttttttttttttttttttttttttttttttt"
    i = n[:16]
    key = n.encode('utf-8') 
    iv = i.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(r.encode('utf-8'), AES.block_size))
    return base64.b64encode(base64.b64encode(encrypted)).decode('utf-8')


# Replace 'query_id' in headers with user input
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'lan': 'en',
    'origin': 'https://bbqapp.bbqcoin.ai',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://bbqapp.bbqcoin.ai/',
    'sec-ch-ua': '"Android WebView";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'use-agen': 
    'query_id=AAH_f45XAwAAAP9_jlcBScMS&user=%7B%22id%22%3A7911407615%2C%22first_name%22%3A%22Shafquat%22%2C%22last_name%22%3A%22Ujan%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1730446590&hash=421c7ea2329c54c59be6f08a971e26ede940c787cb46bc5483b7e316e7b88130',
    'user-agent': 'add your custom header here',
    'x-requested-with': 'org.telegram.messenger',
}
# Collect user input

user_id = input("Enter your Telegram User ID: ")
taps = input("Enter the amount of coin taps: ")


# Function to perform the coin tap action
def bbq_tap():
    data = {
        'id_user': user_id,
        'mm': taps,
        'game': encode_event(user_id, taps),
    }
    response = requests.post('https://bbqbackcs.bbqcoin.ai/api/coin/earnmoney', headers=headers, data=data)
    print(response.text)  # Print the server's response

# Call the function
bbq_tap()