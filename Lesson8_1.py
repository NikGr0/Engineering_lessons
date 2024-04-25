
# класс человек
class Human:
    name: str
    __rota: str
    __polk: str

    def __init__(self, v_name='Ivan'):
        self.name = v_name
        self.__rota = 'Ne sostoit'
        self.__polk = 'Ne sostoit'

    def get_name(self):
        return self.name

    def set_rota(self, v_rota):
        self.__rota = v_rota

    def remove_is_rota(self):
        self.__rota = 'Ne sostoit'

    def get_rota(self):
        return self.name + ': ' + self.__rota

    def set_polk(self, v_polk):
        self.__polk = v_polk

    def remove_is_polk(self):
        self.__polk = 'Ne sostoit'

    def get_polk(self):
        return self.__polk

    def print_all_inf(self):
        return self.name + ': ' + self.__rota + ' '+ self.__polk


class Rota:
    name_rota: str
    __name_polk: str
    __rota: list()

    def __init__(self, v_name_rota='1 rota'):
        self.name_rota = v_name_rota
        self.__name_polk = 'Ne sostoit'
        self.__rota = list()

    def add_polk(self, v_name_polk: str):
        self.__name_polk = v_name_polk

    def get_rota(self):
        return self.__rota

    def add_rota(self, rota: list):
        for one_sold in rota:
            one_sold.set_rota(self.name_rota)
        self.__rota = self.__rota + rota

    def remove_rota(self, rota: list):
        for one_sold in rota:
            if one_sold in self.__rota:
                self.__rota.remove(one_sold)
                one_sold.remove_is_rota()
                one_sold.remove_is_polk()

    def print_all_rota(self):
        for one_sold in self.__rota:
            print(one_sold.get_rota(), one_sold.get_polk())



class Polk:
    name_polk: str
    __polk: list

    def __init__(self, v_name_polk='1 polk'):
        self.name_polk = v_name_polk
        self.__polk = list()

    def add_rota_v_polk(self, rota: str):
        rota.add_polk(self.name_polk)
        for one_sold in rota.get_rota():
            one_sold.set_polk(self.name_polk)




o_ivan = Human()
# o_ivan.set_rota('1 rota')
# o_ivan.set_polk('10 polk')
o_igor = Human('Igor')
# print(o_ivan.get_rota())
# print(o_ivan.get_polk())

one_rota = Rota('1 Rota')
two_rota = Rota('2 Rota')
five_polk = Polk('5 Polk')
one_rota.add_rota([o_ivan, o_igor])

five_polk.add_rota_v_polk(one_rota)
#one_rota.add_polk(five_polk)
one_rota.print_all_rota()
# print()
#o_ivan.get_rota()
one_rota.remove_rota([o_ivan])
# print('---------')
print(o_ivan.print_all_inf())
print('---------')
one_rota.print_all_rota()