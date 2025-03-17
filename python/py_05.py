score = input().split()
kor = int(score[0])
eng = int(score[1])
math = int(score[2])

# 총합, 평균 계산
sum = kor+eng+math
avg = sum / 3
print(sum)
print(avg)