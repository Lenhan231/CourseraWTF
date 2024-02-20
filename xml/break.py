import xml.etree.ElementTree as et
class Food:
    def __init__(self, name, price, des, calo):
        self.__name == name
        self.__price == price
        self.__description == des
        self.__calories == calo
    
    def __str__(self):
        return f'Food[name = {self.__name}, price = {self.__price}, description = {self.__price}, calo = {self.__calories},'\
               f'desc = {self.__description}, calo = {self.__cal}'
    @property
    def price(self):
        return self.__price
    @property
    def calo(self):
        return self.__calories
def parse_xml(file_name):
    tree = et.parse(file_name)
    root = tree.getroot()
    food_list = []
    for food in root.findall('food'):
        name = food.find('name').text
        price = food.find('price').text
        des = food.find('description').text
        calo = food.find('calories').text
        food_list.append(Food(name, price, des, calo))
    return food_list