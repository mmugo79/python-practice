def addDigits(num):
    if num == 0:
        return 0

    return (num % 10) + addDigits(num // 10)