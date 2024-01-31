# 1
def square(n):
    for i in range(n):
        yield i ** 2


'''
for n in square(10):
    print(n)
'''


# 2
def only_even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

'''
n = int(input())
for i in only_even(n):
    print(f"{i}, ",end="")
'''

#3
def between(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
'''
for i in between(20):
    print(i)
'''

#4
def squares(n,m):
    for i in range(n,m+1):
        yield i**2
'''
for i in squares(5,15):
    print(i)
'''

#5
def down(n):
    for i in range(n+1):
        yield n-i

for i in down(20):
    print(i)

    