# Student 클래스 만들기
# 클래스는 self 키워드를 사용
# init() - 생성자(Constructor)함수 사용

class Student:
    def __init__(self):          #inital 이니셜 (생성자)
        self.name = "콩쥐"        #멤버 변수
        self.grade = 1
        print("생성자 함수 입니다.")        #run해보면 제일 먼저 출력!!

    def learn(self):
        print("수업을 듣습니다.")          # ^-^ 여기서 return을 써줬으면 아래 프린트 필요함. 상황에 따라 사용하기!!

s = Student()       #Student 클래스의 객체(인스턴스) s 생성
# 매개변수가 업는 생성자
print("이름 : " + s.name)
print("학년 : " + str(s.grade))

s.learn()       # 얘는 프린트 할거 없당 위에서 이미 해서!! ^-^