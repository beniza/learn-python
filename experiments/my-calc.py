# Calculator project for collaboration
a = raw_input("Enter the first number :")
b = raw_input("\nEnter the second Number :")

def addition(x, y):
	return a + b

def sum(a,b):
	return (a + b)

def division(x, y):
	if(y!=0):
		return(x/y)
	else:
		return("Division by Zero not defined")

def mul(a,b):
    return(a*b)

def subtraction(a, b):
	return(a-b)

def mod(a,b):
	return (a%b)

print "Calculator"

