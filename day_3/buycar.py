brand = str(input('марка авто:'))
year = int(input('год авто:'))
mileage12 = int(input('пробег авто:'))
color12 = str(input('цвет авто:'))
price12 = int(input('цена авто:'))
swpos = str(input('расположение руля:'))
owner = int(input('владельцев по птс:'))

counter1 = 0
counter2 = 0

if (brand == 'toyota' or brand == 'lexus') and year == 2004 and 0 <= mileage12 <= 150000 and (color12 == 'white' or 'grey') and swpos == 'left' and owner <= 2 and price12 <= 10000:
    counter1 +=1
elif (brand == 'toyota' or brand == 'lexus') and year == 2004 and 150000 <= mileage12 <= 200000 and (color12 == 'white' or 'grey') and swpos == 'left' and owner <= 2 and price12 <= 8000:
    counter2 += 1

if counter1 == 1:
    print('есть в наличии1')
elif counter2 == 1:
    print('есть в наличии2')
else:
    print('такой машины нет! извините')
