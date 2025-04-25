def addDigits(num):
    if num == 0:
        return 0

    return (num % 10) + addDigits(num // 10)
#example usage
print(addDigits(1234))#output should be 10