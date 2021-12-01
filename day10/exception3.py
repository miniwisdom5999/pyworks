# try ~ except ~ finally

'''
def div(x, y):
    result = x / y
    print(result)

div(2, 1)
div(2, 0)

#ZeroDivisionError: division by zero  나눌때 0이 있어서 에러났음
'''

def div(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    finally:
        print("여기는 반드시 수행되는 구간입니다.")

#div(2, 1)
div(2, 0)