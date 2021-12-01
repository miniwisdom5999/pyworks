# 파일을 열 수 없습니다~~~!!!!
# 만약 파일이름을 틀렸다면 다운되어 버리는데, 그 전에 표시하게 만들기!!

season = ['봄', '여름', '가을', '겨울']
f = open("c:/web_dev/pyfile/season.txt", 'w')
for i in season:
    f.write(i + '\n')  # 파일에 쓰기(저장)

f.close()  # 닫기

try:
    f = open("c:/web_dev/pyfile/seasonsss.txt", 'r')    #여기서 없는 파일이름 적어줬음!!
    season = f.read()
    print(season)
except FileNotFoundError:
    print("파일을 열 수 없습니다.")                         #표시 해줬음!!