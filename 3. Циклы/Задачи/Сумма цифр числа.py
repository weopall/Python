n = int(input()) #111 % 10 1 1 1
s = 0
while n > 0:
    s += n % 10
    n = n // 10
print(s)
