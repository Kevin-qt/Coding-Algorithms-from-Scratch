import random

def pivotIndex(arr: list, start: int, end: int) -> int:
    """Find the index of pivot"""
    idx = random.randrange(start, end)
    arr[idx], arr[end] = arr[end], arr[idx] # initial random swap
    pi = start
    for i in range(start, end):
        if arr[i] <= arr[end]:
            arr[pi], arr[i] = arr[i], arr[pi]
            pi += 1
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi

def initialCheck(func):
    def wrapper(arr, start=None, end=None):
        if start is None:
            start = 0
        if end is None:
            end = len(arr) - 1
        return func(arr, start, end)
    return wrapper

@initialCheck
def quickSort(arr: list, start: int, end: int) -> None:
    """Sort an array in ascending order"""
    if start >= end:
        return
    pivot = pivotIndex(arr, start, end)
    quickSort(arr, start, pivot-1)
    quickSort(arr, pivot+1, end)