#add
def add(a,b):
	return a+b

#subtract
def subtract(a,b):
	return a-b

#multiply
def  multiply(a,b):
	return a*b

#divide
def divide(a,b):
	return a/b

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
