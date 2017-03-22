import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个socket
# AF_INET指定使用IPv4协议  SOCK_STREAM 指定使用面向流的TCP协议

s.connect(('www.sina.com.cn',80)) #建立连接
# 要已知IP地址和端口号（端口号根据什么样的服务是固定的）

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') #发送数据

# 接收数据
buffer = [] #buffer缓冲
while True:
    d = s.recv(1024)# recv(max)方法 一次最多接收指定的字节数
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close() #关闭连接

header, html = data.split(b'\r\n\r\n',1) #把HTTP头和网页分离
print(header.decode('utf-8'))#打印头文件

with open('E:\sina.html','wb') as f:
    f.write(html)



#if __name__ == "__main__":
#    app.run(debug=True , host='0.0.0.0')

