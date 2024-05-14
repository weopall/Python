n = int(input())
k = 0
p = 1
def is_top(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s == num

while n != k:
    if is_top(p):
        k += 1
        print(p)
    p += 1