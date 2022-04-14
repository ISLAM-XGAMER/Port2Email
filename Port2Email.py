import socket
import pyfiglet
import time
from EmailSender import *
from getpass import getpass
from colorama import Fore
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-q',
                    '--quite',
                    help="Quite mode (banner cancelled)",
                    action='store_true')

args = parser.parse_args()

#banner
if args.quite != True:
    print(Fore.RED + pyfiglet.figlet_format('Port2Email'))
    print("""programmed by : islam.h7""")

print(Fore.WHITE)

# s for sender , r for receiver , p for password
s = input("write your Sender Email  (the email you will send from) : ".title()
          ).replace(" ", "")
r = input(
    "write your receiver Email  (the email you will receive the email at) : ".
    title()).replace(" ", "")
p = getpass("write your Sender Email password : ".title()).replace(" ", "")

userinfo(s, r, p)

print("""Choose what type of scanning you would like to use:

1 - typed port 
2 - most common ports
3 - all ports
4 - help
5 - contact with me  
6 - Exit""".title())

answer = input('write here : '.title())

while answer == '' or answer not in ['1', '2', '3', '4', '5', '6']:
    print("Wrong input , please type again")
    answer = input('write here : '.title())


def all_ports():

    target = input('Type The IP : ')
    for port in range(1, 65536):

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            r = s.connect_ex((target, port))
            service = socket.getservbyport(port)
            if r == 0:
                print(
                    f'port {port} is open !!!!!!!! ,  and service is {service}'
                )
                send(port, target, "o")
            else:
                print(f'port {port} is closed !!!! and service is {service}')
                send(port, target, "c")
            s.close()
        except:
            pass


def typed_port():
    target = input('Type The IP : ')
    port = int(input('Type The Port : '))

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex((target, port))

        if r == 0:
            service = socket.getservbyport(port)
            print(f'{port} is open !!!!!!!! ,  and service is {service}')
            send(port, target, "o")
        else:
            service = socket.getservbyport(port)
            print(f'{port} is closed !!!! and service is {service}')
            s.close()
            send(port, target, "c")
    except:
        print('this port is not found in our system'.title())
        typed_port()


def most_common_ports():
    target = input('type the IP : ')
    ports = [21, 20, 19, 22, 23, 443, 80]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex((target, port))

        if r == 0:
            service = socket.getservbyport(port)
            print(f'{port} is open !!!!!!!! ,  and service is {service}')
            send(port, target, "o")

        else:
            service = socket.getservbyport(port)
            print(f'{port} is closed !!!! and service is {service}')
            send(port, target, "c")

            s.close()


if answer == '1':
    typed_port()

elif answer == '2':
    most_common_ports()

elif answer == '3':
    all_ports()

if answer == '4':
    print("""1 - Typed Port ======> a port chosen by the user 
2 -  Most Common Ports  ==========> checking most common ports  [21 , 20 , 19 , 22 ,23 , 443 , 80 ]
3 - All Ports =========> checking all 65,535 port , this going to take some time could be about 1 ~ 1.5 hour """
          .title())

if answer == '5':
    print(""" Gmail : islmhmdymhmed@gmail.com
    this is the only way you can contact with me :) 
    please read the ReadMe.txt file to know more about this program and ensure it is working correctly :)"""
          )

if answer == "6":
    sys.exit()