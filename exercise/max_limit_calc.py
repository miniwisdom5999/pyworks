from exercise.exercise3_q2 import Calculator
# value가 100이상의 값은 가질 수 없도록 제한하기

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


        return self.value


cal = MaxLimitCalculator()
print(cal.add(50))
print(cal.add(60))

print(cal.value)
