print("Welcome to the Tip Calculator")
bill = float(input("How much is your original bill in $:\n"))
num = int(input("How many people would like to pay a tip:\n"))
percentage = int(input("What is the percentage that you would like to pay the tip with it (10, 12, 15):\n"))

tip = bill * (1+ percentage/100) / num
tip_after_rounding = round(tip,2)
print(f"Each people should pay:{tip_after_rounding}")


