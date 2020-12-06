#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input("Напишите свое имя ")
surname = input("Напишите свою фамилию ")
year = int(input("Укажите год своего рождения "))
city = input("Укажите город, в котором вы живете ")
email = input("Укажите свою электронную почту ")
phone = int(input("Оставьте свой номер телефона "))
##while str(phone) != 10:
#    print("neverno vvedite ewe raz", input"Введите еще раз")
##print("Вы ввели","Имя:", name, "Фамилия:", surname, "Год рождения:", year, "город проживания", city,"Контактные данные:", email,phone)

def my_func(name, surname, year, city, email, phone):
    return [name, surname, year, city, email, phone]
print(my_func(surname, name, year, city, email, phone))