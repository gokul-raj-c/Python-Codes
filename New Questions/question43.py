# Write a Python program to check if the given number is a Disarium Number.

def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    if digit_sum == number:
        return number

num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")
