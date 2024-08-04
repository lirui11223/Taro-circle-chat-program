import socket

HOST = '127.0.0.1'  # 服务器地址
PORT = 65432        # 服务器端口

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()  # 等待客户端连接
    with conn:
        print('连接', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print('消息', repr(data))
            conn.sendall(data.encode() + b'\n')  # 发送回客户端
