#!/usr/bin/python
import socket
import json
import atexit




class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        res = self.sock.recv(1024)
        print(res.decode('utf-8'))

    def do_cmd(self, obj):
        self.sock.sendall((json.dumps(obj)).encode("utf8"))
        res = self.sock.recv(1024)
        if res:
            res = json.loads(res)
            return res
        else:
            pass


    def __del__(self):
        self.sock.sendall((json.dumps(['!disconnect']).encode("utf8")))


cli = Client(socket.gethostbyname(socket.gethostname()), 5555)
atexit.register(cli.__del__)
