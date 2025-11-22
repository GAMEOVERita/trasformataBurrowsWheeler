# Sorting with QuickSort 
def partition(arr:list, low:int, high:int):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def qSort(arr:list, low:int, high:int):
    if low < high:
        p = partition(arr, low, high)
        qSort(arr, low, p - 1)
        qSort(arr, p + 1, high)

# i wanted to add multiprocessing but i couldn't figure out how to make quicksort work with it
