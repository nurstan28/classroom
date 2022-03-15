print('Выберите дом')

area = str(input('Выберите район: чон арык, байтик, или ортосай:'))
walls = str(input('Стены из кирпича или пескоблока?:'))
plot = int(input('Введите участок в сотках:'))
price = int(input('Стоимость дома:'))
counter1 = 0
counter2 = 0
if area == 'чон арык' or area == 'байтик' or area == 'ортосай':
    counter1 += 1
if walls == 'кирпич' and plot <= 4:
    if price <= 50000:
        counter1 += 1
if counter1 == 2:
    print('выбор1')
else:
    if area == 'чон арык' or area == 'байтик' or area == 'ортосай':
        counter2 += 1
    if walls == 'пескоблок' and plot <= 5:
        if price <= 45000:
            counter1 += 1
    if counter1 == 2:
        print('выбор2')
    else:
        print('дом с такими требованиями не найден!')
