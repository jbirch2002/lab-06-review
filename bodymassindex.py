weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = weight / (height ** 2)

bmi_str = str(bmi)

print("Your BMI is: " + bmi_str)