# TO-DO: Complete the selection_sort() function below

# Selection sort starts at the first index and goes through the rest of the array comparing that index to every item in the array. It searches for the smallest item left in the array. If it finds one that is smaller than the current index then it swaps those indexes


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Hold index of current number we are comparing to
        cur_index = i
        # Keep track of smallest number left in array
        smallest_index = cur_index+1
        # Loop through all numbers right of the current index
        for y in range(i+1, len(arr)):
            # Find the smallest number in that loop and save the index
            if arr[y] < arr[smallest_index]:
                smallest_index = y
        # Check if the number in that smallest index is smaller than the current index
        if arr[cur_index] > arr[smallest_index]:
            # If it is, Swap them
            holder = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = holder

        # TO-DO: swap

    return arr


# Bubble sort starts at the beginning of an array and keeps going through the entire array over and over again until a swap doesn't happen. You basically check the current index to the index immediately to the right of it. If the current index is larger than the next index then you swap them. You just keep swapping until the largest number gets to the end of the array then the loop starts over again from the start of the array.


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Continue looping through the array until a swap doesn't happen
    swap = True
    while swap == True:
        swap = False
        # As we iterate through the array, we need to check the current index to the next index
        for i in range(0, len(arr)-1):
            # if current index is larger than next then you swap them
            if arr[i] > arr[i+1]:
                holder = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = holder
                swap = True

    return arr

# Count sort counts how many times an element appears in the array. It removes it from the original array and adds a counter in a seperate array that is located at the index of the original number. So you eventually get an array of numbers that equal a count of each time that number appeared. You then go through that newly filled array and fill the array back up starting with index 0 and passing as many numbers back in based on the count

# STRETCH: implement the Count Sort function below


# def count_sort(arr, maximum=-1):
#     # get max
#     m = 0
#     for i in arr:
#         if i > m:
#             m = i
#     # create a new array to hold counters
#     counts = [0 for i in range(0, m+1)]
#     output = [0 for i in range(0, m+1)]
#     # loop through the array
#     print(counts)
#     for i in arr:
#         # index = value of the iteration of the loop
#         counts[i] += 1

#     print(counts)
#     y = 0
#     while y < len(counts) - 1:
#         holder = y
#         for c in range(0, holder):
#             output[y] = counts.index(counts[y])
#             y += 1

#     # Once the loop is done, loop through the new array and pass the index back into the original array as many times as there as the count.

#     return output


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(count_sort(arr1))
