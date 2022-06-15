#Script creado por:
#Alberto Villar Bautista

from typing import List
from wakeonlan import send_magic_packet

class pc:
    def __init__(self, ip, mac):  
        self.ip = ip  
        self.mac = mac 

ordenadores = [];

archivo = open("C:/Users/avillar/Desktop/Python pruebas/Wake on Lan/aula5.txt");
lineas = archivo.readlines();
archivo.close();

for i in lineas:
    info = i.split(';');
    ordenadores.append(pc(info[0], info[1]));

#codigo para ver si coge bien el archivo
for pc in ordenadores:
    print(pc.ip + " - Encendido.");
    send_magic_packet(pc.mac);