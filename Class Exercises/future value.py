'''
def main():
    investment = int(input("Enter monthly investment: "))
    interest = float(input("Enter yearly interest rate: "))
    years = int(input("Enter number of years"))
def spacing ():
    print ("")
    print ("")

print (f"Monthly investment:\t\t\t${investment}")
print (f"Interest rate:\t\t\t{interest}")
print (f"Years:\t\t\t${years}")
futurevalue = 0
monthlyinterest = futurevalue * (interest/12)
'''

import locale as lc
def futurevalue (monthlyinvestment, yinterest, years):
    monthlyinvestment = yinterest / (12 / 100)
    months= y * 12
    futurevalue = 0
    for i in range (months)
        futurevalue += monthlyinvestment
        monthinterest = futurevalue * monthlyinterest
        futurevalue += monthinterest
    return futurevalue

def main():
    choice = ('y')
    while choice == 'y':
        monthlyinterest = int(input('Enter monthly investment \t\t '))
        yearlyinterest = int(input('Enter yearly investment \t\t '))
        years = int(input('Enter years \t\t '))

        futurevalue = futurevalue(monthlyinvestment, yinterest, years)
        lc.setlocale(lc.LC_ALL, 'en_US')
        monthlyinvestment = lc.currency(monthly_investment, yearly_interest, grouping = True)
        futurevalue = lc.currency(future_value, grouping =True)

        print(f"{'Monthly investment: ':20} [monthlyinvestment: >10}")
        print(f"{'interest rate:' :20'} {futurevalue : >10.2f}")



