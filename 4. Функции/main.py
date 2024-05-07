# Функция, выводит числа в диапазоне от a до b
def print_seq(a, b):
    for i in range(a, b + 1):
        print(i, end=' ')

# Функция, которая находит сумму чисел в диапазоне от a до b
def sum_seq(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s


print_seq(5, 15)
print()
print(sum_seq(5, 15))







