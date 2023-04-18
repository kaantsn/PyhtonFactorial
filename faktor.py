def faktoriyel(n):
    faktoriyel = 1
    for i in range(1, n+1):
        faktoriyel *= i
    return faktoriyel

# örnek kullanım
print(faktoriyel(5)) # çıktı: 120
