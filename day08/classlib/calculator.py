# 계산기 클래스 정의
# 기능 : 더하기 , 빼기

class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x += y     # self.x = self.x + y
        return

    #####################