## 6.0001 Pset 1: Part b
## Name: Yeabsira Moges
## Time Spent: 7 minutes
## Collaborators:

##########################################################################################
## Get user input for annual_salary, portion_saved, total_cost, semi_annual_raise below ##
##########################################################################################

annual_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
current_savings = 0
annual_r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

down_payment = portion_down_payment * total_cost

while current_savings < down_payment:

	current_savings += current_savings*annual_r/12 #annual rate / 12 to get monthly rate
	current_savings += (annual_salary/12)*portion_saved # portion saved * monthly salary to get monthly savings
	annual_salary *= (1 + semi_annual_raise) if (months+1) % 6 == 0 else 1 # 1 + semi anual raise to get percent increase, months + 1 to get months passed instead of the index of the month
	months+=1

print("Number of months: " + str(months))