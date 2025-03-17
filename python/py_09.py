weight = float(input())
height = float(input())
height_m = height / 100 
bmi = weight / (height_m * height_m)

if bmi < 20:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 40:
    print("Obesity")
else:
    print("Extremely overweight")