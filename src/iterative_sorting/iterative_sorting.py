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



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    swap = True

    while swap == True:
        change = False

        for i in range(0, len(arr) -1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                change = True
        
        if change == False:
            swap = False
  
    print(arr)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    output = []

    if len(arr) == 0:
        return []

    mini = min(arr)
    maxi = max(arr)+1

    if mini < 0:
        return "Error, negative numbers not allowed in Count Sort"
    
    count = [0 for i in range(mini, maxi)]
    print(count)

    for i in arr:
        count[i - mini] += 1

    for index, y in enumerate(count):
        if y != 0:
            for x in range(y):
                output.append(index + mini)

    

    print(arr)
    print(count)
    print(output)

    return output
    

count_sort([1,2,3,6,5,4,2,4,5,4,4])