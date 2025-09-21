#Write a Python Program to Print the Fibonacci sequence
limit = int(input("enter limit: "))
n1, n2 = 0, 1
if limit <= 0:
   print("Please enter a positive integer")
elif limit == 1:
   print(f"Fibonacci sequence upto{limit}:")
   print(n1)
else:
   print("Fibonacci sequence:")
   for i in range(limit):
      print(n1)
      n1,n2=n2,n1+n2