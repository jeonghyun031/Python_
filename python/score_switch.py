a = int(input("성적을 입력하시오 : "))
def get_grade(score):
    match score:
        case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
            grade = "A"
        case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
            grade = "B"
        case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
            grade = "C"
        case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
            grade = "D"
        case _:
            grade = "F"
    return grade

print(get_grade(a))