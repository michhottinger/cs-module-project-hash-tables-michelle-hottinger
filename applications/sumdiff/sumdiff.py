"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

cache = {}
sumcache = {}

def f(x):
    
    for i in q:
        cache[i] = f(i)
    
    return x * 4 + 6


#grouped set: left and right side
{(f(a), f(b)): sum} {(sumf(a)+f(b): (f(a), f(b)))}
f(a) + F(b)   F(c) - F(d)
iterate through q
# Your code here

list1 = f.a + f.b
list2 = f.c - f.d
list1 == list2

leftside = {}#addition
rightside = {}#subtraction with i[1] - i[0]



z = list(itertools.combination(q, 2))

rightside = {}
leftside = {}

for x in q:
    if f(x) + f(x) not in leftside:
        leftside[(f(x) + f(x))] = list(x, x)

for i in z:
    #need to include the sum of fi and fi
    numsum = f(i[0]) + f(i[1])
    if numsum not in leftside:
        leftside[numsum] = []
    leftside[numsum].append(i)
    
    negsum = f(i[1]) - f(i[0])
    if negsum not in rightside:
        rightside[negsum] = []
    
    print(i[0] + i[1], f(i[0]) + f(i[0]) )
    