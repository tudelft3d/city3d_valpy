#!/usr/bin/env python
# coding=utf-8
import sys
import pyxb
import citygml.appearance_1_0
import citygml.building_1_0
import citygml.cgml_1_0
import citygml.cgmlbase_1_0
import citygml.cityFurniture_1_0
import citygml.cityObjectGroup_1_0
import citygml.generics_1_0
import citygml.landUse_1_0
import citygml.relief_1_0
import citygml.vegetation_1_0
import citygml.waterBody_1_0
import citygml.transportation_1_0
import citygml.cgmlbase_2_0
import citygml.appearance_2_0
import citygml.bridge_2_0
import citygml.building_2_0
import citygml.cgml_2_0
import citygml.cityFurniture_2_0
import citygml.cityObjectGroup_2_0
import citygml.generics_2_0
import citygml.landUse_2_0
import citygml.relief_2_0
import citygml.transportation_2_0
import citygml.tunnel_2_0
import citygml.vegetation_2_0
import citygml.waterBody_2_0

def data_read():
    input = sys.stdin
    t = input.readline()
    if t:
        pathes = [i for i in t.split()]
    else:
        print "No input file!"
        return
    dataset = []
    for i in range pathes:
        print "Reading input file: i"
        xml = open(i).read()
        
def cgml2class(xml_path):
    xml = open(xml_path).read()
    try:
        cgml_model = cit


if __name__ = "__main__":

