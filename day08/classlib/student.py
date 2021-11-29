# 생성자 - 매개변수가 있는 생성자
class Student:
    def __init__(self, name, grade):    #생성자로 매개 변수를 전달
        self.name = name
        self.grade = grade

    def __str__(self):  #객체의 멤버정보를 출력하는 함수 (필수!!)
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)


if __name__ == "__main__":      #여기서도 적용하고싶을때..??무슨말이닞 모르겠당...
    s1 = Student("콩쥐", 1)   #s1 객체 생성
    print(s1)

    s2 = Student("팥쥐, 2") #s2 객체 생성



##########################