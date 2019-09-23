while True: 
    a = int(input('Введите число fizz: '))
    b = int(input('Введите число buzz: '))
    c = int(input('Введите число, до которого нужно считать: '))

    for num in range(1, c+1):
        if num % a == 0 and num % b == 0:
            print('FB', end = ' ')
        elif num % a == 0:
            print('F', end = ' ')
        elif num % b == 0:
            print('B', end = ' ')
        else:
            print(num, end = ' ')
        
    d = int(input('\n''Еще раз? 1 - да 0 - нет: '))
    if d == 1: continue
    if d == 0: break
