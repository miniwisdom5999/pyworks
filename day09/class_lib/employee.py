# Employee 클래스 정의
from day09.class_lib.person import Person


class Employee(Person): #Person 클래스 상속받음
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)      # 부모 멤버 super() 함수로 명시
        self.employeeID = employeeID     # 자기 멤버 초기화
#멤버가 없을땐 상관없는데, 멤버가 생겼을때는 부모(상속클래스)멤버를 가져와야함
#자기거는 self.   부모거는 super().

    def __str__(self):  #부모 __str__() 함수 상속 - 재정의(오버라이??)
        return super().__str__() + ", 사번 : " + str(self.employeeID)



e = Employee("이강", 25, 101)
print(e)

#print("이름 : " + e.name)??
#print("나이 : " + e.age)??
#print("사번 : " + e.??????)






# 테스트할때 내용 넣어야만 넘어가는 경우는 pass를 넣어줘서 넘기기 가능!!








# person.py 와 연결시켰다.