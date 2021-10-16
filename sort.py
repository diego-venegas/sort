def get_pivot(array, i, j):
    pivot = array[j]
    item = i - 1

    for k in range(i, j):
        if array[k] <= pivot:
            item = item + 1
            (array[item], array[k]) = (array[k], array[item])

    array[item + 1], array[j] = array[j], array[item + 1]

    return item + 1


def quick_sort(array, i=None, j=None):
    if i == None:
        i = 0
    if j == None:
        j = len(array) - 1

    if i < j:
        pivot = get_pivot(array, i, j)
        quick_sort(array, i, pivot - 1)
        quick_sort(array, pivot + 1, j)



def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]

