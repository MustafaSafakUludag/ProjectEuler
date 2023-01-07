"""
1.soru:10'un altındaki 3 veya 5'in katı olan tüm doğal sayıları sıralarsak 3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.
1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.
"""
#1.Çözüm

toplam=0

for i in range(1000):
    if i%3==0 or i%5==0:
        toplam+=i
print(f"1000'in altındaki 3 veya 5'in tüm katlarının toplamı:{toplam}")



#2.Çözüm
def math_(a):
    if a%3==0 or a%5==0:
        return True
    else:
        return False
toplam=0
list=[]
for i in range(1000):
    if math_(i)== True:
        toplam+=i
        list.append(i)
print(list)
print(toplam)



#3.Çözüm

list=[]
toplam=0
for i in range(1000):
    if i%3==0 or i%5==0:
        list.append(i)
for a in list:
    toplam+=a
print(toplam)


