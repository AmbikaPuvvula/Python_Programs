first = int(input("Enter first number: "))
last = int(input("Enter last number: "))
print("Prime numbers between",first,"and",last,"are:")
for i in range(first, last + 1):  
   if i > 1: 
       for n in range(2, i): 
           if (i % n) == 0: 
               break
       else: 
           print(i) 



