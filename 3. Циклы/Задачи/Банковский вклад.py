start_sum = int(input())
percent = int(input())
target_sum = int(input())
s = 0
while start_sum < target_sum:
    start_sum = start_sum + start_sum * (percent / 100)
    s += 1
    print(f'{s}-{start_sum}')
print(f'Кол-во месяцев: {s}; Итоговая сумма: {start_sum}')
