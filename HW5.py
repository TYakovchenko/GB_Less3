sum = 0

try:
    while True:
        for i in map(int,input("Введите числа для суммы, \nДля выхода нажмите любую букву: ").split()):
            sum += i
        print(sum)
except ValueError:
     print("Вы завершили цикл. Итоговая сумма:", sum)