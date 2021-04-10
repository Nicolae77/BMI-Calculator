height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
if bmi <= 18:
    print("You are Underweight!!!")
elif 18 < bmi <= 25:
    print("You are perfect, Normal Body Mass Index.")
elif 25 < bmi <= 30:
    print("You are Overweight!!!")
elif 30 < bmi <= 35:
    print("You are OBESE!!!")
else:
    print("You are EXTREMELY OBESE!!!")
bmi_as_int = int(bmi)
print(bmi)
print(round(bmi))
print(bmi_as_int)