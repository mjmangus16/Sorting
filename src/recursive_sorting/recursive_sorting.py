# Merge sort is a divide and conquer strategy to sorting. The idea is that you keep dividing the array down until each value is by itself. A single value in an array is guaranteed to be sorted. Breaking it down like this eventually results in a tree of steps starting with the full array, each step breaking each array in half until the last step is all single value arrays. Once you are down to single value arrays. You go through each array and start merging them back together with eachother. There should be the same amount of steps needed to break it down than there is to build it back up.

# TO-DO: complete the helpe function below to merge 2 sorted arrays

# *** Another way to handle the merge function is instead of popping items and always checking the values of the zero index. You can use 2 indexes to loop through each array. When you select a value from one of the arrays to pass in, you increase the index of that array only. You just keep increasing these indexes until you get to the end of each array


def merge(arrA, arrB):
    # The plan here is to combine both arrays into one by going through an empty array and finding what belongs at each index
    # Because of the way this is being done recursively. Regardless of what step in the recursion stack we are in, arrA and arrB should already be sorted.
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # We want to fill our pre-created merged_array with values in correct order so by looping through the count of elements available we should be able to fill every spot.
    for i in range(elements):
        # Check that each array has atleast 1 value left in it. We do this because we want need conditionals to determine what to do based on if there are values left or not.
        # If they both have values left
        if len(arrA) > 0 and len(arrB) > 0:
            # Compare values at the zero index. Whichever one is the smaller value should go into the current index of the merged_arr
            # Remove the chosen value from its array. This allows us to compare every element while just comparing to the zero index.
            if arrA[0] > arrB[0]:
                merged_arr[i] = arrB[0]
                arrB.pop(0)
            else:
                merged_arr[i] = arrA[0]
                arrA.pop(0)
            # If one of the arrays is empty, then the remaining values in the other array can get passed in to the current index. No need to compare because arrA and arrB are already sorted when they get passed in to this function
        elif len(arrA) == 0:
            merged_arr[i] = arrB[0]
            arrB.pop(0)
        else:
            merged_arr[i] = arrA[0]
            arrA.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # We want to keep splitting the array into halves until its a single item
    # We check that here
    if len(arr) == 1:
        return arr

    # First get the middle item of the array
    middle = len(arr)//2
    # Get the left and right halves of the array
    left = arr[:middle]
    right = arr[middle:]

    # We pass the recursion into the merge function above. What is happening here is we are creating a stack of merge function calls that don't begin running until the merge_sort recursion splits all the way down to 1 item. The merge_sort doesn't pass an actual value into the merge function until its gotten down to a length of 1. Once we are at 1, we have a large call stack of merge functions where we pass 2 arrays into it with just 1 item. At this point we just work our way back through the steps merging them together in order.

    return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

# Tim sort is one of the best sorts to use because it chooses which type of sort to use based on an analysis of the list. If the list is 64 elements or shorter the most efficient sort is insertion sort. So it chooses to sort the array that way

# Insertion sort loops through the array and compares the cur index to the value to the left. If the cur index is smaller, you move that bigger value to the right and you keep going backwards through the array until you get to a spot where the value to the left is not bigger.

def timsort(arr):
    # Check length is 64 or less

    if (len(arr) <= 64):
        # If it is, implement insertion sort
        # Loop through array starting with index 1
        for i in range(1, len(arr)):
            y = i
            # Store cur value
            cont = arr[i]
            # If the value at index - 1 is geater than the cur index.
            while cont < arr[y - 1] and y >= 1:
                # Move value of index - 1 over to cur value
                arr[y] = arr[y-1]
                # Keep doing this until index - 1 is not greater than cur index
                y = y - 1
            # place stored cur value in correct spot
            arr[y] = cont

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(timsort(arr1))
