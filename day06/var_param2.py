# 가변 매개변수 예제

def merge_text(*text):
    sum_s = " "      #문자변수 초기화시 공백 문자
    for s in text:
        sum_s += s
        return sum_s

str1 = merge_text("봄", "여름")
str2 = merge_text("봄", "여름", "가을", "겨울")


# 문자를 합치고 싶었다!!

# 초기화 할때 숫자는 0을 넣고 문자는 공백(" ")을 넣는다!!


# 파이썬 교재 157~9p
# 파이썬 교재 231~ p
