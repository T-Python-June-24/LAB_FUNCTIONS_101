def reverse_num(x:int) -> str:
    pattern:str = ""
    for iint in range(x, 0, -1):
        for n in range(i, 0, -1):
            pattern += pattern.join(str(n))
        pattern += pattern.join("\n")
    return pattern
number_pattern = reverse_num(int(input("Enter an integer: ")))
print(number_pattern)