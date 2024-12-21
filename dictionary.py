# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:06:52 2024

@author: User
"""

#Dictionary(Lugat)
#lugatni qolgan malumot turlaridan farqi lugatda malumotlarni saqlash uchun kalit suz va qiymatdan foydlanamiza
#key value pair -- kalit suz qiymat juftligi
# car_0 = {'model':'ferrari','rang':'qizil'}
# # print(car_0['model'])
# # print(car_0['rang'])

# mevalar ={'olma':10000,'banan':20000,'qovun':30000}
# print(f"olma narxi {mevalar['olma']}")

#Bush lugat yaratish  lugatdan element uchirish va qushish
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['yosh'] = 23
# talaba_1['kurs'] = 3
# del talaba_1['kurs']
# print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

#lugatlarni bir necha qatorda yozish
# talabalar = {
#     'ali':'iphone x',
#     'olim':'galaxy s9',
#     'orif':'nokia'
#     }
# print(talabalar)

#lugatda yuq narsalarni chaqirganda xato bermasligi javob berishi uchun
#get() metodidan foydalanamiza
# phone = talabalar.get('hasan','bunday odam mavjud emas')
# print(phone)


#Amaliyot
# otam = {'ism':'mavlutdin','yil':'1954','joy':'samaraqand'}
# onam = {'ism':'xadicha','yil':'1964','joy':'qarshi'}
# ukam = {'ism':'olim','yil':'1994','joy':'toshkent'}
# print(f"Otamning ismi {otam['ism'].title()} u {otam['yil']}-yilda {otam['joy'].title()} shaxrida tugilgan")

taomlar = {
    'ali':'osh',
    'orif':'manti',
    'olim':'lagman',
    'akmal':'shashlik',
    'shuxrat':'somsa'
    }
taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")















