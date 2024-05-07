a=int(input())
b=int(input())
c=int(input())
#сумма любых двух сторон больше третьей, то существует
if a + b > c and a + c > b and c + b > a:
    print("Может")
else:
    print(f'Не может')