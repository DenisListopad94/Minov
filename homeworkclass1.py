"""
======================= 1 ЗАДАНИЕ ===============================
    Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
    Добавить функцию, которая находит сумму значений этих переменных,
    и функцию которая находит наибольшее значение из этих двух переменных.
"""
class Some:
    def __init__(self, some_value: int, another_value: int):
        self.some_value = some_value
        self.another_value = another_value

    def output(self):
        print(self.some_value, self.another_value)

    def some_change(self, change):
        self.some_value = change

    def another_change(self, change):
        self.another_value = change

    def summ(self):
        print(self.some_value + self.another_value)

    def bigger(self):
        if self.some_value > self.another_value:
            print(self.some_value)
        else:
            print(self.another_value)


der = Some(int(input("1 зачение:")), int(input("2 значение")))

der.output()
der.some_change(int(input("введите новое 1 зачение:")))
der.another_change(int(input("введите новое 2 зачение:")))
der.output()
der.summ()
der.bigger()
"""
======================= 2 ЗАДАНИЕ ===============================
    Описать класс, реализующий десятичный счетчик, 
    который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне. 
    Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями. 
    Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние. 
    Написать программу, демонстрирующую все возможности класса.
"""
class Counter:
    def __init__(self, min, max=10, current=0):
        self.min = min
        self.max = max
        self.current = current
        if self.current < self.max:
            self.current = self.min
        elif self.current > self.max:
            self.current = self.max
            
    def increase(self):
        if self.current < self.max:
            self.current += 1
        else:
            print("already on max")

    def decrease(self):
        if self.current > self.min:
            self.current -= 1
        else:
            print("alredy on min")

    def current_value(self):
        print(self.current)


der = Counter(int(input("min value:")), int(input("max value:")), int(input("current value")))
der.current_value()
der.increase()
der.current_value()
der.decrease()
der.current_value()
"""
======================= 3 ЗАДАНИЕ ===============================
    Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов, 
    поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
"""
class Shop:
    def __init__(self, assort=None):
        if assort is None:
            assort = {}
        self.assort = assort

    def find_good(self, key):
        if key in self.assort:
            print(f"на скаде этого товара:{self.assort[key][1]}, по цене {self.assort[key][0]} за штуку")
        else:
            print("нет такого товара")

    def add_good(self, key, price, quantity):
        self.assort[key] = (price, quantity)

    def remove_good(self, key):
        del self.assort[key]


romashka = Shop({})
romashka.add_good(input("введите название товара:"), int(input("цена:")), int(input("количество")))
romashka.add_good(input("введите название товара:"), int(input("цена:")), int(input("количество")))
romashka.find_good(input("введите название товара:"))
romashka.remove_good(input("введите название товара:"))
"""
======================= 4 ЗАДАНИЕ ===============================
    Реализуйте класс MoneyBox, для работы с виртуальной копилкой. 
    Каждая копилка имеет ограниченную вместимость, 
    которая выражается целым числом – количеством монет(capacity -вместимость), 
    которые можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, 
    предоставлять возможность добавлять монеты в копилку и узнавать, 
    можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость. 
Класс должен иметь следующий вид:
class MoneyBox: 
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки 
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.

"""
class MoneyBox:
    def __init__(self, capacity: int, current=0):
        self.capaity = capacity
        self.current = current

    def can_add(self, coins: int) -> bool:
        return self.capaity - self.current >= coins

    def add(self, add_coins: int):
        if self.can_add(add_coins):
            self.current += add_coins


pig = MoneyBox(int(input("введите вмесимоть копилки:")))
pig.add(int(input("введите количество монет:")))
print(pig.can_add(int(input("введите количество монет:"))))
