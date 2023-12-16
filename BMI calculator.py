def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Example usage:
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi_result)

print(f"Your BMI is {bmi_result:.2f}, which is considered {interpretation}.")

