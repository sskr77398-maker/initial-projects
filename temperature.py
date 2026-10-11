unit = input("the entered unit is in fahrenheit or celcius (c/f): ")   # f = c * (9/5+32) 
temperature = float(input("enter the temperature: "))                  # c = f - 32 * 5/9

if unit == "c":
    temp = round((temperature*9)/5+32,2)
    print(f"the converted temp. is: {temp}")

elif unit == "f":
    temp = round((temperature-32)*5/9,2) 
    print(f"the converted temp. is: {temp}")

else:
    print("invalid input")    