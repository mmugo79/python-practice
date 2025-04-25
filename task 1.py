def sum_list(numbers):
    total = 0 #initialize total to 0
    for x in numbers:#loop elements in the list
        total = total + x#add each element to the total
    return total

#create a list
my_list = [10, 20, 30, 40, 50]
#call the function to output the results
print(sum_list(my_list))#output should be 150

