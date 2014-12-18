
def is_rev(a,b) :
	i = 0
	j = len(b)-1

	if (len(b) != len(a)) :
		return False

	while j > 0 :
		print j,i
	
		if a[i] != b[j] :
			return False
		i+=1
		j-=1
	
	return True

print is_rev('stop','pots')

