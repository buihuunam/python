def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:l + n1]
    R = arr[m + 1:m + 1 + n2]

    i, j = 0, 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        # Merge the sorted halves
        merge(arr, l, m, r)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    mergeSort(arr, 0, len(arr) - 1)
    print("Sorted array is: ", arr)