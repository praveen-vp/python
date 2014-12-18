
def istriangle(a,b,c) :
	if (a+b) >= c :
		print 'yes'
		return
	elif (a+c) >= b:
		print 'yes'
		return 
	elif (b+c) >= a:
		print 'yes'
		return
	else :
		print 'no'
		return

istriangle(4,2,3)

