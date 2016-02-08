#!/bin/bash
pyxbgen --schema-location=CGML1_0/CityGML.xsd --module=cgml_1_0 \
	    --schema-location=CGML1_0/CityGML/appearance.xsd --module=appearance_1_0 \
	    --schema-location=CGML1_0/CityGML/building.xsd --module=building_1_0 \
	    --schema-location=CGML1_0/CityGML/cityFurniture.xsd --module=cityFurniture_1_0 \
	    --schema-location=CGML1_0/CityGML/cityObjectGroup.xsd --module=cityObjectGroup_1_0 \
	    --schema-location=CGML1_0/CityGML/generics.xsd --module=generics_1_0 \
	    --schema-location=CGML1_0/CityGML/landUse.xsd --module=landUse_1_0 \
	    --schema-location=CGML1_0/CityGML/relief.xsd --module=relief_1_0 \
	    --schema-location=CGML1_0/CityGML/texturedSurface.xsd --module=texturedSurface_1_0 \
	    --schema-location=CGML1_0/CityGML/transportation.xsd --module=transportation_1_0 \
	    --schema-location=CGML1_0/CityGML/vegetation.xsd --module=vegetation_1_0 \
	    --schema-location=CGML1_0/CityGML/waterBody.xsd --module=waterBody_1_0 \
	    --module-prefix=citygml10 \
	    --archive-to-file=cgml_1_0.wxs

