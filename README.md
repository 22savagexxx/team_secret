# team_secret
# 2 
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.
'''
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
'''
#Реализуйте студенческую комнату с помощью ООП:

# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>
'''class Person:
    def __init__(self,name,age,less):
        self.name = name
        self.age = age
        self.less = less


steve = Person('Steven Schultz', 23, 'English')
johnny = Person(' Jonathan Rosenberg',24,'Biology')
penny = Person('Penelope Meramveliotakis',21,'Physics')
print(('name:',steve.name,'age:',steve.age,'major:',steve.less))
print(('name:',johnny.name,'age:',johnny.age,'major:',johnny.less))
print(('name:',penny.name,'age:',penny.age,'major:',penny.less))'''
