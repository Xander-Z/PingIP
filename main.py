from MyPing import *

if __name__ == '__main__':
    # 读取IP
    with open('ip.txt','r') as f:
        ips = []
        for ip in f.readlines():
            ip = ip.strip('\n')
            if ip == '' or ip[0] in '#' :
                continue
            ips.append(ip.split(' ')[0])
    # 参数设置

    ping =MyPing()
    # Ping
    for ip in ips:
        ref = ping.send_ping(ip)
        if(ref == -1):
            print("{} 无法连通".format(ip))
        else:
            print("{} 已经连通, 抖动值: {}".format(ip, ref))
            break



