
def find(word,letter) :
	i = 0
	while i < len(word):
		if word[i] == letter :
			return i
		i+=1
	return -1
	
print(find('praveen','v'))
