def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
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
	return months