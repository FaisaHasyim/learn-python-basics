# Program 9: Selection Sort Algorithm

def selection_sort(data):
    """
    Selection Sort - mencari minimum setiap pass
    Waktu: O(n²) - sama dengan bubble sort tapi lebih simple
    Jumlah swap: n-1 (lebih efisien dari bubble sort)
    """
    n = len(data)
    
    # Outer loop - berapa pass
    for i in range(n):
        min_index = i  # Asumsi elemen pertama adalah minimum
        
        # Inner loop - cari minimum dari i+1 sampai akhir
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j  # Update index minimum
        
        # Swap elemen di index i dengan elemen minimum
        data[i], data[min_index] = data[min_index], data[i]
    
    return data

def tampilkan_step_by_step(data):
    """Function untuk tampilkan setiap step sorting"""
    n = len(data)
    print(f"\nData awal: {data}\n")
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        
        # Swap
        data[i], data[min_index] = data[min_index], data[i]
        print(f"Pass {i+1}: {data}")
    
    return data

# Main program
print("=" * 50)
print("PROGRAM SELECTION SORT")
print("=" * 50)

# Test case 1 - Simple
data1 = [5, 2, 8, 1, 9]
print(f"\nTest 1: {data1}")
result1 = selection_sort(data1.copy())
print(f"Result: {result1}\n")

# Test case 2 - Step by step
data2 = [5, 2, 8, 1, 9]
print("Test 2 - Step by Step:")
result2 = tampilkan_step_by_step(data2)

# Test case 3 - User input
print("\n" + "=" * 50)
angka_string = input("Masukkan daftar angka (pisahkan dengan spasi): ")
data_user = list(map(int, angka_string.split()))

print("\nStep by Step:")
result_user = tampilkan_step_by_step(data_user)