#파일 읽기

f = open("c:/web_dev/pyfile/number.txt", 'r')  #파일 읽기 모드 - 'r' 사용

text = f.read()     #파일 내용 전체 읽어옴(보조기억장치)   #이건 저장이 안된다!!
print(text)         # 콘솔에 출력(메모리)
f.close()           #파일 닫기










f.close()

####################모르겠당 -> 파일이 나중에 만들어지기도 하네 기다려야하는듯