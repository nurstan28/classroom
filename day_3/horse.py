x = int(input('введите 1 точку координаты коня:'))
y = int(input('введите 2 точку координаты коня:'))
c = int(input('введите 1 точку координаты фигуры:'))
d = int(input('введите 2 точку координаты фигуры:'))

if x == c and y == d:
    print('конь бьет по координатам')
else:
    print('конь НЕ бьет по координатам')

