import os,shutil,filecmp,time

while(True):
    
    file = open("Y:\prueba.txt", "w")
    file.write("Esto es una prueba" + os.linesep)
    file.write("Esto es una prueba2")
    file.close()
    print("archivo creado")
    
    time.sleep(60)
    
    os.remove("Y:\prueba.txt")
    print("archivo eliminado")
    time.sleep(40)
    
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)