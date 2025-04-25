def reverse_string(text):
    reversed_text="" #start with an empty string
    length = len(text)
    index= length -1
    #loop from last character to first
    while index>=0:
      reversed_text += text[index]#add each character to the result
      index -=1#move backwards

    return reversed_text #return results

#example usage
original = "MOSES"
reversed_result = reverse_string(original)
print("reversed_string:", reversed_result)

