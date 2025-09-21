# Write a Python Program to check if given array is Monotonic.
def is_monotonic(arr):
   increasing = decreasing = True
   for i in range(1, len(arr)):
     if arr[i] > arr[i - 1]:
       decreasing = False
     elif arr[i] < arr[i - 1]:
       increasing = False
   return increasing or decreasing

arr=list(map(int, input("enter array: ").split()))
res=is_monotonic(arr)
if res:
  print("array is monotonic")
else:
  print("array is not monotonic")