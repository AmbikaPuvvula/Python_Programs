def binary_search(lst, start, end, key):
    if not start < end:
        return -1
 
    mid = (start + end)//2
    if lst[mid] < key:
        return binary_search(lst, mid + 1, end, key)
    elif lst[mid] > key:
        return binary_search(lst, start, mid, key)
    else:
        return mid
 
 
lst = input('Enter the sorted list of numbers: ')
lst = lst.split()
lst = [int(x) for x in lst]
key = int(input('The number to search for: '))
 
index = binary_search(lst, 0, len(lst), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
