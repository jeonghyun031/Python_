with open("prob1-1.txt", "w", encoding="utf-8") as file:
    while True:
        user_input = input()
        if user_input == "Q":
            break
        file.write(user_input + "\n")