import requests
from bs4 import BeautifulSoup

url = "http://naver.com/"
resp = requests.get(url)    #응답 객체 생성
soup = BeautifulSoup(resp.text, 'html.parser')  #html 파싱(해석)할 soup 객체 생성

div = soup.find('div', attrs={'class': 'service_area'})     #div의 class 속성을 팢음
                #태그이름, 소스이름???
first_a = div.find('a')    #div속성으로 첫번째 'a'태그 찾음
print(first_a)
print(first_a.text)



#주니어 네이버 문자열 찾기
all_a = div.find_all('a')
# print(all_a)
print(all_a[1].text)
