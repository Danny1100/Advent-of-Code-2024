equations = []
with open("Input.txt", "r") as file:
    for line in file:
        goal, nums = line.strip().split(':')
        equations.append([int(goal), list(map(int, nums.strip().split(' ')))])

# Problem 1
result = 0

def backtrack(i, goal, nums, current):
    if i >= len(nums):
        if current == goal: return True
        return False
    return backtrack(i+1, goal, nums, current + nums[i]) or backtrack(i+1, goal, nums, current * nums[i])

for equation in equations:
    goal, nums = equation[0], equation[1]
    if backtrack(1, goal, nums, nums[0]):
        result += goal
print(result)

# Problem 2
result2 = 0

def backtrack2(i, goal, nums, current):
    if i >= len(nums):
        if current == goal: return True
        return False
    return (backtrack2(i+1, goal, nums, current + nums[i]) or
            backtrack2(i+1, goal, nums, current * nums[i]) or
            backtrack2(i+1, goal, nums, int(str(current) + str(nums[i]))))

for equation in equations:
    goal, nums = equation[0], equation[1]
    if backtrack2(1, goal, nums, nums[0]):
        result2 += goal
print(result2)