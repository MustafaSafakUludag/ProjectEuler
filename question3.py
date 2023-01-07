"""
3.soru :13195'in asal çarpanları 5, 7, 13 ve 29'dur.

600851475143 sayısının en büyük asal çarpanı nedir?
"""
#1.Çözüm

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return  True
def maxprimefactor(n):
    for i in range(int(n**0.5),1,-1):
        if isprime(i) and n%i==0:
            return i
    return n
print(maxprimefactor(600851475143))


#2.Çözüm

def find_largest_prime_factor(n):
    i = 2
    while i < n:
        if not n % i:
            n //= i
        else:
            i += 1

    return i
print(find_largest_prime_factor(600851475143))


#3.Çözüm


sayi = 600851475143
for i in range(2, sayi):
    if (sayi % i == 0):
        bolundu = False
        for j in range(2, i):
            if i % j == 0:
                bolundu = True

        if bolundu == False:
            print("ASAL : " + str(i))




