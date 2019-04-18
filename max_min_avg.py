n=int(input("Enter the list of numbers to be inserted: "))
s=[]
for i in range(0,n):
    r = int(input("Enter number: "))
    s.append(r)
average = sum(s)/n
print("Maximum number in the list is :", max(s))
print("Minimum number in the list is :", min(s))
print("Average of numbers in the list :",round(average,2))



