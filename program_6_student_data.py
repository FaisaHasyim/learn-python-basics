# Program 6: Kelola Data Siswa dengan List dan Dictionary

def tambah_siswa(daftar_siswa):
    """Function untuk tambah data siswa baru"""
    nama = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai: "))
    
    siswa = {
        "nama": nama,
        "nilai": nilai
    }
    daftar_siswa.append(siswa)
    print(f"✓ {nama} ditambahkan!\n")

def tampilkan_semua_siswa(daftar_siswa):
    """Function untuk tampilkan semua data siswa"""
    print("\n" + "=" * 50)
    print("DAFTAR SISWA")
    print("=" * 50)
    
    if len(daftar_siswa) == 0:
        print("Tidak ada data siswa.\n")
        return
    
    for i, siswa in enumerate(daftar_siswa, 1):
        print(f"{i}. {siswa['nama']} - Nilai: {siswa['nilai']}")
    print("=" * 50 + "\n")

def hitung_rata_rata(daftar_siswa):
    """Function untuk hitung rata-rata nilai"""
    if len(daftar_siswa) == 0:
        print("Tidak ada data siswa.\n")
        return
    
    total_nilai = sum(siswa['nilai'] for siswa in daftar_siswa)
    rata_rata = total_nilai / len(daftar_siswa)
    
    print(f"\nRata-rata nilai: {rata_rata:.2f}\n")

def menu_utama():
    """Function untuk tampilkan menu dan kelola siswa"""
    daftar_siswa = []
    
    while True:
        print("=" * 50)
        print("SISTEM MANAJEMEN DATA SISWA")
        print("=" * 50)
        print("1. Tambah Siswa")
        print("2. Tampilkan Semua Siswa")
        print("3. Hitung Rata-rata Nilai")
        print("4. Keluar")
        print("=" * 50)
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_siswa(daftar_siswa)
        elif pilihan == "2":
            tampilkan_semua_siswa(daftar_siswa)
        elif pilihan == "3":
            hitung_rata_rata(daftar_siswa)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.\n")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

# Main program
menu_utama()