# Нечетный
from operator import contains

# Напишите программу, которая выводит числа от 1 до 100,
# пропуская четные числа.
# Используйте цикл while и оператор continue для пропуска
# четных чисел.

# Напишите тут ваш код
count = 0
while count < 100:
    count += 1
    if count % 2 == 0:
        continue
    print(count)