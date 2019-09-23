'''def lower(a):   #ex 1
    return a.lower()
def upper(b):
    return b.upper()
list1 = ['LOWER']
list2 = ['upper']
result1 = list(map(lower, list1))
result2 = list(map(upper, list2))
print(result1, result2)

def square(num):   #ex 2
    for x in range (2, num):
        if num % x == 0:
            return '.'
    return num ** 2
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
square_nums = list(map(square, numbers))
print(square_nums)


file = open('file.txt', 'r')
f = file.read()
def count_word(word):
    if word in total_count:
        total_count[word] += 1
    else:
        total_count[word] = 1
total_count = {}
list(map(lambda x: count_word(''.join(filter(str.isalpha, x.lower()))), f.split()))
print(total_count)
