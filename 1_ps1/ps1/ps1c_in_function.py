def part_c(initial_deposit):
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
	
	r = (upper_r + lower_r)/2
	down_payment = portion_down_payment * total_cost
	upper_down_payment_bound = down_payment + 100
	lower_down_payment_bound = down_payment - 100
	
	if initial_deposit >= lower_down_payment_bound:
		r = 0
		steps = 0
	elif initial_deposit * (1 + (1/12))**months < lower_down_payment_bound:
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
	return r, steps