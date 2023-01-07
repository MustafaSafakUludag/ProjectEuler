"""
2.soru :Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle oluşturulur.
1 ve 2 ile başlayarak ilk 10 terim şöyle olacaktır:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Değerleri dört milyonu geçmeyen Fibonacci dizisindeki terimleri dikkate alarak
çift değerli terimlerin toplamını bulunuz."""

#1.Çözüm

fib=list()
fib.append(1)
fib.append(2)
i=2
while True:
    if fib[i-1]+fib[i-2]<4000000:
        fib.append(fib[i-1]+fib[i-2])
        i+=1
    else:
        break
toplam=0
for i in fib:
    if i%2==0:
        toplam+=i
print(toplam)
print(fib)
print(len(fib))

#2.Çözüm

a=1
b=2
sum=2 # 2 olma sebebi çift sayı
while True:
    c=a+b
    a=b
    b=c
    if c%2==0:
        sum+=c
    if c>4000000:
        break
print(sum)


