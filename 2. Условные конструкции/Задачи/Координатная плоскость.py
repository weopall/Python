x=int(input())
y=int(input())
if x>0 and y>0:
    print("первая четверть")
if x<0 and y<0:
    print("третья четверть")
if x>0 and y<0:
    print("четвертая четверть")
if x<0 and y>0:
    print("вторая четверть")
if x==0 or y==0:
    print("на оси")