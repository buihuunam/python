import random
import time

# Hàm tạo mảng ngẫu nhiên
def generate_array(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Thuật toán Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Hàm Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Đo thời gian thực thi
sizes = [5000, 10000, 20000]
for size in sizes:
    array = generate_array(size)
    
    # Đo thời gian Merge Sort
    start_time = time.time()
    merge_sort(array.copy())
    merge_time = time.time() - start_time
    
    # Đo thời gian Bubble Sort
    start_time = time.time()
    bubble_sort(array.copy())
    bubble_time = time.time() - start_time
    
    print(f"Kích thước mảng: {size}")
    print(f"Thời gian Merge Sort: {merge_time:.4f} giây")
    print(f"Thời gian Bubble Sort: {bubble_time:.4f} giây")
    print("-" * 40)
