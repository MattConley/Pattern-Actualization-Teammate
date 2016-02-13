#import sys

pone = {"y" : ['ep','es','a','ea','eah','eh','essir', 1], "n" : ['o','ope','ot', 0]}

def pos_neg(s):
	try:
		available = pone[s[0]]
		return available[-1]
	except:
		#e = sys.exc_info()[0]
		#print(e)
		return complarse(s)
		

def complarse(s):
	delimited = s.split(' ')
	return delimited

def process(s):
	return s

def boolus(wino):
	toref = pos_neg(wino)
	print(toref)
	return toref
	
