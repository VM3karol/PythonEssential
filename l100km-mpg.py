# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:36:32 2022

@author: USUARIO
"""
milla=1609.344
galon=3.785411784

def l100kmtompg(liters):
    mpg=(100*galon)/((milla/1000)*liters);
    return mpg
#

def mpgtol100km(miles):
    l100km=(100*galon)/((milla/1000)*miles);
    return l100km
#

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
