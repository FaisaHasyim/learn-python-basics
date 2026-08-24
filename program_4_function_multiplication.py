# Program 4: Tabel Perkalian dengan Function
# Demonstrasi penggunaan function untuk modularisasi code

def tabel_perkalian(angka):
    """Function untuk menampilkan tabel perkalian"""
    print(f"\nTabel perkalian {angka}:")
    print("-" * 30)
    
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i:2d} = {hasil:3d}")
    
    print("-" * 30)

# Main program
angka = int(input("Masukkan angka: "))
tabel_perkalian(angka)