## 6.0001 Pset 1: Part c
## Name: Yeabsira Moges
## Time Spent: 30 minutes
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

current_savings = 0
total_cost = 800000
portion_down_payment = 0.25
months = 36
upper_r = 1
lower_r = 0
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

r = (upper_r + lower_r)/2 # find an r value that is between a possible upper and lower bound
down_payment = portion_down_payment * total_cost
upper_down_payment_bound = down_payment + 100
lower_down_payment_bound = down_payment - 100

if initial_deposit >= lower_down_payment_bound: #deposit amount already reached
	r = 0
	steps = 0
elif initial_deposit * (1 + (1/12))**months < lower_down_payment_bound: # not possible with a max 200% raise
	r = None
	steps = 0
else:
	while True:
		steps += 1
		r = (upper_r + lower_r)/2
		current_savings = initial_deposit * (1 + (r/12))**months
		if current_savings > upper_down_payment_bound:
			upper_r = r
		elif current_savings < lower_down_payment_bound:
			lower_r = r
		else:
			break

print("Best savings rate: " + str(r))
print("Steps in bisection search: " + str(steps))