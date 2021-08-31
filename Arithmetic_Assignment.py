cost = eval(input("Total cost of 4 year college: "))
savings = eval(input("How much money can you save in a month for this college?: "))
gift = eval(input("How much additional gift money or scholarships will be given to you?: "))
year = eval(input("How many more years until you can attend this college?: "))

yearsavings = savings * 12
totalsavings = yearsavings * year
allsavings = totalsavings + gift
difference = cost - allsavings


print("Total cost of the 4 year college")
print(cost)
print("Total money you can save per year")
print(yearsavings)
print("Given the number of years until you start college, how much money would you have saved")
print(totalsavings)
print("How much in total money do you have including gifts and scholarship?")
print(allsavings)
print("Overall how much money more money is needed to attend the college or how much is the surplus")
print(difference)

