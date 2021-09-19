import math

def num_split(n):

    split = []
    n_len = 1
    n_copy = n

    while n_copy >= 10 or n_copy <= -10:
        n_len += 1
        n_copy /= 10

    for i in range(n_len):
        power = math.pow(10, n_len - i - 1)
        val = math.ceil(n / power) * power
        if n > 0:
            val = math.floor(n / power) * power
        split.append(val)
        n -= val

    return split

print(num_split(1049164))
