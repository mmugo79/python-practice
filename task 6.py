#calculate sum of digits using recursion
def addDigits(num):
    #if number is 0,return o
    if num == 0:
        return 0
#recursive case:add the last digit to the results of addDigits on the remaining digits
    return (num % 10) + addDigits(num // 10)
#example usage
print(addDigits(1234))#output should be 10