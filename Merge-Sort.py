def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # middle index
        left = arr[:mid]     # left half
        right = arr[mid:]    # right half
        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)
        # Merge step
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:   # keep stable
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

print(merge_sort([9,7,8,6,4,5,3,1,2]))