def takes(number: int) -> str:
    """
    Rewrite the previous function so that it returns the pattern as a string, then assign the result to a variables and print it.
    """
    text = ""
    for num in range(number, 0, -1):
        for num1 in range(num, 0, -1):
            text += str(num1) +" "
        text = text + "\n"
    return text


print(takes.__doc__)
text_result = takes(5)
print(text_result)
