'''
@Author: Sauron Wu
@GitHub: wutianze
@Email: 1369130123qq@gmail.com
@Date: 2020-02-05 14:51:10
@LastEditors  : Sauron Wu
@LastEditTime : 2020-02-05 20:02:54
@Description: 
'''
import subprocess
import psutil

def server_status():
    ips = []
    s1, o1 = subprocess.getstatusoutput("hostname")
    s2, o2 = subprocess.getstatusoutput("ifconfig |grep inet\ ")
    for line in o2.split('\n'):
        ips.append(line.split()[1])
    if s1 != 0:
        print("get hostname error")
        return {"info":"Get Hostname Error"}
    if s2 != 0:
        print("get ip error")
        return {"info":"Get IP Error"}
    return {"info":"success","hostname":o1,"ips":ips}

def server_capability():
    # cpu
    cpu_count_logic = psutil.cpu_count()
    cpu_count_physic = psutil.cpu_count(logical=False)
    cpu_percent = psutil.cpu_percent()

    # memory
    memory_info = psutil.virtual_memory()

    # disk
    disk_usage = psutil.disk_usage('/')

    return {"info":"success","cpu":{"logic":cpu_count_logic,"physic":cpu_count_physic,"usage":cpu_percent},"memory":{"total":memory_info.total/1073741824.0,"used_percent":memory_info.percent},"disk":{"total":disk_usage.total/1073741824.0,"used_percent":disk_usage.percent}}


if __name__ == '__main__':
    print(server_status())
    print(server_capability())