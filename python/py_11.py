price = int(input())
total = price
if price > 150000:
    total =round((price * 15) / 100)
    print("15%")
    print(price - total)
elif price > 100000:
    total = round((price * 10) / 100)
    print("10%")
    print(price - total)
elif price > 50000:
    total =round((price * 5) / 100)
    print("5%")
    print(price - total)
else:
    print("-1")