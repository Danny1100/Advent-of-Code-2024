sn = []
with open("Input.txt") as file:
    for line in file:
        sn.append(int(line.strip()))


# Problem 1
def mix(secret, given):
    return secret ^ given


def prune(n):
    return n % 16777216


# def get_number(s, iterations):
#     secret = s
#     for _ in range(iterations):
#         multiplied = secret * 64
#         secret = mix(secret, multiplied)
#         secret = prune(secret)

#         divided = secret // 32
#         secret = mix(secret, divided)
#         secret = prune(secret)

#         multiplied = secret * 2048
#         secret = mix(secret, multiplied)
#         secret = prune(secret)

#     return secret


# result = 0
# for n in sn:
#     res = get_number(n, 2000)
#     result += res
# print(result)

# Problem 2
cache = {}


def get_number(s, iterations):
    secret = s
    data = [(int(str(secret)[-1]), "N/A")]  # (secret_number_digit, difference)
    for i in range(iterations):
        multiplied = secret * 64
        secret = mix(secret, multiplied)
        secret = prune(secret)

        divided = secret // 32
        secret = mix(secret, divided)
        secret = prune(secret)

        multiplied = secret * 2048
        secret = mix(secret, multiplied)
        secret = prune(secret)

        last_digit = int(str(secret)[-1])
        data.append((last_digit, last_digit - data[-1][0]))
        if i >= 3:
            temp = data[i - 2 : i + 2]
            ls = []
            for t in temp:
                ls.append(t[1])
            window = tuple(ls)
            if window not in cache:
                cache[window] = last_digit
            else:
                cache[window] += last_digit

            # if window == (-2, 2, -1, -1):
            #     print(s)

    return secret


for n in sn:
    res = get_number(n, 2000)

result = 0
for key, val in cache.items():
    if val > result:
        result = val
    # if val == 30:
    #     print(key)
print(result)
