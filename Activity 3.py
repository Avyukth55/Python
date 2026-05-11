print ("Enter your height")
height=float(input())
print("Enter your weight")
weight=float(input())
bmi=float((weight/(height*height)))
print("BMI is=", bmi)
if bmi<18.5:
    print("You are underweight.")
elif bmi>=18.5 and bmi<=24.9:
    print("You have normal weight.")
elif bmi>=25 and bmi<=29.9:
    print("You are overweight.")
elif bmi>=30:
    print("You are obese.")
