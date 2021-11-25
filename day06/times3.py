# 1~100까지의 수 중에서 배수 출력

def times(x):
    # 3의 배수
    global count    # 전역변수임을 명시함    #전역변수로 만들어줬다!!
    for i in range(1,101):
        if i % x == 0:
            count += 1
            print(i, end=' ')
            #print(count)       #지역으로 찍을거면 여기에!!

count = 0   #전역으로 찍을거면 여기에!!
times(3)
#print("3의 배수의 개수 : ", count)
print("\n3의 배수의 개수 : ", str(count) + "개")

# (지역으로 했을때 설명!!)리턴 받을때는 여기에 print해도 괜찮은데, 지금은 if 안에 있어서 여기에 print 할 필요가 없다!!