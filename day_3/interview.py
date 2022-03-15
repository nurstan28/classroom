language1 = "python"
language2 = "java"
language3 = "javascript"

language11 = str(input('Язык программирования python, java, javascript:'))
age12 = int(input('Возраст:'))
experience = int(input('Опыт:'))
salary = int(input('Желаемая заработная плата:'))
counter = 0
if language11 == language1 or language11 == language2 or language11 == language3:
    counter += 1
    print('критерий 1 подходит')
    if 18 <= age12 <= 65:
        counter += 1
        print('критерий 2 подходит')
    else:
        print('критерий 2 не подходит')
    if experience >= 3:
        counter += 1
        print('критерий 3 подходит')
    else:
        print('критерий 3 не подходит')
    if salary <= 60000:
        counter += 1
        print('критерий 4 подходит')
    else:
        print('критерий 4 не подходит')
else:
    print('кандидат не подходит')

if counter == 4:
    print('кандидат подходит')
else:
    print('кандидат не подходит')
