bill = input("Welcome to the tip calculator!\nWhat was the total bill? $")

percentage = input("How much tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

bill_as_float = float(bill)

percentage_as_float = float(percentage)

people_as_float = float(people)

each_person_pay = (bill_as_float/people_as_float) *((percentage_as_float/100) + 1)
each_person_pay_rounded = round(each_person_pay, 2)
format_dollar = "{:.2f}".format(each_person_pay_rounded)
print(f"Each person should pay: ${format_dollar}")