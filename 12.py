
def factt(n) :
	space = ' ' *(4*n)
	print space, 'factorial', n

	if n == 0:
		print space, 'returning 1'
		return 1
	else :
		result = n*factt(n-1)
		print space, 'returning', result
		return result

print factt(5)
