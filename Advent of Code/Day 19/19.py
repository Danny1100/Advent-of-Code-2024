segments = []
problems = []
with open("Input.txt") as file:
    first = True
    for line in file:
        if line == '\n':
            first = False
        elif first:
            segments = line.strip().replace(" ", "").split(',')
        else:
            problems.append(line.strip())
print(segments)
print(problems)

# Problem 1
# def dp(i, problem, score):
#     if i >= len(problem): return score
#     if i in cache: return cache[i]

#     res = float("inf")
#     substring = problem[i:]
#     for segment in segments:
#         if len(segment) > len(substring): continue
#         if segment != problem[i:i+len(segment)]: continue
        
#         res = min(dp(i+len(segment), problem, score+1), res)
#     cache[i] = res
#     return res

# result = 0
# for problem in problems:
#     cache = {}
#     res = dp(0, problem, 0)
#     if res != float("inf"):
#         result += 1
# print(result)

# Problem 2
def dp(i, problem):
    if i >= len(problem): return 1
    if i in cache: return cache[i]

    res = 0
    substring = problem[i:]
    for segment in segments:
        if len(segment) > len(substring): continue
        if segment != problem[i:i+len(segment)]: continue
        
        res += dp(i+len(segment), problem)
    cache[i] = res
    return res

result = 0
for problem in problems:
    cache = {}
    res = dp(0, problem)
    result += res
print(result)