# 문자열 함수 - 특별한 1차원 리스트
s = "banana, grape, apple"
x = s.split(',')    # 콤머(,)를 구분기호로 설정
print(x)        #['banana', ' grape', ' apple']
print(x[0])     #banana

for i in x:
    print(i)

print()

s2 = "a, b, c, d"
x2 = s2.split(':')
print(x2)


# 두 수를 동시에 입력 받아 더하기
n1, n2 = input("두 수 입력 :").split()

#놓쳤음ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ

add = n1 + n2
print(add)

