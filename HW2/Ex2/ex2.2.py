#Cделать калькулятор, который может делать такие операции: +, -, *, / .
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = input('Введите операцию(+,-,*,/): ')

if z == '+':
    print('Результат: ',x + y)
if z == '-':
    print('Результат: ',x - y)
if z == '*':
    print('Результат:',x * y)
if z == '/':
    print('Результат:',x / y)