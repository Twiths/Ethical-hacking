import socket
from IPy import IP
from termcolor import colored

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[- 0 scanning Target]: ' + str(target))
    for port in range(1, 100):
        scan_port(converted_ip, port)

    
#convert target name into ip address
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

#Try connection
def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip_address, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

if __name__ == '__main__':
#define port and ip_address
    targets = input('[+] Enter Target/s to scan(Split multiple targets with a comma ,): ')
    # port_num = input('[+] Enter the number of ports you want to scan: ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)


