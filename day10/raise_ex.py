# 예외 처리 미루기
# 사용하는 곳에서 예외를 처리함
class Animal:
    def cry(self):
        #print("소리를 낸다")
        raise NotImplementedError   # 구현하지 않으면 에러 발생
        #try를 쓰거나 raise를 쓰거나 ㅇㅇ!!
        
        
class Dog(Animal):  #Animal 상속
    #pass
    def cry(self):      # cry 재정의
        print("왈와리~~왈왈~~")
        
class Cat(Animal):
    #pass
    def cry(self):
        print("냥냥~~냥냐냥~~")

dog = Dog()
dog.cry()

cat = Cat()
cat.cry()
