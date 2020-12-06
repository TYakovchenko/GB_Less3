#3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

#Первый вариант
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print("Первый вариант реализации:")
arg1 = int(input("Первое значение: "))
arg2 = int(input("Второе значение: "))
arg3 = int(input("Третье значение: "))

print(my_func(arg1, arg2, arg3))


##Второй вариант
def my_func2(arg4, arg5, arg6):
    range_1 = [arg4, arg5, arg6]
    total = []
    max_1 = max(range_1)
    total.append(max_1)
    range_1.remove(max_1)
    max_2 = max(range_1)
    total.append(max_2)
    print(sum(total))

print("Второй вариант реализации:")
my_func2(arg4 = int(input("Первое значение: ")), arg5 = int(input("Второе значение: ")),arg6 = int(input("Третье значение: ")))
