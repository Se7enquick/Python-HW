import sys
numbers = []
out = ''
with open('numbers.txt', 'r') as f:
    items = f.read().split('\n')
    for i in items:
        numbers.append([int(n) for n in i.split(',')])

with open('result.txt', 'w+') as r:
    for nums in numbers:
        for num in range(1, nums[2]+1):
            if num % nums[0] == 0 and num % nums[1] == 0:
                out += 'FB' + ' '
            elif num % nums[0] == 0:
                out += 'F' + ' '
            elif num % nums[1] == 0:
                out += 'B' + ' '
            else:
                out += str(num) + ' '
        out += '\n'
with open('output.txt', 'w') as output:
    output.write(str(out))
    output.close()    