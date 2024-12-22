result = 0
def is_safe(levels):
    for i in range(1, len(levels)):
        if i == 1:
            if levels[i] > levels[i-1]:
                increasing = True
            else: increasing = False

        diff = abs(levels[i] - levels[i-1]) 
        if diff < 1 or diff > 3: return False
        if increasing and levels[i] < levels[i-1]: return False
        if not increasing and levels[i] > levels[i-1]: return False
    return True

with open("Input.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            result += 1
    print(result)

result2 = 0
with open("Input.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))

        if is_safe(levels):
            result2 += 1
            continue

        for i in range(len(levels)):
            new_list = levels[:i] + levels[i + 1:]
            if is_safe(new_list):
                result2 += 1
                break

    print(result2)