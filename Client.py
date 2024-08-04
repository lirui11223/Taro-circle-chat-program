import socket
import time

HOST = '127.0.0.1'  # 服务器地址
PORT = 65432        # 服务器端口

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input('Enter message(请输入信息): ')
        if msg == 'exit':
            break
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)

        print('Received(消息)', repr(data.decode('utf-8')))
print('Welcome to the chat program again(欢迎再次使用聊天程序)')
time.sleep(10)
