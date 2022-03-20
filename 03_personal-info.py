# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:37:32 2022

@author: USUARIO
"""

print("Registro de usuario")
nombre=input("Ingrese su nombre: ")
#apellido=input("Ingrese su apellido: ")
#ubicacion=input("Ingrese su ubicación: ")
edad=int(input("Ingrese su edad:"))
space=" "

#print(nombre+space+apellido+space+"vive en"
 #     +space+ubicacion+space+"y su edad es de"+space+edad)

if edad>=1 and edad<=17:
    print(f"{nombre} es menor de edad.")
elif edad>=18 and edad<=26:
    print(f"{nombre} es joven")
elif edad>=27 and edad<=64:
    print(f"{nombre} es adulto")
elif edad>=65:
    print(f"{nombre} es adulto mayor")
else:
    print("Edad ingresada incorrecta")