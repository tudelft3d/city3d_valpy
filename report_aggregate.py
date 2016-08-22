from lxml import etree
import os
import sys

def aggregate(source_elements,xmldist):
	path_dist = open(xmldist).read()
	root_dist = etree.XML(path_dist)
	try:
		for ele in root_dist.getchildren():
			if ele.tag == 'building':
				source_elements.insert(0,ele)
			elif ele.tag == 'inputfile/' or ele.tag == 'inputfile':
				continue
			else:
				source_value = int(source_elements.find('.//'+ele.tag).text)
				source_elements.find('.//'+ele.tag).text = str(source_value + int(ele.text))
	except ValueError:
		print ele," : ",xmldist

def iterate_path(path):
	reports = []
	for root,dirnames,filenames in os.walk(path):
		for fname in filenames:
			if fname.find('sem')!=-1:
				report_name = root+'/'+fname
				if len(open(report_name).readlines())<2:
					continue
				reports.append(root+'/'+fname)
	#print reports
	path_source = open(reports[0]).read()
	root_source = etree.XML(path_source)
	#source_elements = root_source.getchildren()
	for report in reports[1:]:
		aggregate(root_source,report)
	print etree.tostring(root_source,pretty_print=True)

if __name__ == '__main__':
	dirpath = '/home/dxin/result_valsem/'+sys.argv[1]
	iterate_path(dirpath)
