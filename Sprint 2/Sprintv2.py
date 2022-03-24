import math
import re

print("Choose between Investment and Bond.")
x = input()

while re.search("[A-Z a-z 0-9]", x, re.I):
    if re.search("investment", x, re.I):
        print("Enter amount of money you will be depositing:")
        investment_amount = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", investment_amount, re.I):
            print("Please enter a valid amount.")
            investment_amount = input()
        print("Enter interest rate(Do not include the '%' symbol):")
        interest_rate = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", interest_rate, re.I):
            print("Please enter a valid interest rate.")
            interest_rate = input()
        print("Enter amount of years for the investment:")
        amount_of_years = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", amount_of_years, re.I):
            print("Please enter a valid amount of years.")
            amount_of_years = input()
        print("Would you like to calculate simple interest or compound interest?")
        interest = input()
        while re.search("[A-Z a-z 0-9]", interest, re.I):
            if re.search("simple", interest, re.I):
                final_amount = float(investment_amount) * ( 1 + (float(interest_rate) / 100) * float(amount_of_years))
                print("Final amount = R" + "%.2f" % float(final_amount))
                break
            elif re.search("compound", interest, re.I):
                final_amount = float(investment_amount) * math.pow((1 + (float(interest_rate) / 100)) , float(amount_of_years))
                print("Final amount = R" + "%.2f" % float(final_amount))
                break
            else:
                print("Please enter one of the given options.")
                interest = input()
        break
    elif re.search("bond", x, re.I):
        print("Enter Present Value of the house:")
        present_value = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", present_value, re.I):
            print("Please enter a valid present value.")
            present_value = input()
        print("Enter Annual Interest Rate(Do not include the '%' symbol):")
        interest_rate = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", interest_rate, re.I):
            print("Please enter a valid amount of years.")
            interest_rate = input()
        print("Enter amount of months you will repay the bond in:")
        amount_of_months = input()
        while re.search("[A-Z a-z !#$%&'()*+,-./:;<=>?@^_`{|}~]", amount_of_months, re.I):
            print("Please enter a valid amount of months.")
            amount_of_months = input()
        bond_repayment =(((float(interest_rate)/100)/12) * float(present_value)) / (1 - math.pow((1 + ((float(interest_rate) / 100) / 12)), -(float(amount_of_months))))
        print("Bond Repayment amount for each month will be equal to R" + "%.2f" % float(bond_repayment))
        break
    else:
        print("Please enter one of the given options.")
        x = input()