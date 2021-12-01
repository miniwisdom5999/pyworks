# 파일 쓰기

f = open("c:/web_dev/pyfile/file.txt", "w")     # 파일 열기, 쓰기모드
f.write("%d\n" % 25)
f.write("%f\n" % 12.34)
f.write("%d\n" % (45 + 1))  #괄호 생략하면 안됨

i = 3
j = 4
times = "%d x %d = %d" % (i, j, i*j)
#숫자 바로 넣어도 괜찮고 i와 j 변수를 만들어줘도 괜찮다
f.write(times)





f.close()       # 파일 닫기