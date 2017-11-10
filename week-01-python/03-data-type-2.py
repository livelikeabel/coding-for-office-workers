#list []
list_a = [1, 2, 3]
#type([1, 2, 3])
list_a[0:2]
list_a.append(4)
list_a.remove(2)
list_a.clear()



#tuple () - 한번 만들어진 내용을 변경할 수 없다.
(1,)
(1, 2, 3)
#type((1, 2, 3))


# dict (map) {}
# key & value
dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
 }
dict_a["apple"]


# set set([])
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)
# 집합 = 교집합, 합집합, 차집합, 여집합
# 중복제거
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
