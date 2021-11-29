# 다각형 그리기
import turtle as t

def polygon(n):    # n - 변의 수
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def polygon2(n, d): # d - 거리
    for x in range(n):
        t.forward(d)
        t.left(360/n)

polygon(3)      #삼각형 실행
polygon(5)      #오각형 실행

t.up()          #선 올리기      #이거 안하면 다른 도형 그리러 가는길의 이동 선이 보인다!!
t.forward(100)
t.down()        #선 내리기

polygon2(3, 100)
polygon2(5, 100)


t.mainloop()