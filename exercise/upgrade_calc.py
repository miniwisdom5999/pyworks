from exercise.exercise3_q1 import Calculator

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)