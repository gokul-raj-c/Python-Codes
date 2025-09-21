#Write a Python Program to Split the array and add the first part to the end?
def split_and_add(arr, k):
  if k <= 0 or k >= len(arr):
     return arr  
  first_part = arr[:k]
  second_part = arr[k:]
  result = second_part + first_part
  return result

arr = list(map(int, input("Enter array: ").split()))
k = int(input("enter value: "))
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)