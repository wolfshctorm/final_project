from ast import literal_eval
from distutils.command.clean import clean

# value1 знаментаель первой дроби
# value2 числотель перовй дробм
# value12 знаменатель второй дроби
# value22 чсилитель второй дроби
class Fraction:
    def __init__(self, value1, value2, value12, value22, float1, float2):
        self.value1 = value1
        self.value2 = value2
        self.value12 = value12
        self.value22 = value22
        self.float1 = float1
        self.float2 = float2

    def get_float1(self, float1):
        self.float1 = self.value1/self.value2
        return float1

    def get_float2(self, float2):
        self.float2 = self.value12/self.value22
        return float2

    def multiply(self):
        return self.float1*self.float2

    def devision(self):
        return self.float1/self.float2

    def addition(self):
        return self.float1+self.float2

    def subtraction(self):
        return self.float1-self.float2

    def get_list_multiply(self):
        return (f'Результат умножения: {self.float1*self.float2}')

    def get_list_devision(self):
        return (f'Результат деления: {self.float1/self.float2}')

    def get_list_addition(self):
        return (f'Результат сложения: {self.float1+self.float2}')

    def get_list_subtraction(self):
        return (f'Результат вычитания: {self.float1-self.float2}')


# value3 = celcia
# value4 = farengeit
class Graducnic:
    def __init__(self, value3, value4):
        self.value3 = value3
        self.value4 = value4

    @staticmethod
    def celtofar(self):
        return (self.value3*9/5)+32

    @staticmethod
    def fartocel(self):
        return (self.value4-32)*5/9

    def get_list1(self):
        return (f'Цельсия в фаренгейты: {(self.value3*9/5)+32}')
    def get_list2(self):
        return (f'Фаренгейты в цельсия: {(self.value4-32)*5/9}')

# value5 = metr
# value6 = mili
#Возможна погрешность
class Perevod:
    def __init__(self, value5, value6):
        self.value5 = value5
        self.value6 = value6

    @staticmethod
    def metrtomili(self):
        return self.value6/1609

    @staticmethod
    def militometr(self):
        return self.value5*1609

    def get_list1(self):
        return (f'Метры в мили: {self.value5/1609}')
    def get_list2(self):
        return (f'Мили в метры: {self.value6*1609}')

# value7 = litr
# value8 = galon
#Возможна погрешность
class Perevod2:
    def __init__(self, value7, value8):
        self.value7 = value7
        self.value8 = value8

    @staticmethod
    def litrtogalon(self):
        return self.value7/3.785

    @staticmethod
    def galontolitr(self):
        return self.value8*3.785
    def get_list1(self):
        return (f'Галоны в литры: {self.value8*3.785}')
    def get_list2(self):
        return (f'Литры в галоны: {self.value7/3.785}')

# Интерфейс
print('Выберете действие:\n1-Работа с дробями\n2-Перевод из цельсий в фаренгейты и наоборот\n3-Перевод из миль в метры и наоборот\n4-Перевод из галонов в литры и наоборот')
action_choice = input('Ваш выбор(напишите цифру):')
if '1' in action_choice:
    print('Вы выбрали работа с дробями!\nВыберите действие:\n1-Умножение\n2-Деление\n3-Сложение\n4-Вычитание')
    action_choice5 = input('Ваш выбор(напишите цифру):')

    if '1' in action_choice5:
        fraction1 = int(input('Знаменатель первой дроби:'))
        fraction2 = int(input('Числитель первой дроби:'))
        fraction3 = int(input('Знаменатель второй дроби:'))
        fraction4 = int(input('Числитель второй дроби:'))
        num_class = Fraction(fraction1, fraction2, fraction3, fraction4, float1=fraction1/fraction2, float2=fraction3/fraction4)
        print(num_class.get_list_multiply())
    if '2' in action_choice5:
        fraction1 = int(input('Знаменатель первой дроби:'))
        fraction2 = int(input('Числитель первой дроби:'))
        fraction3 = int(input('Знаменатель второй дроби:'))
        fraction4 = int(input('Числитель второй дроби:'))
        num_class = Fraction(fraction1, fraction2, fraction3, fraction4, float1=fraction1/fraction2, float2=fraction3/fraction4)
        print(num_class.get_list_devision())
    if '3' in action_choice5:
        fraction1 = int(input('Знаменатель первой дроби:'))
        fraction2 = int(input('Числитель первой дроби:'))
        fraction3 = int(input('Знаменатель второй дроби:'))
        fraction4 = int(input('Числитель второй дроби:'))
        num_class = Fraction(fraction1, fraction2, fraction3, fraction4, float1=fraction1/fraction2, float2=fraction3/fraction4)
        print(num_class.get_list_addition())
    if '4' in action_choice5:
        fraction1 = int(input('Знаменатель первой дроби:'))
        fraction2 = int(input('Числитель первой дроби:'))
        fraction3 = int(input('Знаменатель второй дроби:'))
        fraction4 = int(input('Числитель второй дроби:'))
        num_class = Fraction(fraction1, fraction2, fraction3, fraction4, float1=fraction1/fraction2, float2=fraction3/fraction4)
        print(num_class.get_list_subtraction())
if '2' in action_choice:
    print('Перевод из фаренгейты в цельсия и наоборот!\nВыбирите действие:\n1-Цельсия в фаренгейты\n2-Фаренгейты в цельсия')
    action_choice4 = input('Ваш выбор(напишите цифру):')
    if '1' in action_choice4:
        print('Вы выбрали перевод из цельсия в фаренгейты!\nВведите данные:')
        celcia = int(input('Цельсия:'))
        farengeit = None
        num_class = Graducnic(celcia, farengeit)
        print(num_class.get_list1())
    if '2' in action_choice4:
        print('Вы выбрали перевод из фарегнейтов в цельсия!\nВведите данные:')
        celcia = None
        farengeit = int(input('Фаренгейты:'))
        num_class = Graducnic(celcia, farengeit)
        print(num_class.get_list2())
if '3' in action_choice:
    print('Перевод из мили в метры и наоборот!\nВыбирите действие:\n1-Метры в мили\n2-Мили в метры')
    action_choice3 = input('Ваш выбор(напишите цифру):')
    if '1' in action_choice3:
        print('Вы выбрали перевод из метров в мили!\nВведите данные:')
        mili = None
        metr = int(input('Метры:'))
        num_class = Perevod(metr, mili)
        print(num_class.get_list1())
    if '2' in action_choice3:
        print('Вы выбрали перевод из милей в метры!\nВведите данные:')
        mili = int(input('Мили:'))
        metr = None
        num_class = Perevod(metr, mili)
        print(num_class.get_list2())
if '4' in action_choice:
    print('Перевод из галонов в литры и наоборот!\nВыбирите действие:\n1-Галоны в литры\n2-Литры в галоны')
    action_choice2 = input('Ваш выбор(напишите цифру):')
    if '1' in action_choice2:
        print('Вы выбрали перевод из галонов в литры!\nВведите данные:')
        galon = int(input('Галоны:'))
        litr = None
        num_class = Perevod2(litr, galon)
        print(num_class.get_list1())
    if '2' in action_choice2:
        print('Вы выбрали перевод из литров в галоны!\nВведите данные:')
        litr = int(input('Литры:'))
        galon = None
        num_class = Perevod2(litr, galon)
        print(num_class.get_list2())
