# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:54:52 2024

@author: User
"""

#.items() metodi tarjimasi elementlar degan manoni beradi yani elementdagi hamma malumotlarni bizga kursatib beradi
# talaba_0 = {
#     'ism':'Shamsiddin',
#     'familya':'shamsiyev',
#     'yosh':23,
#     'fakultet':'matematika'
#     }
# #print(talaba_0.items())

# #bu yerda talaba.itemsdagi har bir kalit va qiymat uchun pastdagi komandani bajar
# for kalit, qiymat in talaba_0.items(): 
#     print(f"Kalit {kalit}")
#     print(f"Qiymat {qiymat} \n")
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

#Agar biz lugatdagi faqat kalitlarni bilmoqchi bulsak .keys metodidan foydalanamiza

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# # print("Do'kondagi mahsulotlar:")

# # for mahsulot in mahsulotlar:
# #     print(mahsulot.title())
# bozorlik = ['uzum','anor','yog','un']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()}{mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos dukoningizga {buyum} olib keling")

#Lugatlarni tartib bilan  chaqirish
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
    
# #Ruyhatdan faqat qiymatlari kerak bulganda biz .value metodidan foydalanamiza
# print(mahsulotlar.values())
# print(f"Foydalanuvchi quydagi telefon ishlatadi: ")
# for meva in mahsulotlar.values():
#     print(meva)


#.set metodi haqida set metodi bizga qayta qayta chiqadiga elemetnlarni bir marat chiqarishga yordam beradi
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
# print("Foydalanuvchilar shu telefonlardan: ")
# for user in set(telefonlar.values()):
#     print(user)

#biz SETS ning huddi lugat tuple list kabi ishlatishimiz mumkin lekin uning ichida bir hil narsa ikki marta takrorlanmaydi
# toys = {'ball','toys','car','lamp','ball'}
 

#Amaliyot
# python_lugat = {
#     'Boolean':'Mantiqiy qiymat',
#     'Float':"O'nlik son",
#     'For':'Biror amalni qayta bajarish sikli',
#     'If':'Shartni tugri yoki notugriligini tekshirish',
#     'Tuple':"O'zgarmas ruyhat",
#     'String':'Matn',
#     'Number':'Raqam'
#     }
# for key in sorted(python_lugat):
#     print(key)


# davlatlar = {
#     'uzb':'tashkent',
#     'rus':'moskva',
#     'usa':'Washinhton',
#     'uk':'london'
#     }
# davlat = input('Davlatni kiriting: ').lower()
# poytaxt = davlatlar.get(davlat,"Bu ruyhatda yuq")

# if davlat == None:
#     print("Bizda bunaqa malumot yuq")
# else:
#     print(f"Bu davlat poytaxti {poytaxt.title()}")

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }
# print('3 ta taom buyurtma qiling')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input (f"{n+1}-taom:").lower())
    
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()}{menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz {buyurtma} yo'q")
    


























































