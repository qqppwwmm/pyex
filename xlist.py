
a = [13, 41, 66]
c = []

def makelist_x(xcoordinate, listlen, xlist):
	xcoordi = 0
	zeronum = 0
	while zeronum <= listlen:
		while xcoordi < len(xcoordinate):
			if len(xlist) == xcoordinate[xcoordi]:
				xlist.append('x')
				xcoordi = xcoordi + 1
				zeronum = zeronum + 1
			else:
				xlist.append(0)
				zeronum = zeronum + 1
		xlist.append(0)
		zeronum = zeronum + 1
	return xlist
				
		
makelist_x(a, 70, c)
print (c)
