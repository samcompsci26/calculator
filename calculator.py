# SCCM4910 lab project - a four-operation calculator
#add
def add(a,b):
	return a+b

#subtract
def subtract(a,b):
	return a-b

#multiply
def multiply(a,b):
	return a*b

#divide
def divide(a,b):
	return a/b

#calculate circle area
def circle_area(r):
	if r >= 0:
		return 3.14*r**2
	else:
		return "Error"



def main():
	while True:
		a = float(input("Enter a first number:  "))
		op = input("Enter an operator (+ - * /):  ")
		b = float(input("Enter a second number:  "))
		if op == "+":
			print("Result:", add(a, b))
		elif op == "-":
			print("Result:", subtract(a, b))
		elif op == "*":
			print("Result:", multiply(a, b))
		elif op == "/":
			print("Result:", divide(a, b))
		else:
			print("Unknown operator:", op)

if __name__ == "__main__":
	main()
