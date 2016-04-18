# city3d_valpy  

Validation of 3D city model based on CityGML. This project is a part of research topic "Quality control of 3D city models" in 3D geoinformation group, Delft University of Technology, the Netherlands.   

This software contain two main parts for the time being. First part is a tool that can generate python binding classes corresponding to XML schema components. These classes can be used to transfer CityGML instance into python class. Second part is a tool that can validate semantic information of 3D city model in CityGML and give a report for the quality condition.   

# class generation automatically 

For the first part, an open source library PyXB is used to generate binding classes. A specific profile which contains XSDs in 0.4, 1.0, 2.0 for all of the feature classes. Then an algorithm which can extract geometric and semantic information from python classes to construct spatial model for the input of validation tool is built up.    

![building](https://cloud.githubusercontent.com/assets/4657104/14591357/556510ce-0510-11e6-8500-311f50d85bb5.png)

This algorithm is implemented in cgml_reader.py.     

# semantic validation

For the second part, the normal vector of each surface is calculated. A range chart of orientation corresponding to the normal vectors is built for validation rule.    

<img src="https://cloud.githubusercontent.com/assets/4657104/14591429/d84bd7d8-0511-11e6-8772-a3a09ac34e02.png" width="250">

The validation and report parts are implemented in semantic_check.py.    

batch processing for the whole workflow from data read to result report is realized in valid_order.sh and iterator.sh

	usage:
		1. valid_order.sh 
	    	cd working path,in bash shell environment.   
	    	sh valid_order.sh "inputfile.gml" "outputfilename.geo.xml" "tolerance" "resultfolder"    
	    2. iterator.sh
	    	cd working path
	    	bash iterator.sh "datapath" "document key word" "resultfolder" 

# result report

the software can output the validity result and the real orientation of the surface. The value of the orientation represent the angle between the normal vector and the standard vector we defined. Hence, the readers can understand the orientation of the surface in the real world.





		    
