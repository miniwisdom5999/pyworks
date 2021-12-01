# 구구단 파일 쓰기
# with ~ as 구문 -> f.close()를 사용하지 않음

with open('gugu.txt', 'w') as f:
    for i in range(2, 10):
        for j in range(1, 10):
            times = "%d x %d = %d\n" % (i, j, i*j)
            f.write(times)
        f.write('\n')