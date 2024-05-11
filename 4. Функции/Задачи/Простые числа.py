n = int(input())
i = 0
p = 2


def is_prime(num):
    for f in range(2, num):
        if num % f == 0:
            return False
    return True


while i != n:
    if is_prime(p):
        print(p, end=' ')
        i += 1
    p += 1
