







# FILTER!
def post_filter(link,headline,text,html,cost,email):
	"""
	This is the function for deciding if a craig's list 
	entry matches your requirements. 

	Return True or False.
	"""

	# example
	body = headline+" "+text
	if body.lower().find('silverlake') > -1:
		return True
	if body.lower().find('los feliz') > -1:
		return True


	return False



