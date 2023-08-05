def binarySearch(arr: list, target) -> int:
    '''Search for the index of the target in a sorted array
        return -1 if target is not found'''
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1
        
        else:
            return mid
    return -1