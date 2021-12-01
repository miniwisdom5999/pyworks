# 파일 쓰기

f = open("c:/web_dev/pyfile/file.txt", "w")  #파일 열기
f.write("하늘이 파랗다\n")

f.write("Thank you!!\n")

f.write("社員\n")

#f.write(45)   # 숫자는 바로 저장할 수 없음

f.write('45')   # 문자는 가능    # 숫자로 넣을 다른 방법은 따로 있다고 함..ㅇㅇ









f.close()   #파일 닫기