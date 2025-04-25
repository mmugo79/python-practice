def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

    #example usage
    number = 5
    result = factorial(number)
    print(f"the factorial of {number} is {result}")
    return None

