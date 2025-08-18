def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # found
        elif arr[mid] < target:
            low = mid + 1  # search right half
        else:
            high = mid - 1  # search left half
    return -1  # not found