# program to find compound interest
 
def compound_interest(principle, time, rate):  
	CI = principle * (pow((1 + rate / 100), time)) 
	print("Compound interest is", CI) 
 
compound_interest(10000, 5, 10.25) 
