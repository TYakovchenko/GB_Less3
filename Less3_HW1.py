#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div():
    try:
        arg1 = int(input("введите числитель "))
        arg2 = int(input("введите знаменатель "))
        answer = arg1 / arg2
    except ValueError:
        return 'Числитель и знаменатель должны быть записаны арабскими цифрами'
    except ZeroDivisionError:
        return "Нельзя делить на ноль"

    return answer

print('Результат', div())