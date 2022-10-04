value = ((5+7*5/8)/3**5)
print: value

x1 = int(input())
x2 = int(input())
print((x1*x2)%109)

x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1 == x2 == x3:
    print(3)
elif x1 == x2 or x2 == x3 or x1 == x3:
    print(2)
else:
    print(0)
