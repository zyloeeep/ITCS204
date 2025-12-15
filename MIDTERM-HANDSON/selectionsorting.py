# Python program for implementation of Selection Sort
import sys
A = [6, 30, 17, 9, 11, 1, 33]

steps = 0   # counter for steps
  
# Traverse through all array elements
for i in range(len(A)):
      
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
        steps += 1   # count each comparison
              
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
    steps += 1   # count each swap
  
# Driver code to test above
print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i])

print("Number of steps to sort:", steps)
