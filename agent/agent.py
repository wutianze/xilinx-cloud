'''
@Author: Sauron Wu
@GitHub: wutianze
@Email: 1369130123qq@gmail.com
@Date: 2020-02-03 10:42:36
@LastEditors  : Sauron Wu
@LastEditTime : 2020-02-05 22:05:01
@Description: 
'''
import requests
import json
import os
from multiprocessing import Pool

DEBUG = False
SERVER_IP = '127.0.0.1'
SERVER_PORT = '8888'

with open(os.path.abspath('config.json'), encoding='utf-8') as f:
    config = json.load(f)
if DEBUG == True:
    print(config['xshdcg01'])

#-------------------------------

def _printStatus(info):
    print("Status:\n    hostname: "+info["hostname"]+"\n    all ip: "+", ".join(info["ips"]))

def _printCapability(info):
    print("Capability:\n    %d logic cpu, %d physic cpu, cpu usage: %.2f%%\n    total memory: %.2f G, memory usage: %d%%\n    total disk capacity: %.2f G, disk usage: %d%%"%(info["cpu"]["logic"],info["cpu"]["physic"],info["cpu"]["usage"],info["memory"]["total"],info["memory"]["used_percent"],info["disk"]["total"],info["disk"]["used_percent"]))
#--------------------------------
def list_func(url,ps,name):
    res = {}
    try:
        res = json.loads(requests.get(url,params=ps,timeout=5).text)
    except:
        res["info"] = "Warn: Server Connect Timeout"
    res["name"] = name
    return res
#--------------------------------

while True:
    command = input(">> ").split()

    if command[0] == 'quit':
        break
    elif command[0] == 'list':
        responses = {}
        if command[1] == "all":
            p = Pool(4)
            objs = []
            for key in config:
                obj = p.apply_async(list_func,args=('http://'+config[key]["idracIp"]+':'+SERVER_PORT+'/list',{"type":command[2:]},key))
                objs.append(obj)
            p.close()
            p.join()
            for o in objs:
                tmp = o.get()
                responses[tmp["name"]] = tmp
        elif command[1] not in config.keys():
            print("Error: the server "+command[1]+" not exist in config")
        else:
            tmp = list_func('http://'+config[command[1]]["idracIp"]+':'+SERVER_PORT+'/list',{"type":command[2:]},command[1])
            responses[tmp["name"]] = tmp
        if len(responses) == 0:
            print("Help: list xxx/all status/capability")
        for piece in responses.keys():
            info = responses[piece]
            print("----------server %s----------"%(info["name"]))
            if DEBUG:
                print(info)
            if info["info"] != "success":
                print(info["info"])
                print("-----------------------------------")
                continue
            if "status" in command:
                _printStatus(info)
            if "capability" in command:
                _printCapability(info)
            print("-----------------------------------")
        
            

