# vulnerability scanner using portscanner module
import portscanner

targets_ip = input('[+] * Enter Target To scan For Vulnerable open Ports: ')
port_number = int(input('[+] * Enter Amount of ports you want to scan(500 - first 500 Ports): '))
vul_file = input('[+] * Enter path to file with vulnerable software: ')
print('\n')

target = portscanner.PortScan(targets_ip, port_number)

# Initiate portscan method
print('Scanning target.....')
target.scan()


# compare vul_file
with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + ' " ON PORT: ' + str(target.open_ports))
        count += 1
