'''
Author: Ken Luo ken.luo.5227@gmail.com
Date: 2023-10-09 11:26:23
LastEditTime: 2023-10-09 11:26:41
LastEditors: Ken Luo ken.luo.5227@gmail.com
FilePath: /python/socket/clientTest.py
'''
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
 
s.connect((host, port))
print(s.recv(1024))
s.close()