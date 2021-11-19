#자리배치도 프로그램
#고객수를 열(좌석)로 나눠 행(줄)을 구해서 for문으로 배치
customer = 28
col = 5
row = customer // col #몫

for i in range(0, row):
    for j in range(1, col+1):    #여기 1을 0으로 하면 0부터 시작하던데..!!
        print(i*col+j, end=' ')
    print()
