# 다중 try ~ except 구문
'''
data = [50, 70, 30, 90]
print(data[0])
print(data[4])


#IndexError: list index out of range  인덱스 에러 생겼음
'''
try:
    data = [50, 70, 30, 90]

    x = int(input("정수 입력(0~3까지) : "))
    print(data[x])

except IndexError:
    print("0~3까지 입력해주세요.")
except ValueError:
    print("숫자가 아닙니다. 정수를 입력해 주세요.")

    