# Problem 2: Cari Bilangan Terbesar dari 3 Bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

if a >= b and a >= c:
    terbesar = a
elif b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

print(f"Bilangan terbesar dari {a}, {b}, {c} adalah {terbesar}")
