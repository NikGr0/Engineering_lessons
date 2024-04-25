

class Mammals:

    def __init__(self):
        self.head = 1
        self.hands = 2
        self.feet = 2
        self.age = 0
        self.sex = 1
        #self.name = 'Имя'

    def see_info(self):
        print(f'Head = {str(self.head)}')
        print(f'Hands = {str(self.hands)}')
        print(f'Feet = {str(self.feet)}')
        print(f'Age = {str(self.age)}')
        print(f'Sex = {str(self.sex)}')

class Human(Mammals):
    def __init__(self, age, sex, v_name='Имя'):
        super().__init__()
        self.age = age
        self.sex = sex
        self.name = v_name

    def see_info(self):
        super().see_info()
        print(f'Name = {str(self.name)}')

class Bus:

    def __init__(self):
        self.places = []
        self.coord = 0

    def hum_app(self, l):
        #self.places.append(l)
        self.places.extend(l)

    def hum_del(self, l):
       self.places.remove(l)

    def see_info(self):
        print(f'В автобусе: {self.places}')



scool_bus = Bus()
scool_bus.hum_app(['Ваня', 'Гоша'])
scool_bus.hum_app(['Оля'])
scool_bus.see_info()
scool_bus.hum_del('Оля')
scool_bus.see_info()

# Bus().hum_app(['Ваня', 'Гоша'])
# Bus.see_info()
# h_petya = Human(25, 0, 'Петя')
# h_petya.see_info()

# a1 = Mammals()
# a1.see_info()