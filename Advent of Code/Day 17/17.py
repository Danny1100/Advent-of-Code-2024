from collections import deque

with open("Input.txt") as file:
    for line in file:
        if line.startswith("Register A"):
            a = int(line.split(" ")[2].strip())
        elif line.startswith("Register B"):
            b = int(line.split(" ")[2].strip())
        elif line.startswith("Register C"):
            c = int(line.split(" ")[2].strip())
        elif line.startswith("Program"):
            program = list(map(int, line.split(" ")[1].strip().split(",")))
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


result = []

i = 0
while i < len(program):
    opcode, operand = program[i], program[i + 1]
    print(opcode, operand)
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

print(result)
print(str(result).replace(" ", ""))

# Problem 2
# start = (0, 1)  # the current number, how many digits of program this number covers
# q = deque([start])
# final_result = float("inf")

# while q:
#     c_n, digits = q.pop()
#     minimum, maximum = c_n * 8, (c_n + 1) * 8
#     for x in range(minimum, maximum):
#         a = x
#         result = []
#         i = 0
#         while i < len(program):
#             opcode, operand = program[i], program[i + 1]
#             if opcode == 0:
#                 numerator = a
#                 denominator = 2 ** get_combo_operand(operand)
#                 res = numerator // denominator
#                 a = res
#             elif opcode == 1:
#                 res = b ^ operand
#                 b = res
#             elif opcode == 2:
#                 res = get_combo_operand(operand) % 8
#                 b = res
#             elif opcode == 3:
#                 if a != 0:
#                     i = operand
#                     continue
#             elif opcode == 4:
#                 res = b ^ c
#                 b = res
#             elif opcode == 5:
#                 res = get_combo_operand(operand) % 8
#                 result.append(res)
#             elif opcode == 6:
#                 numerator = a
#                 denominator = 2 ** get_combo_operand(operand)
#                 res = numerator // denominator
#                 b = res
#             elif opcode == 7:
#                 numerator = a
#                 denominator = 2 ** get_combo_operand(operand)
#                 res = numerator // denominator
#                 c = res

#             i += 2

#         if result == program[len(program) - digits : len(program)]:
#             # print(x, result)
#             q.append((x, digits + 1))
#             if result == program:
#                 final_result = min(x, final_result)

# print(final_result)
