import random
import time

# Hàm Randomized Partition
def randomized_partition(arr, low, high):
    random_pivot = random.randint(low, high)  # Chọn pivot ngẫu nhiên
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]  # Đưa pivot về cuối
    return partition(arr, low, high)

# Hàm Partition tiêu chuẩn
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Hàm Randomized Quick Sort
def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)  # Gọi partition ngẫu nhiên
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Hàm Quick Sort mặc định
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Gọi partition tiêu chuẩn
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Đo thời gian thực thi
sizes = [5000, 10000, 20000]
for size in sizes:
    array = [random.randint(0, 100000) for _ in range(size)]
    
    # Đo thời gian Quick Sort mặc định
    start_time = time.time()
    quick_sort(array.copy(), 0, len(array) - 1)
    default_time = time.time() - start_time

    # Đo thời gian Randomized Quick Sort
    start_time = time.time()
    randomized_quick_sort(array.copy(), 0, len(array) - 1)
    randomized_time = time.time() - start_time
    
    print(f"Kích thước mảng: {size}")
    print(f"Thời gian Quick Sort mặc định: {default_time:.4f} giây")
    print(f"Thời gian Randomized Quick Sort: {randomized_time:.4f} giây")
    print("-" * 40)
