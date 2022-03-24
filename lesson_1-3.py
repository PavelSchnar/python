# Задание 1

# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('введи промежуток времени'))

if duration < 60:
    print(f'{duration} сек')

elif (duration >= 60) and (duration < 86400):
    hour = duration // 3600
    minute = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(f'{hour} час, {minute} мин, {sec} сек')

else:
    days = duration // 86400
    hour = (duration // 3600) % 24
    minute = (duration % 3600) // 60
    sec = (duration % 3600) % 60
    print(f'{days}дн {hour}час, {minute} мин, {sec}сек')

# Задание 2
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.



arr = [i ** 3 for i in range(1, 1000, 2)]
print(arr)
arr1 = []
summ = int
for i in arr:
    a = i % 10
    b = i // 10 % 10
    c = i // 10 // 10 % 10
    d = i // 10 // 10 // 10 % 10
    e = i // 10 // 10 // 10 // 10 % 10
    f = i // 10 // 10 // 10 // 10 // 10 % 10
    g = i // 10 // 10 // 10 // 10 // 10 // 10 % 10
    h = i // 10 // 10 // 10 // 10 // 10 // 10 // 10 % 10
    i = i // 10 // 10 // 10 // 10 // 10 // 10 // 10 // 10 % 10
    summ = a + b + c + d + e + f + g + h + i

    if summ % 7 == 0:
        arr1.append(summ)
print(sum(arr1))

arr2 = [(i ** 3 + 17) for i in range(1, 1000, 2)]
print(arr2)
arr3 = []
for i in arr2:
    a = i % 10
    b = i // 10 % 10
    c = i // 10 // 10 % 10
    d = i // 10 // 10 // 10 % 10
    e = i // 10 // 10 // 10 // 10 % 10
    f = i // 10 // 10 // 10 // 10 // 10 % 10
    g = i // 10 // 10 // 10 // 10 // 10 // 10 % 10
    h = i // 10 // 10 // 10 // 10 // 10 // 10 // 10 % 10
    i = i // 10 // 10 // 10 // 10 // 10 // 10 // 10 // 10 % 10
    summ = a + b + c + d + e + f + g + h + i
    if summ % 7 == 0:
        arr3.append(summ)
print(sum(arr3))

# Задание №3
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
numbs = []
for i in range(100):
    i = i + 1
    if i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 < 5:
        print(i, "процента")
    else:
        print(i, "процентов")