import socket
target_ip = "127.0.0.1"
target_port = 8765
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
result = sock.connect_ex((target_ip, target_port))
if result == 0:
    print(f"Port {target_port} is open")
else:
    print(f"Port {target_port} is closed")
sock.close()