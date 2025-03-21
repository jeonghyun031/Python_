#성적 입력 시 등급 부여
def GetGrade(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'

score = int(input())
if (score > 100 or score < 0):
        print(-1)
else:
    print("Your Grade is %c" %GetGrade(score))