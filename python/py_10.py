change =  int(input())
coins = [500, 100, 50, 10]

count = 0

for coin in coins:
    count = change // coin
    change %= coin
    print(count, end= " ")