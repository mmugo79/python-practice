#function to calculate factorial using recursion
def factorial(n):
    # if n is 0, return 1
    if n ==0:
        return 1
    else:
        #recurisve case
        return n * factorial(n-1)

#example usage
number = 5
result = factorial(number)
print(f"the factorial of {number} is {result}")



