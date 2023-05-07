N = 2
max = 0
len = 0
max_index = -1
while N != 0:
    N = int(input())
    if N > max:
        max = N
        max_index = len
    len += 1
print(max_index)