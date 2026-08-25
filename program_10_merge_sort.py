# Program 10: Merge Sort Algorithm

def merge_sort(data):
    """
    Merge Sort - Divide and Conquer algorithm
    Waktu: O(n log n) - JAUH lebih cepat untuk data besar!
    Ruang: O(n) - butuh extra space untuk merge
    """
    if len(data) <= 1:
        return data
    
    # Step 1: Divide
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    # Step 2: Conquer (Recursive)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Step 3: Merge
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Function untuk merge 2 sorted arrays"""
    result = []
    i = j = 0
    
    # Compare elemen dari left dan right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Tambah sisa elemen (kalau ada)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def tampilkan_visual(data, level=0):
    """Function untuk tampilkan proses divide"""
    if len(data) <= 1:
        return data
    
    print("  " * level + f"Divide: {data}")
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    left_sorted = tampilkan_visual(left, level + 1)
    right_sorted = tampilkan_visual(right, level + 1)
    
    result = merge(left_sorted, right_sorted)
    print("  " * level + f"Merge: {result}")
    
    return result

# Main program
print("=" * 60)
print("PROGRAM MERGE SORT")
print("=" * 60)

# Test case 1 - Simple
data1 = [5, 2, 8, 1, 9]
print(f"\nTest 1: {data1}")
result1 = merge_sort(data1)
print(f"Result: {result1}\n")

# Test case 2 - Visual step by step
data2 = [5, 2, 8, 1, 9, 4]
print("Test 2 - Visual Step by Step:")
print(f"Data awal: {data2}\n")
result2 = tampilkan_visual(data2)
print(f"\nFinal result: {result2}\n")

# Test case 3 - Besar data
data3 = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]
print("-" * 60)
print(f"Test 3 (besar): {data3}")
result3 = merge_sort(data3)
print(f"Result: {result3}\n")

# Test case 4 - User input
print("=" * 60)
angka_string = input("Masukkan daftar angka (pisahkan dengan spasi): ")
data_user = list(map(int, angka_string.split()))

print("\nVisual Step by Step:")
result_user = tampilkan_visual(data_user)
print(f"\nFinal result: {result_user}")
