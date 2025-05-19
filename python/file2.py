with open("prob1-1.txt", "a", encoding="utf-8") as file:
    user_input = input("추가 입력(Q 입력 시 종료): ")
    if user_input != "Q":
        file.write(user_input + "\n")

with open("prob1-1.txt", "r", encoding="utf-8") as file:
    content = file.readlines()

with open("prob1-2.txt", "w", encoding="utf-8") as file:
    file.writelines(content)

print("prob1-2.txt에 저장된 내용:")
print("".join(content))