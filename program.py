__author__ = 'Kw'

import zip.extract
import zip.compress

l = [1,2,3]
ll = 10

print (zip.compress.compress(zip.extract.extract(l, ll)))