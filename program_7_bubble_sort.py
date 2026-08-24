# Program 7: Bubble Sort Algorithm

def bubble_sort(data):
    """
    Bubble Sort - mengurutkan data dari kecil ke besar
    Waktu: O(n²) - lambat untuk data besar
    """
    n = len(data)
    
    # Pass loop
    for i in range(n):
        swapped = False  # Flag untuk optimisasi
        
        # Compare adjacent elements
        for j in range(0, n - i - 1):
            # Jika elemen kiri lebih besar dari kanan, swap
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]  # Swap
                swapped = True
        
        # Kalau tidak ada swap, data sudah sorted
        if not swapped:
            break
    
    return data

def tampilkan_proses(data, judul):
    """Function untuk tampilkan data"""
    print(f"\n{judul}")
    print(f"Data: {data}")

# Main program
print("=" * 50)
print("PROGRAM BUBBLE SORT")
print("=" * 50)

# Test case 1
data1 = [5, 2, 8, 1, 9]
tampilkan_proses(data1, "Data awal:")
data1_sorted = bubble_sort(data1)
tampilkan_proses(data1_sorted, "Setelah diurutkan:")

# Test case 2
data2 = [64, 34, 25, 12, 22, 11, 90]
tampilkan_proses(data2, "\nData 2 awal:")
data2_sorted = bubble_sort(data2)
tampilkan_proses(data2_sorted, "Setelah diurutkan:")

# Test case 3 - User input
print("\n" + "=" * 50)
angka_string = input("Masukkan daftar angka (pisahkan dengan spasi): ")
angka_list = list(map(int, angka_string.split()))

tampilkan_proses(angka_list, "Data dari user:")
angka_sorted = bubble_sort(angka_list)
tampilkan_proses(angka_sorted, "Setelah diurutkan:")
