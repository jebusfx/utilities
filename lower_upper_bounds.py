def lower_bound(_list,lower,upper,value,position_found=-1):	
	if lower <= upper:
		midpoint = lower + (upper - lower)/2
		if value == _list[midpoint]:
			return lower_bound(_list,lower,midpoint - 1,value,midpoint)
		elif value < _list[midpoint]:
			return lower_bound(_list,lower,midpoint - 1,value,midpoint - 1)			
		elif value > _list[midpoint]:
			return lower_bound(_list,midpoint + 1,upper,value,position_found)		
	return position_found

def upper_bound(_list,lower,upper,value,position_found=-1):	
	if lower <= upper:
		midpoint = lower + (upper - lower)/2
		if value == _list[midpoint]:
			return upper_bound(_list,midpoint + 1,upper,value,midpoint)
		elif value > _list[midpoint]:
			return upper_bound(_list,midpoint + 1,upper,value,midpoint + 1)
		elif value < _list[midpoint]:
			return upper_bound(_list,lower,midpoint - 1,value,position_found)		
	return position_found

if __name__ == "__main__":
	_list = [1,1,1,1,2,2,2,2,3,3,3,3,4,5,5,5,5,7,8,8]
	#print lower_bound(_list,0,len(_list) - 1,6)
		#print upper_bound(_list,0,len(_list) - 1,6)
	# print lower_bound(_list,0,len(_list) - 1,2)
	# print lower_bound(_list,0,len(_list) - 1,5)
	# print lower_bound(_list,0,len(_list) - 1,7)
		# print upper_bound(_list,0,len(_list) - 1,2)
		# print upper_bound(_list,0,len(_list) - 1,5)
		# print upper_bound(_list,0,len(_list) - 1,7)	
	print upper_bound(_list,0,len(_list) - 1,214)
	print lower_bound(_list,0,len(_list) - 1,2134)