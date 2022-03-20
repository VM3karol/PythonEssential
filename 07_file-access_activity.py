# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:52:58 2022

@author: USUARIO
"""

file=open("C:/Users/USUARIO/.spyder-py3/devices.txt","a")
while True:
    newItem = input("Ingresar un nuevo dispositivo: ")
    if newItem != 'exit':
        file.write(newItem + "\n")
    else:
        print("All done!")
        file.close()
        break

