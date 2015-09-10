a = [13, 41, 66]
c = []

def makelist_x(xcoordinate, listlen):
	xlist = []
	zeronum = 0
	while zeronum <= listlen:
		for xx in xcoordinate:
			if xx == len(xlist):
				xlist.append('x')
				zeronum = zeronum + 1
		xlist.append(0)
		zeronum = zeronum + 1
	return xlist
	xcoordinate = xlist

makelist_x(a, 70)
print (a)