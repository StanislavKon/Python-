
# # Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# # проверяет, является ли этот день выходным.

day_number = int(input('Введите число, обозначающую день недели (от 1 до 7 включительно): '))
if day_number == 6 or day_number == 7:
    print(f'День недели {day_number} -> выходной день')
elif 1 <= day_number <= 5:
    print(f'День недели {day_number} -> рабочий день')
else:
     print('Введено значение вне заданного диапозона')
       
    