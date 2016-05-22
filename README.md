# city3d_valpy  

Validation of 3D city model based on CityGML. This project is a part of research topic "Quality control of 3D city models" in 3D geoinformation group, Delft University of Technology, the Netherlands.   

This software contain three main parts. First part is a tool that can generate python binding classes corresponding to XML schema components. These classes can be used to transfer CityGML instance into python class. Second part is a tiny parser aim at parsing Building in CityGML. Third part is a tool which can validate semantic information of 3D city model in CityGML and give a report.   

# class generation automatically 

An open source library PyXB is used to generate binding classes. A specific profile is created by ourselves, which contains XSDs in 0.4, 1.0, 2.0 for all of the feature classes.

# smart parser

A fast, low memory cost CityGML parser, extracting Building information from CityGML files.

# semantic validation

Semantic validation for BoundedBy surfaces in CityGML, based on the normal orientation.   

# For usage

For using this software, you need to install python package PyXB, lxml, Numpy.



	usage:
		1. valid_order.sh 
	    	cd working path,in bash shell environment.   
	    	sh valid_order.sh "inputfile.gml" "outputfilename.geo.xml" "tolerance" "resultfolder"    
	    2. iterator.sh
	    	cd working path
	    	bash iterator.sh "datapath" "document key word" "resultfolder" 





		    
