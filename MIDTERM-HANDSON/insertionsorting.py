
# Function to do insertion sort
def insertionSort(arr):
    steps = 0   # counter for steps
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                steps += 1   # count each shift
  
        arr[j+1] = key
        steps += 1   # count placing the key
    return steps   # return total steps
# Driver code to test above
arr = [33, 11, 17, 6, 30, 9, 1]
steps_taken = insertionSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" %arr[i])

print("Number of steps to sort:", steps_taken)
