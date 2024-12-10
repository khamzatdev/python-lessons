# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 02:52:36 2024

@author: User
"""
#03-DARS
#print() funksiysi
#22.10.2024


#print('Odami ersang demagil odami,\nOniki yo\'q xa xalq g\'amidin g\'ami')
#Uch tirnoq quyib yoziladigan bulsa unda matnni pastga tushirish uchun \n belgisi shart emas

#Arifmetik amalar

#print(2+4*2)
#print(15/9)
#print(15/5)
#print(15//5)

#Bulishda agar bitta bulish belgisidan foydalansa o'nlik  kurinishda chiqadi agar ikkita bulish  belgi bulsa unda butun xolatda chiqaradi
#Ammo bulishda qoldiq qoladigan bulsa ikkita belgi foydalanilgan xolatda kursatilmaydi faqat butun son kursatiladi

#print(2**4)
#Ikkita kupaytiruv belgisi usha sonning darajasini chiqaradi 2ning 4chi darajasi

#print('3x3=',3*3)
#bu xolatda string xolatda yozilganlar string bulib number xolatda yozilganlar number xolatda chiqadi

#Amaliyot
#print('"Nexia","Tico",\'Damas\' ko\'rganlar havas qiladi')
#print(5**4)
#print(22%4)
#print(125*125)
#print(125*4)
#print(((12/2)**2)*3.14)
#print(3.14*(12/2)**2)
#-----------------------------------------------------------------------------------------------


#04dars O'zgaruvchilar
#23.10.2024


#ism = 'Abdulloh'
#yosh = 26
#print(ism)
#print(yosh)

#Amaliyot

#matn = 'Hello World'
#print(matn)

#xabar = "Assalamu Alaykum"
#print(xabar) 

#radius = 5
#pi = 3.14
#aylana_yuzi = pi * radius ** 2
#print("Radius" , radius, "ga teng aylananing yuzi=",aylana_yuzi)

#---------------------------------------------------------------------------
#06-dars matn bilan ishlash strings
#29.10.2024

# ism = 'Anvar'

# matn = 'Men yangi 🤑'

# #Stirng ustida amallar 

# ism = 'Ahmad'
# print('Mening ismim '+ism)

# ism = 'Ahad'
# familya = 'Qayum'
# print(ism + ' ' + familya) 

# #f-string

# ism = 'Ahad'
# familya = 'Qayum'
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif)

# #Maxsus belgilar
# print("Hello World")
# print("Hello \nWorld") # qatorni keyingisiga tusurish 
# print("Hello \tWorld") # orasida kuproq joy qoldirish

# #String metodlari
# ism = 'James'
# familya = 'Bond'
# ism_sharif = f"{ism} {familya}"
# ism_sharif = ism_sharif.upper()
# print(ism_sharif.title()) #har bir suzni bosh xarifini katta qiladi
# # upper() bulsa hammasini katta qiladi lower() hammasini kichik qiladi
# #capitaliza() bunda faqat birinchi suzdagi harfni katta qilib beradi

# meva = "    olma    "
# print(meva)
# print("Men " + meva.lstrip()+ "yaxshi kuraman") #lstrip chapdagi bushliqni
# #rstrip o'ng tarafdagi bushliqni olib tashlaydi stripni uzi esa hamma bushliqni olib tashlaydi

#INPUT

# ism = input("Ismingiz kim?")
# print("Assalamu alaykum, " + ism)

# ism = input("Ismingiz kim?\n>>>") #Foydalanuvchining ismi yangi qatordan chiqishi
# print("Assalamu Alaykum, " + ism.title())

#Amaliyot
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# viloyat = "Samarqand"
# tuman = "Bodomzor"
# # print(kocha + " ko'chasi," +mahalla +" mahallasi," + tuman + " tumani," + viloyat + " viloyati")
# print("Iltimos quyidagi malumotlarni kirgizing ")
# kocha = input("Kuchangiz: ")
# mahalla = input("Mahallangiz: ")
# tuman = input("Tumaningiz: ")
# viloyat = input("Viloyatingiz ") 
# manzil = f"{kocha} ko'chasi {mahalla} mahallasi {tuman} tumani {viloyat} viloyati"
# # print(kocha + " ko'chasi,\n" +mahalla +" mahallasi,\n" + tuman + " tumani,\n" + viloyat + " viloyati\n")
# print(manzil.capitalize())

#--------------------------------------------------------------------------
#07-dars sonlar bilan ishlash
# a = 20
# b = 5.5
# print(type(a)) #o'zgaruvchini turini aniqlash

# aholi_soni = 7_594_376_222 #kup xonali sonlar yozishda qulay uslub
# print("Aholi soni: " , aholi_soni)

# x,y,z = 10,5,-67, 

#float sonni intga qushsak yoki kuoaytirasak son float songa aylanadi masalan
# a = 5.5
# b = 40 
# c = a * b
# print(c)

#har qanaqa sonni bulish amalini bajarsak bu son bizga float qaytaradi ammo bulish belgisini // 2 marta quyish orqali int son qaytarishimiza mumkin

# a = 100
# b =  4
# c = a / b
# d = a // b
# print(c,d)

# pythonda constanta tushunchasi yuq bulib dasturchilar orasida katta xarflar bilan yozilgan uzgarusvchilar const deb ataladi
# radius = 20
# PI = 3.14159
# diametr = radius * 2
# print("Aylananing uzunligi = ",diametr * PI)

# o'zgaruvchini int xolatidan str xolatiga utkazish 
# ism = 'Jobir'
# yosh = 36  #strni 
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

#input har qanday sonni string holatda qaytaradi
# t_yil = int(input("Tugilgan yilizni kirgizing: "))
# yosh = 2024-t_yil
# print("Siz", yosh, "yosh ekansiz")

# a = int("10")
# b = float("15")
# temp = str(36.6)

# son_kvadrati = int(input("Sonni kirgizing: "))
# kv = son_kvadrati ** 2
# kub = son_kvadrati ** 3
# print(son_kvadrati,"ning kvadrati",kv,"ga teng")
# print(son_kvadrati,"ning kubi",kub,"ga teng")

# tugulgan_yil = int(input("Yoshingizni kirgizing: "))
# yil = 2024 - tugulgan_yil
# print("Siz", yil,"da tugilgansiz")

# a = float(input("Birinchi son: "))
# b = float(input("Ikkinchi son: "))
# c = (a+b, a-b, a*b, a/b)
# print(c)

#-----------------------------------------------------------------------------
# 08-dars listlar bilan ishlash

# mevalar = ['olma','gilos','anor'] #harflardan tashkil topgan list
# sonlar = ['bir','ikki','uch', 2,4,6] #harflar va sonlardan tashkil topgan list
# ismlar = [] #bo'sh list ham yaratish mumkin pythonda
# #print(mevalar[0]) #musbat sonlar bilan bulsa boshidan sanoq buladi manfiy son bulsa oxiridan hisoblanadi

# #append metodi orqali biz listga yangi malumot qushishimiza mumkin 
# #append metodi har doim ruyhatni oxiriga malumot qushadi
# mevalar.append('urik')

# #agar biz xoxxlagan joydan malumot qushishimiza uchun esa INSERT metodidan foydalanamiza
# mevalar.insert(0, 'banan')

#cars = []


# cars.append('Nissan')

# cars.append('Honda')

# cars.append('Porsche')

# cars.append('Ferrari')

# print(cars)
# ['Nissan', 'Honda', 'Porsche', 'Ferrari']

# del cars[3]

# cars.insert(3,'Ferrari')

# print(cars)
# ['Nissan', 'Honda', 'Porsche', 'Ferrari']

#index raqam bilan emas malumotni ismi bilan uchurish uchun uchun biz REMOVE metodidan foydalanamiza
#agar bizni ruyhatimiza bir nechta bir xil elementlar bulsa remove uni bittasini uchirib tashlaydi

# cars.append('Nissan')

# cars.append('Hummer')

# cars.append('Ferrari')

# cars.append('Toyoto')

# cars.remove('Toyoto')

# cars.remove('Nissan')


#ruyhatdan bir elementni sugirib olish POP() metodidan foydalaniladi
#biz pop metodiga hech qanaqa index bermasak u ruyhat oxiridagi metodni oladi

# bozorlik = ['yog','un','piyoz','kartoshka']
# mahsulot = bozorlik.pop(2)
# print('Men ',mahsulot,'oldim')
# print(bozorlik, 'lar qoldi')

# ismlar = ['Siroj','Davron','Behruz']
# print("Salom",ismlar[1],"bugun choyxona bormi?")
# print(ismlar[2],'bugun joyxona boramizmi')

# sonlar = [23,12,-45,15.6]
# arifmetika = sonlar[2] + sonlar[0]
# sonlar[0] = sonlar[0]+10
# del sonlar[3]

# t_shaxslar = ['Imom Buxoriy','Abu Bakr','Umar r.a']
# z_shaxslar = ['Shayx Muhammad Sodiq','Husanxon Buxoriy','Abror Muxtor Ali']
# print("Men tarixiy shaxslardan",t_shaxslar[2],"bilan,zamonaviy shaxslardan esa",z_shaxslar[0],"bilan kurishishni xox")

# friends = []
# friends.append('Siroj')
# friends.append('Davron')
# friends.append('ali')
# friends.append('Vali')
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(1))
# print("\nKelgan mehmonlar ruyhati",mehmonlar)

#Tartiblash birinchi alifbo buyicha taxlash
#sort() metodi orqali alifbo orqali tartiblash mumkin ammo ruyhatda katta harf bulsa katta harfni birinchi chiqaradi
# cars = ["bmw", "audi","zissan","toyoto","Zeekr"]
# #cars.sort()
# #print(cars)

#endi ruyhatni chappachasiga taxlash reverse=True metodi bilan sortning ichida joylashadi
#cars.sort(reverse=True)
#print(cars)

#asl ruyhatga tegmasdan ruyhatni tartibga keltirish)
#print(sorted(cars,reverse=True))
#agar reverse() metodidan foydalanadigan bulsak unda ruyhatni aylantirib quyadi
# sonlar = [7,2,4,5,-2,-8]
# sonlar.reverse()
# print(sonlar)

#ruyhatda qancha element borligini bilish uchun len() metodidan foydalaniladi
# uzunlik = len(sonlar)
# print(sonlar)

#range metodi bu shunaqa metod bulib u berilgan sonlarni uzi shakillantiradi masalan 0 dan 10gacha
# numbers = list(range(0,10))
# print(numbers)

#bu yerda biz qadamlarni ham hisoblashimiza mumkin masalan juft yoki toq sonlarni chiqarish
# numbers = list(range(0,101,10)) #buyerda 1dan 10gacha bulgan sonlarni 2 qadam tashlash bilan sanash 
# print(numbers)

# #max() metodi orqali eng katta raqamni topishimiz mumkin
# max_qiymat1 = max(numbers)
# max_qiymat = min(numbers)
# summa = sum(numbers)
# print(max_qiymat)
# print(max_qiymat1)
# print(summa)

#Ruyhatni kesish

#ruyhatdan malum bir elementlarni olish uchun masalan 1dan 3chigacha elemenmtlarni olish uchunquydagi metod amalga oshiriladi
#buning uchun biz 1chi va oxirgi elementni indeksini beramiza
#cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(cars[0:3])
# print(cars[:4])#bunaqa xolatda ruyhat boshidan to 4chigacha elementlarni chiqaradi
# print(cars[2:]) #bunaqa xolatda 2chidan boshqab ruyhat oxirigacha chiqadi
    
#Ruyhatdan nusxa olish

#my_cars = cars[:] #bu xolatda carsdagi elementlar boshidan oxirigacha my_cars ga kopiya bulib utadi

#Ruyhatlarni yangi turi TUPLES dasturlash vaqtida bizdan uzgarmas ruyhat talab qilinganida ushanda biz uzgarmas ruyhat tuzis uchun tuplesdan foydalanamiza
#tuples orqqali tuzilgan ruyhatdan hech nimani uchurish va qushish mumkin emas va undan kerakli bulgan elementlarni indeki orqali olishimiza mumkin
#tuples ruyhatga element qushish va uchirish uchun biz faqat bir yuldan foydalanishimiz mumkin tuplesni listga uzgartisrib
# toys = ('bus','car','bear','dino','snake','lizard')
# toys = list(toys)
# toys.append('Teddy')
# print(toys)
# toys = tuple(toys)

#AMALIYOT
# state = ['Uzb','Rus','USA','BAA','Ksa']
# state.sort()
# state.reverse()
# print(state)

# sonlar = list(range(120,1200))
# sonlar1 = min(sonlar)
# sonlar2 = max(sonlar)
# sonlar3 = sonlar2 - sonlar1
# print(len(sonlar))
# print(sonlar3)
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:551])

#taomlar = ['osh','somsa','manti','xonim','lagman']

# nonushta = taomlar[:]
# nonushta.remove('osh')
# nonushta.remove('xonim')
# nonushta = tuple(nonushta)
# nonushta = list(nonushta)
# nonushta[0] = "Qaymoq + Non"
# nonushta = tuple(nonushta)
# print(taomlar)
# print(nonushta)
#------------------------------------------------------------------------------
#09-dars FOR LOOP
#for sikli bizga bir kodni qayta qayta yozmasligimzi uchun yordam beradi

# mehmonlar = ['Ali','Vali','Hasan','Husan','Olim']
# for mehmon in mehmonlar:
#     print('Salom',mehmon) #printni bu tarafga surib yozilishi for siklini ichida bulganini bildiradi agar joy tashlamasdan yozsa sikldan chiqib qoladi va error berib qoladi
#     print("Hayr",mehmon) #ikkinchi printni ham davomidan joy tashlab qushishimiz ikkala siklni ham qaytaradi agar 2-print joy tashlamasdan yozsak ruyhatdan oxirgi elementni oladi
    
# mehmonlar = ['Ali','Vali','Hasan','Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurnatli {mehmon} sizni 20-dekabrda nahorga oshga taklif qilamiza")
#     print("Hurmat bilan Palonchiyevlar oilasi"\n)

# sonlar = list(range(1,11))
# for son in sonlar: #shu yerda ikki nuqta quyish kerak bulib quyilmasa hato buladi asosan spyderni uzi bu nuqtani quyadi
#     print(f"{son} ning kvadrati {son**2}ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# # print(sonlar_kvadrati)
    
# dostlar = []
# for n in range(5):
#     dostlar.append(input(f"{n+1}-eng yaqin dustingizni kiritish: ")) #n plus 1ning sababi suralganda 0 chi emas 1chi deb surashi uchun
# print(dostlar)

# #AMALIYOT
# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"Salom {ism}")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(10,100,1))
# sonlar2 = []
# for son in sonlar:
#     sonlar2.append(son**3)
# print(sonlar2)
     
# kino = []
# for k in range(5):
#     kino.append(input(f"{k+1} sevimli kinoyingizni kirgizing\n>>>>"))
# print(kino)

# people = int(input("Bugun nechi kishi bilan suhbat qildingiz: "))
# ismlar = []
# for n in range(people):
#     ismlar.append(input(f"{n+1} suhbat qilgan odamingiz kim edi?"))
# print(ismlar)
    


#-----------------------------------------------------------------------------
#10-dars Tarmoqlanish if else shartlari
# avtolar = ['bmw','toyota','kia','hyudai','mercedes']
# for avto in avtolar:
#     if avto == 'bmw': 
#         print(avto.upper())
#     else:
#         print(avto.title())
        
# == bu belgi tengmi degan manoni beradi
# != bu belsi esa teng emasmi degan manoni beradi

# ism = 'Ali'
# ism.lower() == 'ali'
# print(ism)
# ism = input("Ismingiz nima?\n>>>")
# if ism.lower() != 'ali':
#     print(f"Uzr {ism.title()} biz Alini kutayabmiz.")
# else:
#     print(f"Salom {ism}")

# javob = float(input("12x6 nechiga teng? >>>"))
# if javob != 72:
#     print('Javob xato')

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh >= 18:
#     print('Xush kelibsiz')
# else:
#     print('Kirish mumkin emas')

# login = input("Login kirgizing?>>>")
# if len(login) <=5:
#     print('Login 5 xarfdan kup bulishi shart')

# yil = int(input("Tugilgan yilingizni kirgizing!\n>>>"))
# if 2024-yil<18 :
#     print(f"Yoshingiz {2024-yil}da ekan")
#     print("Kirish mumkin emas")
# else:
#     print("Xush kelibsiz")

#if bilan printni yani badanini bir qatorda yozishimiz mumkin agarda kodingiz qisqa bolsa
# yosh = int(input("Yoshingizni kirgizing \n>>>"))
# if 65<yosh: print("Sizda COVID-19 risk guruhida ekansiz")

#if else va printni bir qatorda yozish mumkin misol:
# x,y = 25,50
# print("x>y") if x>y else print("x<y") #bu yerda ifning badani ifdan oldin elseniki esa elsedan keyin keladi 

#AMALIYOT
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())

# admin = input("Loginingizni kirgizing: ")
# if admin.lower() == 'admin':
#     print("Xush kelibsiz Admin foydalanuvchilar ruyhatini kurasizmi")
# else:
#     print(f"Xush kelibsiz {admin}")

# son1 = float(input("birinchi son: "))
# son2 = float(input("ikkinchi son: "))
# print("Teng") if son1 == son2 else print("Teng emas")
#-----------------------------------------------------------

#11-dars if elif else 
#biz if else orqali faqat bitta tekshiruv amalga oshiramiza 
#a biz kuplab tekshiruvlarni amalga oshirimiz uchun bizga elif yordam beradi
#if else kabi elif ham tekshiruv metodi bulib aks xolda degan manoni anglatadi

# yosh = int(input("Yoshingizni kirgizing: "))
# if yosh <= 4:  #bu yerda har bir qatorda printdan foydalanishimiza mumkin ammo bu kurinish bolee normalno
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so\'m")

#OR va AND operatorlari or ypoki and va degan manoni anglatani
# ish = input("Bugun qanaqa kun: ")
# if ish.lower()=="shanba" or ish.lower()=="yakshanba":
#     print("Bugun dam olish")
# else:
#     print("Bugun ish kuni")

#AND operatori va degan manoni beradi
# kun = input("Bugun kun nima>>> ")
# harorat = float(input("Havo harorati qanaqa: "))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Kettik chumilgani")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba')and harorat<=30:
#     print("Bugun dam olamiza")
# else:
#     print('Ish kuni')

# narx = 15000
# choy = True
# salat = False

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000
# print(f"Jami: {narx}") # bu if elifni kamchiligi bizga bitta tugri javob bersa birdan qaytaradi va keyingi surovlarga utnayi

#if orqali har bir qatorni tekshirish
# narx = 15000
# choy = 1
# non = 1
# salat = 1
# assorti = 0

# if choy:
#     narx = narx + 300
# if non:
#     narx = narx + 5000
# if salat:
#     narx = narx + 10000
# if assorti:
#     narx = narx + 20000
# print(f"Sizning hisobingiz {narx} so'm") #bu yerda har bir qatorni tekshirib chiqib keyin print ishlidi

#yana bir operator bu in in bilan biz usha joyda qanaqadir element bor yugligini tekshiratmiza 
# menu = ['manti','somsa','osh','xonim']
# ovqat = input("Nima ovaqt yeysiz: ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsus bu ovqat qolmagan") #in operatorining aksi ham bulib bu not in operatori bu bilan elementni ruyhatda yuqligini chiqaramiz

#ikkita ruyhatda bor yuqligini tekshirishimiza ham mumkin
# menu = ['manti','somsa','osh','xonim','lag\'mon']
# buyurtma = ['osh','xonim','tandir']
 
# if buyurtma:
#     for taom in buyurtma:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz menuda {taom} yuq")
# else:
#     print("savatchangiz bo'sh") # bu yerda if bilan ruyhat bush yoki yuqligini ham tekshirdik

#Amaliot
# son = int(input("Son kiriting: "))
# if son % 2:
#     print("Juft son kiriting")
# else:
#     print("Rahmat")

# yosh = int(input("Yoshingix nechada: "))
# if yosh <= 4 or yosh >=60:
#     print("Kerish tekin")
# elif yosh <= 18:
#     print("Kirish narxi 10000 sum")
# else:
#     print("Kirish narxi 20000 sum")

# x = float(input("Birinchi raqamni kirgizing: "))
# y = float(input("Ikkinchi raqamni kirgizing: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")



# mahsulotlar = ['anor','olma','nok','yog','guruch','nuxat','zigir','piyoz','kartoshka','pomidor']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotlarni qushing: "))
# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
# if mavjud_emas:
#     print(f"Dukonda bu mahsulotlar yuq")
#     for mahsulot in mavjud_emas:
#        print(mahsulot)
# else:
#     print("Siz suragan mahsulotlar dukonimizada bor")

# users = ['anvar','aki','romjke','zed','ned']
# login = input("Login kirgizing: ")

# if login in users:
#     print('Login band yangi login tanlang')
# else:
#     print(f"xush kelibsiz,{login.title()}!")
    

# son = int(input("Butun son kiriting: "))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n}ga qoldiqsiz bulinadi")
#---------------------------------------------------------------------------------------------
#12-dars Eng kup uchraydigan xatolar
# son = float(input("Juft son kiriting: "))
# if son%2 == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas.")

yosh = (input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    print







































































































































































