#중첩 for문

# 5행 5열에 문자 출력
for i in range(0, 5):
    for j in range(0, 5):
        print("$", end='')
    print()




#직각 삼각형 모양
for i in range(0, 5):           #5까지라고 쓰면 4라서 +1 해줘야한다!!
    for j in range(0, i+1):
        print("$", end='')
    print()


#역직각 삼각형 모양
for i in range(0, 5):
    for j in range(0, 5-i):
        print("$", end='')
    print()
print()


# 5행 5열 안에 1부터 순차적으로 증가 구현
for i in range(0, 5):
    for j in range(i, 6):
        num = i*5+j
        print(num, end=' ')
    print()
