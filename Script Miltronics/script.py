import os
import shutil
import filecmp

src = "Miltronics"
dest = "MV"

bucle = True

while(bucle):
    srclist = os.listdir(src)
    number_file_src = len(srclist)

    destlist = os.listdir(dest)
    number_file_dest = len(destlist)
    
    if number_file_dest != number_file_src:
        
        dc = filecmp.dircmp(src,dest,ignore=['common_file'])
        
        if number_file_src > number_file_dest:
            #Este for nos elimina los archivos que solo están en la carpeta de origen.
            for item in dc.left_only:
                path = src + "/" + item
                os.remove(path)
                print(f"Archivo {item} eliminado.")
                
        elif number_file_dest > number_file_src:
            #Funcion que copia los archivos de la carpeta origen a la destino. 
            shutil.copytree(dest, src, dirs_exist_ok=True)
    #Probar a eliminar el tema de nuevo archivo de texto con dc.left_list
                      

print("Unexpected exit.")        
        



    
#Este for nos elimina los archivos que solo están en la carpeta de destino. 
#for item in dc.right_only:
#    path = src + "/" + item
#    os.remove(path)
#    print("Archivo {item} eliminado.")




