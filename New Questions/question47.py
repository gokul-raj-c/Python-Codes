#Write a Python program to determine whether the given number is a HarshadNumber.
def is_harshad_number(num):
   digit_sum = sum(int(i) for i in str(num))
   return num % digit_sum == 0

num = int(input("Enter a number: "))
if is_harshad_number(num):
   print(f"{num} is a Harshad Number.")
else:
   print(f"{num} is not a Harshad Number.")