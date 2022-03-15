k = int(input('вместимость скороводки:'))
m = int(input('минуты:'))
n = int(input('кол-во котлет:'))

if n <= k:
    t = 2 * m
elif n * 2 % k == 0:
    t = m * (n * 2 // k)
else:
    t = m * (1 + (n * 2 // k))
print(t)
