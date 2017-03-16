# Calculator project for collaboration
a = raw_input("Enter the first number :")
b = raw_input("\nEnter the second Number :")
print "The sum is :", a + b

def division(x, y):
	if(y!=0):
		return(x/y)
	else:
		return("Division by Zero not defined")

def mul(a,b):
    c=a*b
    print c
