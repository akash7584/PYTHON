#BMI calculate:
Weight_Kg=float(input("Enter a weight="))
Height_meter=float(input("Enter a height="))
BMI=Weight_Kg/(Height_meter*Height_meter)
if BMI<18.5:
    print("Underweight")
elif BMI>18.5 and BMI<24.9:
    print("Normal")
elif BMI>25 and BMI<29.9:
    print("OverWeight")
else:
    print("Obese")

