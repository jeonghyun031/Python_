a, b, c = map(int, input().split())
print("Input 3 integer values>> ", end="")
if a+b > c and a+c > b and b+c > a :
    print("Yes, this is a triangle.")
else:
    print("No, this is NOT a triangle.")