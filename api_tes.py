# encoding:utf-8
import requests

# client_id is the AK from Baidu Ai Studio， client_secret is the SK from Baidu Ai Studio
AK = ''
SK = ''
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+AK+'&client_secret='+SK
response = requests.get(host)
if response:
    print(response.json())
