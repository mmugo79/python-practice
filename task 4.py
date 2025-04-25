def reverse_string(text):
    reversed_text=""
    length = len(text)

index= length -1
while index>=0:
    reversed_text += text[index]
    index -=1

    return reversed_text

#example usage
original = "zytho$n"
reversed_result = reverse_string(original)

