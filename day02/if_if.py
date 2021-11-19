# if 중첩 문
num = 10

if num > 10:
    if num % 2 == 0:
        print("10보다 큰 짝수 입니다")
    else:
        print("10보다 큰 홀수 입니다.")
else:
    if num % 2 == 0:
        print("10이하의 짝수 입니다.")
    else:
        print("10이하의 홀수 입니다.")

#if ~ elif ~ else문 호환

if num > 10 and num % 2 == 0:
    print("10보다 큰 짝수 입니다")
elif num > 10 and num % 2 != 0:
    print("10보다 큰 홀수 입니다.")
elif num >= 10 and num % 2 == 0:
    print("10이하의 짝수 입니다.")
elif num >= 10 and num % 2 != 0:
    print("10이하의 홀수 입니다.")








# 내가 한거

numnum = 39

if numnum > 10:
    if numnum % 2 == 0:
        print("10보다 큰 짝수 입니다")
    else:
        print("10보다 큰 홀수 입니다.")
elif numnum <= 10:
    if numnum % 2 == 0:
        print("10이하의 짝수 입니다.")
    else:
        print("10이하의 홀수 입니다.")
else:
    print("잘못 입력 하셨습니다.")
