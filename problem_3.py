# Problem 3: Sistem Grade Berdasarkan Nilai
nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai: "))

if nilai >= 80:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

print(f"{nama} mendapatkan grade {grade}")
