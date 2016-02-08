#!/bin/bash
pyxbgen --schema-location=CGML2_0/CityGML.xsd --module=cgml_2_0 \
	    --schema-location=CGML2_0/CityGML/appearance.xsd --module=appearance_2_0 \
	    --schema-location=CGML2_0/CityGML/bridge.xsd --module=bridge_2_0 \
	    --schema-location=CGML2_0/CityGML/building.xsd --module=building_2_0 \
	    --schema-location=CGML2_0/CityGML/cityFurniture.xsd --module=cityFurniture_2_0 \
	    --schema-location=CGML2_0/CityGML/cityObjectGroup.xsd --module=cityObjectGroup_2_0 \
	    --schema-location=CGML2_0/CityGML/generics.xsd --module=generics_2_0 \
	    --schema-location=CGML2_0/CityGML/landUse.xsd --module=landUse_2_0 \
	    --schema-location=CGML2_0/CityGML/relief.xsd --module=relief_2_0 \
	    --schema-location=CGML2_0/CityGML/texturedSurface.xsd --module=texturedSurface_2_0 \
	    --schema-location=CGML2_0/CityGML/transportation.xsd --module=transportation_2_0 \
	    --schema-location=CGML2_0/CityGML/tunnel.xsd --module=tunnel_2_0 \
	    --schema-location=CGML2_0/CityGML/vegetation.xsd --module=vegetation_2_0 \
	    --schema-location=CGML2_0/CityGML/waterBody.xsd --module=waterBody_2_0 \
	    --module-prefix=citygml20 \
	    --archive-to-file=cgml_2_0.wxs

