COUNT = 5
scores = []
sum = 0

print(COUNT, "개의 정수를 입력하세요 : ")
for i in range(COUNT):
    value = int(input())
    scores.append(value)
    sum += value

avg = sum / len(scores)

print(scores)
print("sum = ", sum , ",avg = ", avg)