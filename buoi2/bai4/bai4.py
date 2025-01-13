import time
import random
def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def hybrid_quick_sort(arr, low, high, threshold=10):
    if low < high:
        if high - low < threshold:  # Kích thước mảng con nhỏ hơn ngưỡng
            insertion_sort(arr, low, high)
        else:
            pi = partition(arr, low, high)
            hybrid_quick_sort(arr, low, pi - 1, threshold)
            hybrid_quick_sort(arr, pi + 1, high, threshold)


# Tạo mảng ngẫu nhiên
arr_size = 100000
arr = [random.randint(1, 100000) for _ in range(arr_size)]

# Đo thời gian cho Hybrid Quick Sort
start_time = time.time()
hybrid_quick_sort(arr, 0, len(arr) - 1, threshold=20)
hybrid_time = time.time() - start_time

# Đo thời gian cho Quick Sort thuần túy
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = [random.randint(1, 100000) for _ in range(arr_size)]
start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
quick_time = time.time() - start_time

print(f"Hybrid Quick Sort: {hybrid_time:.4f} seconds")
print(f"Quick Sort: {quick_time:.4f} seconds")
