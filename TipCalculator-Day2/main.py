print('Welcome to the tip calculator!')
bill = float(input('What was the total bill? $'))
tip = float(input("Hoy much tip would you like to give? 10, 12, or 15?"))
people = int(input('How many people to split the bill?'))

split = (bill + (bill * (tip / 100))) / people

print(f"Each person should pay: ${round(split, 2)}")
