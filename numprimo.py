# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:38:14 2022

@author: USUARIO
"""

def isPrime(num):
#
    if num==2:
        return True
    else:
        for j in range(2,num):
            res=num%j
            if res==0:
                return False
        return True
#
print(isPrime(9))

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
