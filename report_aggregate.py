from lxml import etree
import os

def aggregate(source_elements,xmldist):
	#path_source = open(xmlsour).read()
	#root_source = etree.XML(path_source)
	path_dist = open(xmldist).read()
	root_dist = etree.XML(path_dist)
	#source_elements = root_source.getchildren()
	for ele in root_dist.getchildren():
		if ele.tag == 'building':
			source_elements.insert(0,ele)
		elif ele.tag == 'inputfile':
			source_elements.find('//inputfile').text+','+ele.text
		elif ele.tag == 'tolerance':
			continue
		else:
			source_value = int(source_element.find('//'+ele.tag).text)
			source_element.text = str(source_value + int(ele.text))

def iterate_path(path):
	reports = []
	for root,dirnames,filenames in os.walk(path):
		for fname in filenames:
			if fname.find('semantic')!=-1:
				reports.append(root+'/'+fname)
	print reports
	path_source = open(reports[0]).read()
	root_source = etree.XML(path_source)
	source_elements = root_source.getchildren()
	for report in reports[1:]:
		aggregate(source_elements,report)
	print etree.tostring(source_elements,pretty_print=True)

if __name__ == '__main__':
	dirpath = '/home/dxin/result/DenHaag'
	iterate_path(dirpath)
