customer_num = int(input("전체 인원수 : "))
col_num = int(input("좌석 열 수 : "))

if customer_num % col_num == 0:
    row_num = int(customer_num / col_num)
else:
    row_num = int(customer_num / col_num) + 1
print("필요한 줄 수는 %d줄 입니다." % row_num)
