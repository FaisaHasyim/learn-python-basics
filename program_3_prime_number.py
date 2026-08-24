# Program 3: Cek Bilangan Prima
# Input: angka dari user
# Output: apakah bilangan itu prima atau tidak

angka = int(input("Masukkan angka: "))

prima = True

if angka < 2:
    prima = False
else:
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

if prima:
    print(f"{angka} adalah bilangan PRIMA\n")
else:
    print(f"{angka} BUKAN bilangan prima\n")
    