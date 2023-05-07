len = 0
sum = 0
N = int(input())
while N != 0:
    sum += N
    len += 1
    N = int(input())
print(sum / len)