weight = float(input("enter your weight in kg/p: "))
unit = input("enter the unit: ")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is: {round(weight,2)} {unit}")

elif unit == "p":
    weight = weight / 2.205
    unit = "kgs."
    print(f"your weight is: {round(weight,2)} {unit}")

else:
    print(f"{unit} is not valid unit")  

