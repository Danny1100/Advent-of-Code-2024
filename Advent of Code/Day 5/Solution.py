rules = {}
updates = []

switch_formatting = False
with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            switch_formatting = True
            continue
        if not switch_formatting:
            rule = list(map(int, line.split('|')))
            p1, p2 = rule[0], rule[1]
            if p1 in rules:
                rules[p1].add(p2)
            else:
                rules[p1] = set({p2})
        else:
            update = list(map(int, line.split(',')))
            updates.append(update)

# Problem 1
def update_is_valid(update):
    cache = {}
    for i in range(len(update)):
        n = update[i]
        if n not in cache:
            cache[n] = [i]
        else:
            cache[n].append(i)
    
    for i in range(len(update)):
        n = update[i]
        for key in rules.keys():
            # If n is the key, check that index of n is less than index of every number in the rule.
            if n == key:
                for n_after in rules[key]:
                    if n_after in cache and min(cache[n_after]) < i:
                        return False
            # If n is the value, check that it is after the key
            elif n in rules[key]:
                if key in cache and max(cache[key]) > i:
                    return False
    return True

result = 0
for update in updates:
    if update_is_valid(update):
        m = len(update) // 2
        result += update[m]
print(result)

# Problem 2
result2 = 0
for update in updates:
    if update_is_valid(update): continue

    update_set = set(update)
    relevant_rules = {}
    for key in rules.keys():
        if key in update_set and (rules[key] & update_set):
            relevant_values = set()
            for value in rules[key]:
                if value in update_set:
                    relevant_values.add(value)
            relevant_rules[key] = relevant_values
    # TODO? make the rules explicit. This may already been innate in the input
    # order based on length in relevant rules dictionary. Start from longest = smallest, remember to remove from both relevant rules and update_set. Make sure to add remaining numbers in update_set
    correct_order_list = sorted(relevant_rules.keys(), key=lambda key: len(relevant_rules[key]), reverse=True)
    m = (len(correct_order_list) + 1) // 2
    result2 += correct_order_list[m]
print(result2)
