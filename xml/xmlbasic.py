import xml.etree.ElementTree as ET

data1 = '''
<breakfast_menu>
    <food>
        <name x = '1'>Belgian Waffles</name>
        <price>$5.95</price>
        <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
        <calories>650</calories>
    </food>
    <food>
        <name x='1'>Strawberry Belgian Waffles</name>
        <price>$7.95</price>
        <description>Light Belgian waffles covered with strawberries and whipped cream</description>
        <calories>900</calories>
    </food>
    <food>
        <name x='1'>Berry-Berry Belgian Waffles</name>
        <price>$8.95</price>
        <description>Light Belgian waffles covered with an assortment of fresh berries and whipped cream</description>
        <calories>900</calories>
    </food>
    <food>
        <name x='1'>French Toast</name>
        <price>$4.50</price>
        <description>Thick slices made from our homemade sourdough bread</description>
        <calories>600</calories>
    </food>
    <food>
        <name x='yes'>Homestyle Breakfast</name>
        <price>$6.95</price>
        <description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description>
        <calories>950</calories>
    </food>
</breakfast_menu>
'''

#data2 = r'D:\CourseraWTF\xml\Breakfast.xml'
#tree = ET.parse(data2)
#print(tree)'''
#data2 = r'D:\CourseraWTF\xml\Breakfast.xml

tree = ET.fromstring(data1)
# Find all 'food' elements and print the value of the 'x' attribute for each 'name' element within them
for food in tree.findall('food'): 
    name = food.find('price')
    print(name.text)