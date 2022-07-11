#Script creado por:
#Alberto Villar Bautista

from concurrent.futures import thread
from time import sleep
from typing import List
from wakeonlan import send_magic_packet
from ping3 import ping
import os
import subprocess
import datetime

class pc:
    def __init__(self, ip, mac):  
        self.ip = ip  
        self.mac = mac 

class pcversions:
    def __init__(self, hostname, v1,v2):  
        self.hostname = hostname  
        self.v1 = v1 
        self.v2 = v2

ordenadores = [];
versiones =[];

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
        versiones.append(pcversions("A310","1","1"))
        
    else:
        hostnames.append("A3" + pc.ip[-2:])
        versiones.append(pcversions("A3" + pc.ip[-2:],"1","1"))

print(hostnames)

for pc in versiones:
    v1 = subprocess.check_output('winrs -r:'+ pc.hostname + r'-u:FUNDACIOCIM\Administrador -p:procan0 type C:\Program Files\Autodesk\webdeploy\production\5504d85ae982f0b7c130e43cd174ede20d73f523\fusion_version.txt')
    v1 = str(v1)
    v1 = v1[2:len(v1)-1]

    pc.v1 = v1



for pc in hostnames:
    print("Actualizando: " + pc)
    os.system('winrs -r:' + pc + r' -u:EDU\administrator -p:procana choco upgrade autodesk-fusion360 --ignore-checksums -y')

for pc in versiones:
    v2 = subprocess.check_output('winrs -r:' + pc.hostname + r'-u:FUNDACIOCIM\Administrador -p:procan0 type C:\Program Files\Autodesk\webdeploy\production\5504d85ae982f0b7c130e43cd174ede20d73f523\fusion_version.txt')
    v2 = str(v2)
    v2 = v2[2:len(v2)-1]

    pc.v2 = v2


today = datetime.datetime.now()

today = "%s/%s/%s : %s:%s" %(today.day, today.month, today.year, today.hour, today.minute)

logs = open(today + "-logs.txt","w+")

for pc in versiones:
    linea = pc.hostname + "Version antes de actualizar: " + pc.v1 + " | Version despues de actualizar: " + pc.v2
    logs.write(linea + "\n")
  
for pc in hostnames:
    os.system('winrs -r:' + pc + r' -u:EDU\administrator -p:procana shutdown -s')