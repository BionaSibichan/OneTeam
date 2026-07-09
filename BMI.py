weight=int(input("Enter weight:"))
height=int(input("Enter height:"))
def calculate_bmi(weight,height):
    if weight<0:
        print("Weight should be greater than 0")
    elif height<0:
        print("Height should be greater than 0")
    else:
        print("Invalid input")

    calculate_bmi=weight/(height*height)
    if calculate_bmi>=18.5:
        print("underweight")
    elif calculate_bmi>=18.5 and calculate_bmi<24.9:
        print("Normalweight")
    elif calculate_bmi>=25 and calculate_bmi<29.9:
        print("Overweight")
    elif calculate_bmi>=30:
        print("Obese")
    return calculate_bmi()
print("BMI is:",round(calculate_bmi(weight,height),2))
print("BMI category:",)


calculate_bmi(weight,height)