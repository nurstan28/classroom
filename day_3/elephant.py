x = int(input('введите 1 точку координаты слона:'))
y = int(input('введите 2 точку координаты слона:'))
c = int(input('введите 1 точку координаты фигуры:'))
d = int(input('введите 2 точку координаты фигуры:'))

if x == c and y == d:
    print('конь бьет по координатам')
else:
    print('конь НЕ бьет по координатам')
