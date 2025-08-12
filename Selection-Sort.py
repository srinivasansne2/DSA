def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap only if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Example usage:
data = [64, 25, 12, 22, 11]
print("Sorted array:", selection_sort(data))
