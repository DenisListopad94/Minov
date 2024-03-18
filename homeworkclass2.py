from abc import ABC, abstractmethod
"""
======================= 1 ЗАДАНИЕ ===============================
    Определить класс «Шахматная фигура» с ее координатами на шахматной доске, 
    ее цветом (черный или белый), виртуальным методом «битья» другой фигуры, 
    и унаследовать от него классы, соответствующие шахматным фигурам «Ферзь», «Пешка», «Конь». 
    Написать виртуальные методы «битья» другой фигуры, которые принимают координаты другой фигуры и определяют, 
    может ли данная  фигура «бить» фигуру с теми (принятыми) координатами.
"""


class Chess(ABC):
    def __init__(self, coord_x: int, coord_y: int, color: str):
        self.coord_x = coord_x
        while self.coord_x > 8 or self.coord_x < 1:
            self.coord_x = int(input("incorrect input of x coordinate, please try again:"))
        self.coord_y = coord_y
        while self.coord_y > 8 or self.coord_y < 1:
            self.coord_y = int(input("incorrect input of y coordinate, please try again:"))
        self.color = color
        while self.color != "white" and self.color != "black":
            self.color = input("incorrect input of color, please try again:")

    def what_color(self) -> str:
        return self.color

    @abstractmethod
    def can_attack(self, coord_x: int, coord_y: int, color: str) -> bool:
        pass


class Pawn(Chess):
    def can_attack(self, coord_x: int, coord_y: int, color: str) -> bool:
        while coord_x > 8 or coord_x < 1:
            coord_x = int(input("incorrect input of x coordinate, please try again:"))
        while coord_y > 8 or coord_y < 1:
            coord_y = int(input("incorrect input of y coordinate, please try again:"))
        while color != "white" and color != "black":
            color = input("incorrect input of color, please try again:")
        if color != self.color:
            if self.color == "white":
                if coord_x == self.coord_x + 1 and coord_y == self.coord_y + 1 or coord_y == self.coord_y - 1:
                    return True
                else:
                    return False
            else:
                if coord_x == self.coord_x - 1 and coord_y == self.coord_y + 1 or coord_y == self.coord_y - 1:
                    return True
                else:
                    return False
        else:
            return False


a = Pawn(int(input("x coordnate of pawn:")), int(input("y coordnate of pawn:")), input("color of pawn:"))
print(a.can_attack(int(input("x coordinate of attack:")), int(input("y coordinate of attack:")),
                   input("color of attacked figure:")))


class Knight(Chess):
    def can_attack(self, coord_x: int, coord_y: int, color: str) -> bool:
        while coord_x > 8 or coord_x < 1:
            coord_x = int(input("incorrect input of x coordinate, please try again:"))
        while coord_y > 8 or coord_y < 1:
            coord_y = int(input("incorrect input of y coordinate, please try again:"))
        while color != "white" and color != "black":
            color = input("incorrect input of color, please try again:")
        if color != self.color:
            if coord_x == self.coord_x + 1 or coord_x == self.coord_x - 1 \
                    and coord_y == self.coord_y + 2 or coord_y == self.coord_y - 2:
                return True
            elif coord_x == self.coord_x + 2 or coord_x == self.coord_x - 2 \
                    and coord_y == self.coord_y + 1 or coord_y == self.coord_y - 1:
                return True
            else:
                return False
        else:
            return False


b = Knight(int(input("x coordnate of knight:")), int(input("y coordnate of knight:")), input("color of knight:"))
print(b.can_attack(int(input("x coordinate of attack:")), int(input("y coordinate of attack:")),
                   input("color of attacked figure:")))


class Queen(Chess):

    def can_attack(self, coord_x: int, coord_y: int, color: str) -> bool:
        while coord_x > 8 or coord_x < 1:
            coord_x = int(input("incorrect input of x coordinate, please try again:"))
        while coord_y > 8 or coord_y < 1:
            coord_y = int(input("incorrect input of y coordinate, please try again:"))
        while color != "white" and color != "black":
            color = input("incorrect input of color, please try again:")
        if color != self.color:
            if coord_x == self.coord_x or coord_y == self.coord_y:
                return True
            elif abs(coord_x - self.coord_x) == abs(coord_y - self.coord_y):
                return True
            else:
                return False
        else:
            return False


c = Queen(int(input("x coordnate of queen:")), int(input("y coordnate of queen:")), input("color of queen:"))
print(c.can_attack(int(input("x coordinate of attack:")), int(input("y coordinate of attack:")),
                   input("color of attacked figure:")))
"""
======================= 2 ЗАДАНИЕ ===============================
    Создать базовый класс «Грузоперевозчик» и производные классы «Самолет», «Поезд», «Автомобиль». 
    Определить время и стоимость перевозки для указанных городов и расстояний
"""


