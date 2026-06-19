def calculate_bmi(weight_kg, height_m):

    # Validate input
    if weight_kg <= 0 or height_m <= 0:
        return {"error": "Weight and height must be greater than 0."}

    bmi = weight_kg / (height_m ** 2)
    bmi_rounded = round(bmi, 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {
        "bmi": bmi_rounded,
        "category": category
    }


# Test cases
print(calculate_bmi(50, 1.7))   # Underweight
print(calculate_bmi(68, 1.75))  # Normal weight
print(calculate_bmi(85, 1.75))  # Overweight
print(calculate_bmi(100, 1.75)) # Obese
print(calculate_bmi(70, 0))     # Invalid input