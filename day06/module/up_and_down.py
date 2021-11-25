# 숫자 추측 게임
import random

'''
com = random.randint(1, 100)    #컴퓨터가 1~100 난수 생성
for i in range(10):
    guess = int(input("맞혀 보세요 : "))     #사용자가 추측한 숫자
    if guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("DOWN!! 너무 커요~ 정답은 더 작은 수 입니다")
    else:
        print("UP!! 너무 작아요~ 정답은 더 큰 수 입니다")

print("정답 : %d" % com)
'''


com = random.randint(1, 100)    #컴퓨터가 1~100 난수 생성
min_v = 1
max_v = 100
for i in range(10):
    #사용자가 추측한 숫자
    guess = int(input("맞혀 보세요([%d회] %d ~ %d) -> " % (i+1, min_v, max_v)))     #사용자가 추측한 숫자
    if guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("DOWN!! 너무 커요~ 정답은 더 작은 수 입니다")
        max_v = guess
    else:
        print("UP!! 너무 작아요~ 정답은 더 큰 수 입니다")
        min_v = guess

print("정답 : %d" % com)
print("점수 : %d점" % ((10 - i) * 10))        # 점수 = 남은 횟수 * 10