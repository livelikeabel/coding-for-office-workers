"""
#구구단
num = input("몇 단을 출력 하시겠습니까?")
for i in range(9):
    result = int(num)*(i+1)
    print(str(num) + " * " + str(i+1) + " = " + str(result))
"""

dan = int(input("몇 단을 출력 하시겠습니까?"))
for num in range(1,10):
    result = dan * num
    print("{} * {} = {}".format(dan, num, result))
