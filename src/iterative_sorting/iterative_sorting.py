# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        print(arr[cur_index])

        for y in range(i, len(arr)):
            if arr[smallest_index] > arr[y]:
                smallest_index = y

        arr[smallest_index],arr[cur_index] = arr[cur_index],arr[smallest_index]


        # TO-DO: swap



    print(arr)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr