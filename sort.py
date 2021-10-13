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
