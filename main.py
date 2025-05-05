from distutils.command.clean import clean


class Numbers_Class:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def multiply(self):
        return self.value1*self.value2

    def devision(self):
        return self.value1/self.value2

    def addition(self):
        return self.value1+self.value2

    def subtraction(self):
        return self.value1-self.value2

    def get_list(self):
        return [self.value1 * self.value2, int(self.value1 / self.value2), int(self.value1 - self.value2), int(self.value1 + self.value2)]

num_class = Numbers_Class(4/8, 1/2)

print(num_class.get_list())



# value1 = celcia
# value2 = farengeit
class Graducnic:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def celtofar(self):
        return (self.value1*9/5)+32

    @staticmethod
    def fartocel(self):
        return (self.value2-32)*5/9



    def get_list(self):
        return [(self.value1*9/5)+32, (self.value2-32)*5/9]

num_class = Graducnic(0,  212)

print(num_class.get_list())

# value1 = metr
# value2 = mili
#Возможна погрешность
class Perevod:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def metrtomili(self):
        return self.value2/1609

    @staticmethod
    def militometr(self):
        return self.value1*1609

    def get_list(self):
        return [self.value2/1609, self.value1*1609]


num_class = Perevod(10, 212)

print(num_class.get_list())

# value1 = litr
# value2 = galon
#Возможна погрешность
class Perevod2:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def litrtogalon(self):
        return self.value1/3.785

    @staticmethod
    def galontolitr(self):
        return self.value2*3.785
    def get_list(self):
        return [self.value1/3.785, self.value2*3.785]


num_class = Perevod2(10, 10)

print(num_class.get_list())

