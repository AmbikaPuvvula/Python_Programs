lst = input('Enter the list of numbers: ')
lst = lst.split()
lst = [int(x) for x in lst]
x = int(input("enter number to search:"))
i = flag = 0
 
while i < len(lst):
	if lst[i] == x:
		flag = 1
		break
 
	i = i + 1
 
if flag == 1:
	print("number found at position:", i + 1)
else:
	print("number not found")
