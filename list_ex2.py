l = [1,2,3,4,5,6]

def double_l(l):
	s = []
	for x in l:
		s.append(x*2)		
	l = s
	return l
	
	
print (double_l(l))