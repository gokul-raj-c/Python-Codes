# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
while True:
   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.exit")
   choice = input("Enter choice")
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   if choice == '1':
     print(num1, "+", num2, "=", add(num1, num2))
   elif choice == '2':
     print(num1, "-", num2, "=", subtract(num1, num2))
   elif choice == '3':
     print(num1, "*", num2, "=", multiply(num1, num2))
   elif choice == '4':
     print(num1, "/", num2, "=", divide(num1, num2))
   elif choice == '5':
     print("exit")
     break
   else:
     print("Invalid Input")