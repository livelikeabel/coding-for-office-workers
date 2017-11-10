#list, tuple 에서 임의의 값 하나 뽑기

import random

foo = [1, 2, 3, 4, 5]
print(random.choice(foo))

# 출처 : https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

import random

foo = ['battery', 'correct', 'horse', 'staple']
secure_random = random.SystemRandom()
print(secure_random.choice(foo))
