# Program 2: Penjumlahan Deret
# Input: N (angka terakhir deret)
# Output: jumlah dari 1 + 2 + 3 + ... + N

n = int(input("Masukkan N: "))

jumlah = 0
deret = []

for i in range(1, n + 1):
    jumlah = jumlah + i
    deret.append(i)

deret_string = " + ".join(map(str, deret))

print(f"\nDeret: {deret_string}")
print(f"Jumlah: {jumlah}\n")
