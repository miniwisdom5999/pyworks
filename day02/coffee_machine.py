# 커피 자판기 프로그램
# 가격 : 400원, 커피의 총 개수 : 5개



coffee = 5      #전역변수
price = 400
while True:
    money = int(input("돈을 넣어주세요."))    # 소수까지 하고싶으면 float
    if money == price:
        print("커피가 나옵니다.")
        coffee = coffee - 1
    elif money > price:
        print("커피가 나오고, 거스름돈", (money - price), "원을 돌려 받습니다.")
        coffee -=1
    elif money < price:
        print("커피가 나오지 않습니다. 금액이 부족합니다.")


    print("남은 커피의 양은 " + str(coffee) + "개 입니다.")

    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break
        
        
