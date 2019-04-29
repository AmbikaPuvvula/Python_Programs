def binarySearch(lst, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)/2; 
          
        # Check if x is present at mid 
        if lst[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif lst[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1
  
  
# Test array 
lst = input('Enter the sorted list of numbers: ')
lst = lst.split()
lst = [int(x) for x in lst]
y = int(input('The number to search for: '))
# Function call 
result = binarySearch(lst, 0, len(lst)-1, y) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
