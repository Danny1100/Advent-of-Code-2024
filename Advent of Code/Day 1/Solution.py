list1, list2 = [], []
with open("Input.txt", "r") as file:
    for line in file:
        string_list = line.strip().split()
        list1.append(int(string_list[0]))
        list2.append(int(string_list[1]))

list1.sort()
list2.sort()

# Problem 1
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)

# Problem 2
total = 0
for i in range(len(list1)):
    count = 0
    for j in range(len(list2)):
        if list1[i] < list2[j]: break
        if list1[i] == list2[j]:
            count += 1
    total += count * list1[i]
print(total)
