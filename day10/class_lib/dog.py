# Dog 클래스 만들기
# https://docs.python.org/ko/3/tutorial/classes.html#class-objects
# 여기 나오는 내용임!!

class Dog:
    kind ="진돗개"     #클래스 변수

    def __init__(self, name):
        self.name = name    #인스턴스 멤버 변수

dog1 = Dog("백구")
dog2 = Dog("둥이")

print(dog1.name)    #unique (유일한) 이름
print(dog1.kind)    #shared (공유한) 종류
print(dog2.name)
print(dog2.kind)