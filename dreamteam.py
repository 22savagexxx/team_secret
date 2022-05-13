# #
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.

# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.

class Soldier:
    def __init__(self, fire='тиги-тигитиш'):
        self.fire = fire
    def fire(self):
        return (f'{self.fire}')
    def fire1(self):
        return 'пиу-пиу'

    def gun_fire(self):
        b = 5
        while True:
            a = input()
            print(b)
            if a == 'r' and b > 0:
                print(Soldier1.fire1())
                b = b - 1
            elif a == 'r' and b <= 0:

                print('Перезарядка')
                b = 5
            else:
                    print('ERROR')

class Act_of_Shooting(Soldier):
    pass

Soldier1 = Soldier()
print('r = fire')
# print(Soldier1.gun_fire())

c = Act_of_Shooting
print(c.gun_fire(self=Soldier))

# # 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
                 return'Мебель:% s Занятая площадь:% .2f '% (self.name, self.area)

class House:
    def __init__(self, house_type, area=300):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.furniture_list = []

    def __str__(self):
                 return f'{self.house_type},{self.area},{self.free_area},{self.furniture_list}'

    def add_furniture(self,furniture):

        print('Добавить мебель% s площадь:% .2f '% (имя.Мебель, площадь.покрытия))
        if self.free_area < furniture.area:
            print('Площадь мебели% s превышает оставшуюся площадь '% Furniture.name)
            return
        self.furniture_list.append(furniture.name)
        self.free_area-=furniture.area


type_house= House('Тип-Кирпичный',300)
bed = Furniture('bed',7)
table = Furniture('table',5)
cabinet = Furniture('cabinet',3)

print (bed)
print (table)
print (cabinet)
print(type_house)

my_house = Furniture('Общая площадь',200)
print (my_house)


# # 3 
# Students room:
# Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Person:
    def __init__(self,name,age,less):
        self.name = name
        self.age = age
        self.less = less


steve = Person('Steven Schultz', 23, 'English')
johnny = Person(' Jonathan Rosenberg',24,'Biology')
penny = Person('Penelope Meramveliotakis',21,'Physics')
print(('name:',steve.name,'age:',steve.age,'major:',steve.less))
print(('name:',johnny.name,'age:',johnny.age,'major:',johnny.less))
print(('name:',penny.name,'age:',penny.age,'major:',penny.less))


# # 4 
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:

# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()

# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567) 
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3


class MoneyFmt:
    def __init__(self, dollarize = 123456.78901, dollarize1 = -123456.7801):
        self.dollarize = dollarize
        self.dollarize1 = dollarize1


    def dollarize2(self):
        return f'{("{:,.2f}".format(self.dollarize))}, {("{:,.2f}".format(self.dollarize1))}'

    def update(self, dollarize):
        self.dollarize = dollarize
        

d = MoneyFmt(dollarize=123456.78901, dollarize1=-123456.7801)
o = d.dollarize2()
print(o)
print(type(o))
d.update(132123425)
print(d.__dict__)


# # 5  
# Deck of Cards:
# Создайте класс колоды карт. Внутри колода карт должна использовать другой класс - класс карт. Ваши требования:
# Класс Deck должен иметь метод раздачи для раздачи одной карты из колоды.
# После раздачи карты она удаляется из колоды.
# Должен быть метод «смешивания», который проверяет, что в колоде есть все 52 карты, а затем меняет их случайным образом.
# Класс должен иметь масть (червы, бубны, трефы, пики) и ценность карты (A, 2,3,4,5,6,7,8,9,10, J, Q, K)
# ПРИМЕЧАНИЕ: используйте случайное перемешивание

# Copy
# from random import shuffle



# # 6 
# Спарсить сайт лалафо с недвижимостью (аренда посуточно)
# https://lalafo.kg/kyrgyzstan/nedvizhimost
# Название 
# Цену
# Фото
# Адрес
# Дату
# Ссылку на пост

# Данные отдать в csv

