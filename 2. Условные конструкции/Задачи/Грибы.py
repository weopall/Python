count=int(input("Введите количество грибов"))
if count % 100 >= 11 and count % 100 <= 14:
    print(f'{count} грибов')
elif count % 10 >= 2 and count % 10 <= 4:
    print(f'{count} гриба')
elif count % 10 == 1:
    print(f'{count} гриб')
else:
    print(f'{count} грибов')