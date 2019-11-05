#A program that calculates compound interest over time given an initial deposit and rate of interest

print("Hello and welcome to the savings calculator. Please enter the initial deposit:")
deposit = input()

print("Thankyou. Now please enter the rate of interest you predict you can get on your savings:")
interest = input()

print("Here is what you can expect your savings to be worth year on year for the next twenty years:")

value = int(deposit)
for i in range(30):
    print("Year ", (i + 1), ": £", round(value, 2))
    value = value + (value * (int(interest) / 100))
