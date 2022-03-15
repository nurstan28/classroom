a = int(input('первое число '))
b = int(input('второе число '))
c = int(input('третье число '))

if b < a > c:
    print(a,'больше')
elif a < b > c:
    print(b, 'больше')
elif a < c > b:
    print(c, 'больше')
else:
    print('0')

if b > a < c:
    print(a, 'меньше')
elif a > b < c:
    print(b, 'меньше')
elif a > c < b:
    print(c, 'меньше')
