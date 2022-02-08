def part_a(annual_salary, portion_saved, total_cost):
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
	
		"""
		Iterating until current savings is greater than or equal to down payment
		"""
	
		current_savings += current_savings*annual_r/12 #annual rate / 12 to get monthly rate
		current_savings += (annual_salary/12)*portion_saved # portion saved * monthly salary to get monthly savings
		months+=1
	
	print("Number of months: " + str(months))
	return months