import xml.etree.ElementTree as ET
class food:
    def __init__(self, name, price, description, calories):
        self.name = name
        self.price = price
        self.decription = description
        self.calories = calories
    
    def hienthi(self):
        print(f'{self.name}\t{self.price}\t{self.decription}\t{self.calories}')


file_path = r'D:\CourseraWTF\xml\Breakfast.xml'
with open(file_path, 'r') as data:
    sub = []
    tree = ET.fromstring(data.read())
    for a in tree.findall('food'): 
        sub.append(food(a.find('name').text, a.find('price').text, a.find('description').text, a.find('calories').text))
    for i in range(len(sub)):
        sub[i].hienthi()