with open("Input.txt") as file:
    for line in file:
        if line.startswith("Register A"):
            a = int(line.split(" ")[2].strip())
        elif line.startswith("Register B"):
            b = int(line.split(" ")[2].strip())
        elif line.startswith("Register C"):
            c = int(line.split(" ")[2].strip())
        elif line.startswith("Program"):
            program = list(map(int, line.split(" ")[1].strip().split(',')))
print(a, b, c, program)

# Problem 1
def get_combo_operand(operand):
    if operand < 4:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c

# result = []

# i = 0
# while i < len(program):
#     opcode, operand = program[i], program[i+1]
#     print(opcode, operand)
#     if opcode == 0:
#         numerator = a
#         denominator = 2 ** get_combo_operand(operand)
#         res = numerator // denominator
#         a = res
#     elif opcode == 1:
#         res = b ^ operand
#         b = res
#     elif opcode == 2:
#         res = get_combo_operand(operand) % 8
#         b = res
#     elif opcode == 3:
#         if a != 0:
#             i = operand
#             continue
#     elif opcode == 4:
#         res = b ^ c
#         b = res
#     elif opcode == 5:
#         res = get_combo_operand(operand) % 8
#         result.append(res)
#     elif opcode == 6:
#         numerator = a
#         denominator = 2 ** get_combo_operand(operand)
#         res = numerator // denominator
#         b = res
#     elif opcode == 7:
#         numerator = a
#         denominator = 2 ** get_combo_operand(operand)
#         res = numerator // denominator
#         c = res
    
#     i += 2

# print(result)
# print(str(result).replace(" ", ""))

# Problem 2
for x in range(999999999):
    a = x
    if x % 10000 == 0: print(x)
    result = []
    i = 0
    while i < len(program):
        opcode, operand = program[i], program[i+1]
        if opcode == 0:
            numerator = a
            denominator = 2 ** get_combo_operand(operand)
            res = numerator // denominator
            a = res
        elif opcode == 1:
            res = b ^ operand
            b = res
        elif opcode == 2:
            res = get_combo_operand(operand) % 8
            b = res
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            res = b ^ c
            b = res
        elif opcode == 5:
            res = get_combo_operand(operand) % 8
            result.append(res)
        elif opcode == 6:
            numerator = a
            denominator = 2 ** get_combo_operand(operand)
            res = numerator // denominator
            b = res
        elif opcode == 7:
            numerator = a
            denominator = 2 ** get_combo_operand(operand)
            res = numerator // denominator
            c = res
        
        i += 2

    if result == program:
        print(i)
        break