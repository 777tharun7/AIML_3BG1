#Write a function that takes an integer and returns the sum of its digits. For example, for the number 1234, the output should be 10 (1 + 2 + 3 + 4).
n = input("enter the number....")
k = 0 
if n.isdigit():
  for i in n:
    k += int(i)
  print(f"the sum of digits in given {n} is {k}")
else:
  print(f"u enter the number as {n} , so pls enter the number only.....")
