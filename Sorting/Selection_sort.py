def selectionSort(arr: list[int]) -> list[int]:
    '''Sort an array in-place in ascending order'''

    def minElement(unsorted_arr: list[int]) -> int:
        '''Find the minimum element in a given array and
            return its index'''
        min_idx = 0
        min_element = unsorted_arr[0]

        for i in range(1,len(unsorted_arr)):
            if unsorted_arr[i] < min_element:
                min_idx = i
                min_element = unsorted_arr[i]

        return min_idx
    
    for i in range(len(arr)):
        min_index = minElement(arr[i:]) + i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr