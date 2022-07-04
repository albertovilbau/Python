#Script creado por:
#Alberto Villar Bautista

from concurrent.futures import thread
from time import sleep
from typing import List
from wakeonlan import send_magic_packet
from ping3 import ping
import os

class pc:
    def __init__(self, ip, mac):  
        self.ip = ip  
        self.mac = mac 

ordenadores = [];

archivo = open(r"C:\Users\Administrator\Desktop\Script Fusion\aula3.txt");
lineas = archivo.readlines();
archivo.close();

for i in lineas:
    info = i.split(';');
	info[1] = info[1].strip('\n');
    ordenadores.append(pc(info[0], info[1]));

#codigo para ver si coge bien el archivo
for pc in ordenadores:
    print(pc.ip + " - Paquete enviado.");
    send_magic_packet(pc.mac);

rsp = False

sleep(120)

ping(ordenadores[0].ip)

if ping:
  print("PCs Encendidos"); 

hostnames = [];
for pc in ordenadores:
    if pc.ip == "10.20.3.1":
        hostnames.append("A310")
    else:
        hostnames.append("A3" + pc.ip[-2:])

print(hostnames)

for pc in hostnames:
    os.system('winrs -r:' + pc + r' -u:user -p:password choco upgrade autodesk-fusion360 --ignore-checksums -y --Force')
  
for pc in hostnames:
    os.system('winrs -r:' + pc + r' -u:user -p:password shutdown -s')