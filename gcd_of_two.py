# Python Program to find GCD of Two Numbers

num1 = float(input(" Please Enter the First Number : "))
num2 = float(input(" Please Enter the Second Number : "))

a = num1
b = num2

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        gcd = i
    i = i + 1

#print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))
print("GCD of two numbers is:", gcd)
