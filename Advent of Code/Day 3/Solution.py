import re

def mul(a, b):
    return a * b

#Problem 1
result = 0
with open("Input.txt", "r") as file:
    text = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    for match in matches:
        multiplied = eval(match)
        result += multiplied
    print(result)

# Problem 2
def get_list(iter):
    res = []
    for match in iter:
        res.append([match.end(), match.group()])
    return res

result = 0
with open("Input.txt", "r") as file:
    text = file.read()
    mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    mul_list = get_list(re.finditer(mul_pattern, text))
    do_list = get_list(re.finditer(do_pattern, text))
    dont_list = get_list(re.finditer(dont_pattern, text))
    total_list = list(map(lambda x: x[1], sorted(mul_list + do_list + dont_list)))

    enabled = True
    for string in total_list:
        if string == "do()":
            enabled = True
        elif string == "don't()":
            enabled = False
        else:
            if enabled:
                result += eval(string)
    print(result)
    
