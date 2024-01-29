import math

# 7
k = 0


def has_33(nums):
    global k
    for i in nums:
        if i == 3 and k == 1:
            return True
        elif i == 3:
            k = 1
        else:
            k += 2
    return False


"""
something = [1, 2, 3, 3, 4, 5, 6, 7, 8]
something_2 = [1, 2, 3, 2, 1, 2, 3, 1, 1, 5, 6, 7, 5]
print(has_33(something))
print(has_33(something_2))
"""

# 8
s = 0


def spy_game(nums):
    global s
    for i in nums:
        if i == 7 and s == 2:
            print(True)
            s = 0
            return True
        elif i == 0 and s == 1:
            s += 1
        elif i == 0 and s == 0:
            s += 1
    s = 0
    print(False)


'''
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 7, 2, 0, 4, 5, 0])
'''


# 9
def vol(r):
    return 4 / 3 * (r ** 3) * math.pi


# print(vol(3))

# 10
def unique(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)


# unique([1,2,3,1,1,1,1,2,3,4,5,6,7])

# 11
def palin(list):
    rev_l = list[::-1]
    if rev_l == list:
        return True
    return False

'''
print(palin([1, 2, 3, 2, 1]))
print(palin([1, 2, 3, 4, 5, 4, 3, 2]))
'''

# 12
def histo(l):
    for i in l:
        print("*" * i)

histo([4,9,7])