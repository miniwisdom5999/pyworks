# 2차원 리스트
a = [
    [10, 20],
    [30, 40],
    [50, 60]


]

print(len(a))   # 리스트의 크기(행)
print(len(a[0]))   # 리스트의 크기(행[열])
print(len(a[1]))   # 리스트의 크기(행[열])
print(len(a[2]))   # 리스트의 크기(행[열])

# 리스트 추가
a.append([70, 80])     #값이 아니라 리스트를 넣어줘야함 주의!!



# 출력
for x, y in a:
    print(x, y)
print("=" * 10)


# 중첩 for문
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        print(a[i][j], end=' ')
    print()



# 합계와 평균 계산하기
sum_v = 0
avg = 0.0
count = 0
for i in range(0, len(a)):
    for j in range(0, len(a[i])):           # 개수 세는거 알아두기
        sum_v += a[i][j]
        count += 1
    print()

avg = sum_v / count
print('합계 : {}점'. format(sum_v))
print('평균 : {}점'. format(avg))

