import re
fhandler= open("regex_sum_42.txt", 'r')
sum = 0
for line in fhandler:
    x = re.findall('[0-9]+', line)
    for i in x:
        sum += int(i)
print(sum)