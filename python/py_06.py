score = int(input())

if score > 101:
    print(-1)
elif score > 80:
    print("A")
elif score > 60:
    print("B")
elif score > 0:
    print("C")
else:
    print(-1)