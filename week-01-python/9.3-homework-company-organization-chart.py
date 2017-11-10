#no hint
"""
사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.
"""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Colleague(Person):
    rank = "대리"
#Person
i_name = input("Input name : ")
i_age = input("Input age : ")
i_gender = input("Input gender : ")

person1 = Person(i_name, i_age, i_gender)
print("person name is {}, {} years old and good {}.".format(person1.name, person1.age, person1.gender))

#Colleague
ic_name = input("Input colleague name : ")
ic_age = input("Input colleague age : ")
ic_gender = input("Input colleague gender : ")

colleague1 = Colleague(ic_name, ic_age, ic_gender)
print("colleague name is {}, {} years old, rank is {} and very faithful {}.".format(colleague1.name, colleague1.age, colleague1.rank, colleague1.gender))
