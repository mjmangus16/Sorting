# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in range(elements):
        print("test", arrA, arrB, "index", i)
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
            else:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
        elif len(arrA):
            merged_arr[i] = arrA[0]
            arrA.pop(0)
        elif len(arrB):
            merged_arr[i] = arrB[0]
            arrB.pop(0)
    print(merged_arr)

    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # TO-DO
    half = len(arr) // 2

    if len(arr) > 1:
        arr = merge(merge_sort(arr[half:]), merge_sort(arr[:half]))

    return arr


cont1 = [1, 3, 5, 6, 7, 9, 2, 4, 8]

cont = merge_sort(cont1)
print(cont)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
