

class Human:

    def __init__(self, v_name='Name'):
        self.__head = 1
        self.__hands = 2
        self.__feet = 2
        self.__age = 10
        self.name = v_name

    @classmethod
    def check_type(cls, x):
        return type(x) in (int, float)

    def get_age(self):
        return self.__age

    def set_age(self, v_age):
        if self.check_type(v_age):
            self.__age = v_age




o_petya = Human('Petya')
print(o_petya.get_age())
o_petya.set_age(25)
print(o_petya.get_age())