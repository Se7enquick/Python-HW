"""x = 0
while x < 100:
    x += 1
    if x % 2 == 0:
        print(x)"""

"""a = [10, 20, 30, 40]
for number, item in enumerate(a):
    a[number] = item + 5
print(a)"""

import sys
import operator
file = sys.argv[1]
f = open('dictionary.txt', 'r')
d = {}
for line in f:
    for symbol in line:
        if symbol not in d:
            d[symbol] = 1
        else:
            d[symbol] += 1
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
list_d
for i in list_d:
    print(i[0], ':', i[1])






    

        