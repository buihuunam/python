comparison_count = 0  # Biến toàn cục để đếm số lần so sánh

def merge_sort(arr):
    global comparison_count
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            comparison_count += 1  # Đếm so sánh
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

def quick_sort(arr, low, high):
    global comparison_count
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    global comparison_count
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparison_count += 1  # Đếm so sánh
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Thử nghiệm
arr1 = [38, 27, 43, 3, 9, 82, 10]
comparison_count = 0
merge_sort(arr1)
print("Merge Sort - Số lần so sánh:", comparison_count)

arr2 = [38, 27, 43, 3, 9, 82, 10]
comparison_count = 0
quick_sort(arr2, 0, len(arr2) - 1)
print("Quick Sort - Số lần so sánh:", comparison_count)
