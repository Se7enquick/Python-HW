s = 'abc'
t = (10, 20, 30)
def shortest_sequence_range(*args):
        return range(len(sorted(args, key=len)[0]))
g = ((s[i], t[i])
         for i in shortest_sequence_range(s,t) )
for item in g:
        print(item)