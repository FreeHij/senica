import urllib.request
import threading
import logging
import socket
import os

version = 1.0

#logging setup
format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format = format, level = logging.DEBUG, datefmt = "%H:%M:%S")

#htmls
try: os.mkdir("www")
except FileExistsError: pass
urllib.request.urlretrieve("http://185.87.192.150/", "www/index.html")
urllib.request.urlretrieve("http://185.87.192.150/favicon.ico", "www/favicon.ico")
logging.info("www done")

#error codes
try: os.mkdir("codes") 
except FileExistsError: pass
urllib.request.urlretrieve("http://185.87.192.150/404_.html", "codes/404.html")
urllib.request.urlretrieve("http://185.87.192.150/favicon.ico", "codes/favicon.ico")
logging.info("codes done")

#plugins
try: os.mkdir("plugins") 
except FileExistsError: pass
logging.info("plugins done")

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 80))
    while True:
        server.listen(4)
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode("utf-8")
        client_socket.send(resp(data))
        client_socket.shutdown(socket.SHUT_WR)

def resp(request_data):
    response = ""
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf8\r\n\r\n"
    try:
        if request_data.split()[1] == "/":
            with open("www" + "/index.html", "rb") as file:
                return HDRS.encode("utf-8") + file.read()
        else:
            try:
                with open("www" + request_data.split()[1], "rb") as file:
                    return HDRS.encode("utf-8") + file.read()
            except Exception:
                with open("codes" + "/404.html", "rb") as file:
                    return HDRS.encode("utf-8") + file.read()
    except Exception:
        return "Error"

Server = threading.Thread(target = start, daemon = True)
Server.start()
logging.info("server is running on :80")
while True:
    cmd = input("> ")
    match cmd:
        case "stop" | "exit":
            exit()
        case "version" | "ver":
            print(version)
        case _:
            print("unknown command")