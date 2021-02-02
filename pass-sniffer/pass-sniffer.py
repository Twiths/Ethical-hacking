from scapy.all import *
from urllib import parse
import re

iface = 'eth0'


def get_login_pass(body):
    user = None
    passwd = None

    userfields = []
    passfields = []

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()
    if user and passwd:
        return user, passwd


def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print()



try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print('Exiting....')
    exit(0)
