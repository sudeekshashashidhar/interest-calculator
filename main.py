def compound_interest(principle, rate, time):
  amount = principle * (pow((1 + rate / 100), time))
  CI  = amount - principle
  print("Compound interest is Rs.", CI)


principle = float(input("ENTER THE PRINCIPLE AMOUNT: "))
rate = float(input("ENTER THE RATE OF INTEREST: "))
time = float(input("ENTER THE TIME PERIOD: "))

compound_interest(principle, rate, time)