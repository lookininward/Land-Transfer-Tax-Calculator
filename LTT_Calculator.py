# Land Transfer Tax Calculator 0.5

def res_com():
	global property_value

	primary_choice = raw_input("Residential or Commercial? ")

	if primary_choice == "r":
		res_tax()
	elif primary_choice == "c":
		com_tax()
	else:
		res_com()

def res_tax():
	global property_value

	Provincial_LTT = ""
	Municipal_LTT = ""
	Total_LTT = ""
	
	property_value = input("What is the property value? ")

	if property_value < 55000.01:
		Provincial_LTT = property_value * 0.005
		Municipal_LTT = property_value * 0.005
		Total_LTT = Provincial_LTT + Municipal_LTT
		print Provincial_LTT
		print Municipal_LTT
		print Total_LTT
	
	elif property_value > 55000:
		
		if property_value < 250000.01:
			Provincial_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)
			Municipal_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT
		
		elif property_value < 400000.01:
			Provincial_LTT = (55000 * 0.005) + ((250000 - 55000) * 0.01) + ((property_value - 250000) * 0.015)
			Municipal_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)	
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT
		
		else:
			Provincial_LTT = (55000 * 0.005) + ((250000 - 55000) * 0.01) + ((400000 - 250000) * 0.015) + ((property_value - 400000) * 0.02)
			Municipal_LTT = (55000 * 0.005) + ((400000 - 55000) * 0.01) + ((property_value - 400000) * 0.02)
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT


def com_tax():
	global property_value

	Provincial_LTT = ""
	Municipal_LTT = ""
	Total_LTT = ""
	
	property_value = input("What is the property value? ")

	if property_value < 55000.01:
		Provincial_LTT = property_value * 0.005
		Municipal_LTT = property_value * 0.005
		Total_LTT = Provincial_LTT + Municipal_LTT
		print Provincial_LTT
		print Municipal_LTT
		print Total_LTT
	
	elif property_value > 55000:
		
		if property_value < 250000.01:
			Provincial_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)
			Municipal_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT
		
		elif property_value > 400000.01:
			Provincial_LTT = (55000 * 0.005) + ((250000 - 55000) * 0.01) + ((property_value - 250000) * 0.015)
			Municipal_LTT = (55000 * 0.005) + ((400000 - 55000) * 0.01)	+ ((40000000 - 400000) * 0.015) + ((property_value - 40000000) * 0.01)
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT

		else:
			Provincial_LTT = (55000 * 0.005) + ((250000 - 55000) * 0.01) + ((property_value - 250000) * 0.015)
			Municipal_LTT = (55000 * 0.005) + ((property_value - 55000) * 0.01)
			Total_LTT = Provincial_LTT + Municipal_LTT
			print Provincial_LTT
			print Municipal_LTT
			print Total_LTT
		
		# else:
		# 	Provincial_LTT = (55000 * 0.005) + ((250000 - 55000) * 0.01) + ((property_value - 250000) * 0.015)
		# 	Municipal_LTT = (55000 * 0.005) + ((400000 - 55000) * 0.01) + ((property_value - 400000) * 0.015)
		# 	Total_LTT = Provincial_LTT + Municipal_LTT
		# 	print Provincial_LTT
		# 	print Municipal_LTT
		# 	print Total_LTT

res_com()