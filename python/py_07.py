i = int(input())

if i > 0:
    i = i % 2
    if i == 0:
        print("even")
    elif i != 0:
        print("odd")
else:
    print(-1)