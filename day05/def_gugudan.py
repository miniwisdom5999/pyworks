# 구구단 함수 정의
def print_gugu(dan):
    for i in range(1,10):
        #print(dan, 'x', i, '=', (dan*i))
        print("%d x %d = %d" % (dan, i, dan*i))

print_gugu(6)      # 얘가 메인 함수고 위에는 지역 함수다..!! 큰틀을 보자면..??