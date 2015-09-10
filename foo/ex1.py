import re

for x in dir(re):
	if x[0] == 'f' and x[1] == 'i':
		print (x)