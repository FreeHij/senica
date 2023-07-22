import urllib.request
import socket
import os

version = 1

#htmls
try: os.mkdir("www") 
except FileExistsError: pass
urllib.request.urlretrieve("http://185.87.192.150/", "www/index.html")
urllib.request.urlretrieve("http://185.87.192.150/favicon.ico", "www/favicon.ico")

#error codes
try: os.mkdir("codes") 
except FileExistsError: pass
urllib.request.urlretrieve("http://185.87.192.150/404_.html", "codes/404.html")
urllib.request.urlretrieve("http://185.87.192.150/favicon.ico", "codes/favicon.ico")

#plugins
try: os.mkdir("plugins") 
except Exception: pass

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 80))
    while True:
        server.listen(20)
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode("utf-8")
        client_socket.send(resp(data))
        client_socket.shutdown(socket.SHUT_WR)

def resp(request_data):
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf8\r\n\r\n"
    path = request_data.split()[1]
    response = ""
    try:
        with open("www" + path, "rb") as file:
            response = file.read()
    except Exception:
        with open("codes" + "/404.html", "rb") as file:
            response = file.read()
    return HDRS.encode("utf-8") + response

start()