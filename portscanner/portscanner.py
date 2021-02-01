import socket
from IPy import IP


# convert target name into ip address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


# Try connection
def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_address, port))
        print('[+] Port ' + str(port) + ' is open')
    except:
        print('[-] Port ' + str(port) + ' is closed')


# define port and ip_address
ip_address = input('[+] Enter Target to scan: ')
converted_ip = check_ip(ip_address)
# port = 80

for port in range(1, 100):
    scan_port(converted_ip, port)