class CargoCarier(ABC):
    def __init__(self, speed: int, cost_for_km: int):
        self.speed = speed
        self.cost_for_km = cost_for_km

    @abstractmethod
    def shipment(self, city: str, way: int) -> str:
        pass


class Plane(CargoCarier):
    def shipment(self, city: str, way: int) -> str:
        time = way / self.speed
        cost = way * self.cost_for_km
        return f"доставка займёт {time}ч и будет стоить {cost} руб."


class Train(CargoCarier):
    def shipment(self, city: str, way: int) -> str:
        if city == "Нью - Йорк":
            return "этот транспорт не может попасть в Нью - Йорк"
        else:
            time = way / self.speed
            cost = way * self.cost_for_km
            return f"доставка займёт {time} ч и будет стоить {cost} руб."


class Truck(CargoCarier):
    def shipment(self, city: str, way: int) -> str:
        if city == "Нью - Йорк":
            return "этот транспорт не может попасть в Нью - Йорк"
        else:
            time = way / self.speed
            cost = way * self.cost_for_km
            return f"доставка займёт {time} ч и будет стоить {cost} руб."


il_76 = Plane(int(input("введите скорость:")), int(input("введите стоимость перевозки:")))
print(il_76.shipment(input("введите место доставки:"), int(input("введите расстояние:"))))

iveko = Truck(int(input("введите скорость:")), int(input("введите стоимость перевозки:")))
print(iveko.shipment(input("введите место доставки:"), int(input("введите расстояние:"))))

roco_73792 = Train(int(input("введите скорость:")), int(input("введите стоимость перевозки:")))
print(iveko.shipment(input("введите место доставки:"), int(input("введите расстояние:"))))
"""
======================= 3 ЗАДАНИЕ ===============================
    Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение». 
    Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет. 
    Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды. 
    Напишите виртуальные методы поедания и определения состояния живого существа (живой или нет, 
    в зависимости от достижения предельного возраста и наличия еды (входной параметр)).
"""


class Living(ABC):
    @abstractmethod
    def eating(self, args) -> str:
        pass

    @abstractmethod
    def is_alive(self, agrs) -> str:
        pass


class Plant(Living):
    def __init__(self, age: int):
        self.life_limit = 100
        self.age = age

    def eating(self, is_sun_avalibe: str) -> str:
        if is_sun_avalibe == "да":
            return "Еда есть!"
        elif is_sun_avalibe == "нет":
            return "Еды нет!"

    def is_alive(self, is_sun_avalible: str) -> str:
        if self.eating(is_sun_avalible) == "Еда есть!" and self.age <= self.life_limit:
            return "Растение живо!"
        else:
            return "Растение мертво!"


grass = Plant(int(input("введите возраст растения:")))
is_sun_avalible = input("ecть ли солнце:")
if grass.is_alive(is_sun_avalible) == "Растение живо!":
    is_plant_avalible = "да"
elif grass.is_alive(is_sun_avalible) == "Растение мертво!":
    is_plant_avalible = "нет"
print(grass.is_alive(is_sun_avalible))


class Rabbit(Living):
    def __init__(self, age: int):
        self.life_limit = 9
        self.age = age

    def eating(self, is_plant_avalibe: str) -> str:
        if is_plant_avalibe == "да":
            return "Еда есть!"
        elif is_plant_avalibe == "нет":
            return "Еды нет!"

    def is_alive(self, is_plant_avalible: str) -> str:
        if self.eating(is_plant_avalible) == "Еда есть!" and self.age <= self.life_limit:
            return "Кролик жив!"
        else:
            return "Кролик мертв!"


gray = Rabbit(int(input("введите возраст кролика:")))
if gray.is_alive(is_plant_avalible) == "Кролик жив!":
    is_rabbit_avalible = "да"
elif gray.is_alive(is_plant_avalible) == "Кролик мертв!":
    is_rabbit_avalible = "нет"
print(gray.is_alive(is_plant_avalible))


class Fox(Living):

    def __init__(self, age: int):
        self.life_limit = 4
        self.age = age

    def eating(self, is_rabbit_avalible: str) -> str:
        if is_rabbit_avalible == "да":
            return "Еда есть!"
        elif is_rabbit_avalible == "нет":
            return "Еды нет!"

    def is_alive(self, is_rabbit_avalible: str) -> str:
        if self.eating(is_rabbit_avalible) == "Еда есть!" and self.age <= self.life_limit:
            return "Лиса жива!"
        else:
            return "Лиса мертва!"


red = Fox(int(input("введите возраст лисы:")))
print(red.is_alive(is_rabbit_avalible))
