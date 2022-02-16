print("\nBubble sort")
lst = [3,6,4,10,2,7,9,25,2,4]
print(lst)

for j in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            
print(lst)


##################################################################


print("\nSelection Sort")
lst2 = [3, 1, 4, 1, 5, 9, 2, 6]
print(lst2)

# Trlstverse through all array elements 
for i in range(len(lst2)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(lst2)): 
        if lst2[min_idx] > lst2[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    lst2[i], lst2[min_idx] = lst2[min_idx], lst2[i] 
    
print(lst2)

####################################################################

print("\nInsertion Sort")
arr = [3, 1, 4, 1, 5, 9, 2, 6]

print(arr)

# Traverse through 1 to len(arr) 
for i in range(1, len(arr)): 

    key = arr[i] 

    # Move elements of arr[0..i-1], that are 
    # greater than key, to one position ahead 
    # of their current position 
    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key 
    
# Driver code to test above 
print(arr)

#####################################################################

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nShell Sort")
print(arr)
  
# Start with a big gap, then reduce the gap 
n = len(arr) 
gap =  int(n/2)

# Do a gapped insertion sort for this gap size. 
# The first gap elements a[0..gap-1] are already in gapped  
# order keep adding one more element until the entire array 
# is gap sorted 
while gap > 0: 

    for i in range(gap,n): 

        # add a[i] to the elements that have been gap sorted 
        # save a[i] in temp and make a hole at position i 
        temp = arr[i] 

        # shift earlier gap-sorted elements up until the correct 
        # location for a[i] is found 
        j = i 
        while  j >= gap and arr[j-gap] >temp: 
            arr[j] = arr[j-gap] 
            j -= gap 

        # put temp (the original a[i]) in its correct location 
        arr[j] = temp 
    gap = int(gap / 2)
  
# Driver code to test above 
print(arr)

#############################################################################
print("\nMerge Sort")
# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
print(arr)
mergeSort(arr,0,len(arr)-1) 
print(arr)



######################################################################

def partition(arr, low, high): 
    i = (low-1)         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low, high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j] <= pivot: 
  
            # increment index of smaller element 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return (i+1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
  
  
def quickSort(arr, low, high): 
    if len(arr) == 1: 
        return arr 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
  
# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
print("\nQuick Sort")
print(arr)
quickSort(arr,0,len(arr)-1) 
print(arr)
  
  
######################################################################

print("\n.sort")
arr = [12, 11, 13, 5, 6, 7] 

print(arr)
arr.sort()

print(arr)
