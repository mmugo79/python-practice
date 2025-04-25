#a function to compute factorial using a loop
def factorial(n):
    result = 1 #initalize result to 1
    for i in range (1, n + 1):#loop from 1 to n
        result *= i# multiply result by 1 in each step
    return result#return computed factorial

#example usage
number = 5 #set a random number
result = factorial(number) #call the factorial function
print(f"the factorial of{number} is {result}") #output the results