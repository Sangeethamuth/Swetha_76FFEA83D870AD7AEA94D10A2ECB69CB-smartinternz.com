# python program to find the factorial of a number using Recursion
#Fact_Recur.py
def fact(m):
   if m<=1:
     return 1
   else:
      return m*fact(m-1)
  # main program
n=int(input("Enter the value of n:"))
print("The factorial of",n," is ", fact (n))
