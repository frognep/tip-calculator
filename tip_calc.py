print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))

total_w_tip = total_bill + total_bill * (percent_tip / 100)
total_for_all = total_w_tip / num_of_people

print(f"Each person should pay: ${round(total_for_all, 2)}")

#test