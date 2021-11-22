#p146

'''
#Q1

a = "Life id too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#if elif  쓸때 결과는 하나만 나온다.
'''




'''
#Q2

result = 0
count = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        count += 1
        result += i
    i += 1

print("합계 :", result)
print("개수 :", count)
'''




'''
#Q3

print('=' * 30)
print('*' * 5)

print()

#whlie문

i = 0
while True:
    i += 1
    if i > 5 : break
    print(i * '*')

#for문

for i in range(0, 5):
    for j in range(0, i + 1):
        print("$", end='')
    print()
'''



'''
#Q4

for i in range(1, 101):
    print(i)
'''



#Q5

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(total)
print(average)
