# 예외 만들기 (사용자정의 에러)
# Excrption 클래스를 상속받아야 함

'''
class MyError(Exception):
    pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()     #에러 발생
    print(nick)

say_nick('영웅')
say_nick('바보')

#에러를 발생시켰다!!
'''

# 에러 발생 시킨것 글로 나오게 해줬음

class MyError(Exception):
    pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보' or nick == '멍청':
        raise MyError()     #에러 발생
    print(nick)

try:
    say_nick('영웅')
    #say_nick('바보')
    #say_nick('멍청')
    say_nick('선바')
    say_nick('냥냥')

except MyError as e:    #e는 MyError의 별칭 객체
    print(e)


######왜 에러난 다음에 여러개는 출력 안해...ㅠㅠ??