#Script creado por:
#Alberto Villar Bautista

from typing import List
import os

class topid:
    def __init__(self, pc, id):  
        self.pc = pc  
        self.id = id 

ids = [];

archivo = open(r"C:\Users\avillar\Desktop\Python pruebas\TopID\id.txt");
lineas = archivo.readlines();
archivo.close();

for i in lineas:
    info = i.split(';');
    info[1] = info[1].strip('\n');
    ids.append(topid(info[0], info[1]));

archivos = os.listdir(r"C:\Users\avillar\Desktop\Python pruebas\TopID\archivos");

rutaids = r"C:\Users\avillar\Desktop\Python pruebas\TopID\archivos\\";

for arx in archivos:
    #print("PC: " + id.pc + " - " + id.id);
    for id in ids:
        if id.id in arx:
            os.rename(rutaids + arx, rutaids + id.pc + ".TopLic");
            print(id.pc)

