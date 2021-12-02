# word.txt 만들기
import random as r


with open("word.txt", "w") as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree',
            'strawberry', 'grape', 'garlic', 'onion', 'potato']
    for w in word:
        f.write(w + ' ')
        
        
        
# 단어를 랜덤하게 추출하기
with open("word.txt", "r") as f:
    #word = f.readline() #리스트로 반환됨    #그냥 read만 쓰면 word 전체가 줄줄이 나옴;;
    word = f.readline().split()   #단어 전체 (공백문자로 구분)  # 하나씩 끊어줌!!
    w = r.choice(word)  #랜덤하게 단어 1개 추출      # 맨 위에 임포트 랜덤 써야함!!
    print(w)