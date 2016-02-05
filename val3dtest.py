#!/usr/bin/env python
# coding=utf-8
from pyxb.utils import domutils
from pyxb.bundles.opengis.cityGMLBase_1_0 import CreateFromDOM
import pyxb.bundles.opengis.cityGMLBase_1_0 as cgmlbase_1_0
import pyxb.bundles.opengis.appearance_1_0
import pyxb.bundles.opengis.building_1_0
import pyxb.bundles.opengis.cityFurniture_1_0
import pyxb.bundles.opengis.cityObjectGroup_1_0
import pyxb.bundles.opengis.generics_1_0
import pyxb.bundles.opengis.landUse_1_0
import pyxb.bundles.opengis.relief_1_0
import pyxb.bundles.opengis.transportation_1_0
import pyxb.bundles.opengis.vegetation_1_0
import pyxb.bundles.opengis.waterBody_1_0
import pyxb.bundles.opengis.texturedSurface_1_0
import pyxb

path = "/Users/octeufer/OneDrive/3DGeo/Dataset/LOD2_4424_5482_solid.gml"
#p = CreateFromDOM(domutils.StringToDOM(open(path).read()))
xml = open(path).read()
def getxml():
    try:
        p = cgmlbase_1_0.CreateFromDocument(xml,location_base=path)
    except pyxb.ValidationError as e:
        print e.details()
    return p

#import pyxb.namespace
#print "\n".join([ _ns.uri() for _ns in pyxb.namespace.Namespace.AvailableNamespaces() ])
