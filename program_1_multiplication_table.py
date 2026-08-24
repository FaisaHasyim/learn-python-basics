# Program 1: Tabel Perkalian
# Input: angka dari user
# Output: tabel perkalian angka tersebut (1-10)

angka = int(input("Masukkan angka: "))

print(f"\nTabel perkalian {angka}:")
print("-" * 30)

for i in range(1, 11):
    hasil = angka * i
    print(f"{angka} x {i:2d} = {hasil:3d}")

print("-" * 30)