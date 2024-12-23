# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:54:52 2024

@author: User
"""

#.items() metodi tarjimasi elementlar degan manoni beradi
talaba_0 = {
    'ism':'Shamsiddin',
    'familya':'shamsiyev',
    'yosh':23,
    'fakultet':'matematika'
    }
#print(talaba_0.items())

#bu yerda talaba.itemsdagi har bir kalit va qiymat uchun pastdagi komandani bajar
for kalit, qiymat in talaba_0.items(): 
    print(f"Kalit {kalit}")
    print(f"Qiymat {qiymat} \n")
    