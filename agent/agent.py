'''
@Author: Sauron Wu
@GitHub: wutianze
@Email: 1369130123qq@gmail.com
@Date: 2020-02-03 10:42:36
@LastEditors  : Sauron Wu
@LastEditTime : 2020-02-05 14:45:41
@Description: 
'''
import requests
import json
import os

DEBUG = True
SERVER_IP = '127.0.0.1'
SERVER_PORT = '8888'

with open(os.path.abspath('config.json'), encoding='utf-8') as f:
    config = json.load(f)
if DEBUG == True:
    print(config['xshdcg01'])

while True:
    command = input(">> ").split()

    if command[0] == 'q':
        break
    elif command[0] == 's':
        response = requests.get('http://'+SERVER_IP+':'+SERVER_PORT, params={"a":[1,2,3], "b":2})
        print(response.text)
#response = requests.get('http://127.0.0.1:8888/')
#print(response.text)
