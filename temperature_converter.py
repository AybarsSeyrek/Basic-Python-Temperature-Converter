#Phyton temperature conversion program

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

# If the user entered C, convert Celsius to Fahrenheit
if unit == "C":
    temp = round(temp * 9 / 5 + 32, 1)
    print(f"Your temperature in Fahrenheit is {temp} F")
# If the user entered F, convert Fahrenheit to Celsius
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Your temperature in Celsius is {temp} C")
# If the user entered anything other than C or F, show an error message
else:
    print(f"{unit} is an invalid unit of measurement")
