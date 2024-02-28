import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = x.split('')
z = y[1].split('@')
print(z[1])    