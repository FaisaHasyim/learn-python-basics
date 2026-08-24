# Program 5: Multiple Functions
# Demonstrasi: memanggil function berkali-kali dengan input berbeda

def hitung_kuadrat(angka):
    """Function untuk menghitung kuadrat"""
    return angka * angka

def hitung_pangkat_tiga(angka):
    """Function untuk menghitung pangkat 3"""
    return angka * angka * angka

def tampilkan_hasil(angka, kuadrat, pangkat_tiga):
    """Function untuk menampilkan hasil perhitungan"""
    print(f"\nAngka: {angka}")
    print(f"Kuadrat: {kuadrat}")
    print(f"Pangkat 3: {pangkat_tiga}")
    print("-" * 40)

# Main program
print("=" * 40)
print("PROGRAM HITUNG KUADRAT DAN PANGKAT 3")
print("=" * 40)

# Test dengan 3 angka berbeda
for angka in [14, 17, 10]:
    kuadrat = hitung_kuadrat(angka)
    pangkat_tiga = hitung_pangkat_tiga(angka)
    tampilkan_hasil(angka, kuadrat, pangkat_tiga)
