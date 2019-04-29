# Function calculates the decimal equivalent 
# to given binary number 

def binaryToDecimal(binary):
    binary1 = binary
    decimal, s, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + (dec * pow(2, s))
        binary = binary//10
        s += 1
    print(decimal)
	

 
binaryToDecimal(1001)
 
