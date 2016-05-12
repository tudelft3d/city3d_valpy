import os
from lxml import etree
import numpy as np
import pylab as pl

path = ''

def main():
	global path
	if path == '':
		path = os.getcwd()+'/result/Linz_2011/report.xml'
	root = etree.XML(open(path).read())
	print path
	print root
	result = root.xpath("//surface[@type='GroundSurface' and validity[text()='False']]/orientation/text()")
	print len(result)
	data = np.array([float(v) for v in result])
	pl.hist(data)
	pl.xlabel('orientation')
	pl.show()

if __name__ == '__main__':
	main()
