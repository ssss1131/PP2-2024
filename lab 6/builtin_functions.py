from math import prod, sqrt
from time import sleep

# 1
list = [1, 2, 3, 4, 5, 10]
# print(prod(list))

# 2
stri = "HELLO my name IS Saulet"
#print(sum(1 for char in stri if char.islower()))
#print(sum(1 for char in stri if char.isupper()))

# 3
stri_3 = "kazak"
stri_3_2 = "apple"
# print("Yes" if stri_3==stri_3[::-1] else "No")
# print("Yes" if stri_3_2==stri_3_2[::-1] else "No")

# 4
'''
num_4 = int(input())
time_4 = int(input())
sleep(time_4/1000)
print(f"Square root of {num_4} after {time_4} miliseconds is {sqrt(num_4)}")
'''

#5
list_5=(True,1,True)
print(all(list_5))