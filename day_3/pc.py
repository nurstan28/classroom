print('Выберите характеристики ноутбука')

if 4 <= int(input('Размер ОЗУ:')) <= 8:
    if str(input('Выберите вид накопителя ssd или hdd:')) == 'ssd':
        if int(input('Размер накопителя ssd в гигабайтах:')) >= 256:
            if int(input('Стоимость:')) <= 1000 and str(input('Состояние: новый или старый:')) == 'новый':
                print('ноутбук в наличии')
    else:
        if int(input('Размер накопителя hdd в террабайтах:')) >= 1:
            if int(input('Стоимость:')) <= 100 and str(input('Состояние: новый или старый:')) == 'новый':
                print('ноутбук в наличии')
            else:
                print('ноутбука нет в наличии')
