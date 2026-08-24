# Program 8: Binary Search Algorithm

def binary_search(data, target):
    """
    Binary Search - mencari elemen dalam data sorted
    Waktu: O(log n) - JAUH lebih cepat dari linear search!
    Syarat: data HARUS sorted
    Return: index jika ketemu, -1 jika tidak ketemu
    """
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2  # // adalah integer division
        
        if data[mid] == target:
            return mid  # Ketemu!
        elif data[mid] < target:
            left = mid + 1  # Cari di kanan
        else:
            right = mid - 1  # Cari di kiri
    
    return -1  # Tidak ketemu

def linear_search(data, target):
    """
    Linear Search - pencarian sederhana (untuk perbandingan)
    Waktu: O(n) - lambat untuk data besar
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def tampilkan_hasil(nama_algoritma, data, target, hasil):
    """Function untuk tampilkan hasil pencarian"""
    if hasil == -1:
        print(f"{nama_algoritma}: Target {target} TIDAK KETEMU")
    else:
        print(f"{nama_algoritma}: Target {target} KETEMU di index {hasil}")

# Main program
print("=" * 50)
print("PROGRAM BINARY SEARCH vs LINEAR SEARCH")
print("=" * 50)

# Test case 1
data1 = [1, 2, 5, 8, 9, 12, 15, 20]
target1 = 8

print(f"\nData: {data1}")
print(f"Cari: {target1}")
print("-" * 50)

hasil_binary = binary_search(data1, target1)
hasil_linear = linear_search(data1, target1)

tampilkan_hasil("Binary Search", data1, target1, hasil_binary)
tampilkan_hasil("Linear Search", data1, target1, hasil_linear)

# Test case 2 - tidak ketemu
print("\n" + "-" * 50)
target2 = 15
print(f"Cari: {target2}")
print("-" * 50)

hasil_binary2 = binary_search(data1, target2)
hasil_linear2 = linear_search(data1, target2)

tampilkan_hasil("Binary Search", data1, target2, hasil_binary2)
tampilkan_hasil("Linear Search", data1, target2, hasil_linear2)

# Test case 3 - User input
print("\n" + "=" * 50)
angka_string = input("Masukkan daftar angka sorted (pisahkan dengan spasi): ")
data_user = list(map(int, angka_string.split()))
target_user = int(input("Masukkan angka yang dicari: "))

print("-" * 50)
hasil_binary3 = binary_search(data_user, target_user)
hasil_linear3 = linear_search(data_user, target_user)

tampilkan_hasil("Binary Search", data_user, target_user, hasil_binary3)
tampilkan_hasil("Linear Search", data_user, target_user, hasil_linear3)
