def CountingSort(arr: list[int]) -> list[int]:
    '''Sort a given non-negative integers array'''
    end = max(arr)
    count = [0 for i in range(end+1)]
    res = [0 for i in range(len(arr))]
    # count the occurrence of integers
    for i in range(len(arr)):
        j = arr[i]
        count[j] += 1
    # determine the position range of integers
    for i in range(1, end+1):
        count[i] += count[i-1]
    # stable sort by looping reversely
    for i in range(len(arr)-1, -1, -1):
        j = arr[i]
        count[j] -= 1
        res[count[j]] = arr[i]
    
    return res