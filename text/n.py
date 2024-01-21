import re

txt = "The rain in Spain"
x = re.findall("^The +\S", txt)
print(x)