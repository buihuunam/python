def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #swap arr[i] and arr[min_idx]
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    selection_sort(arr)
    print("Sorted array is:", arr)