#!/usr/bin/env python
# coding=utf-8
import sys
import pyxb
import pyxb.binding.basis
#import fish
import citygml.appearance_1_0
import citygml.building_1_0
import citygml.cgml
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
    #input = sys.stdin
    #t = input.readline()
    #if t:
    #   pathes = t.split()
    if sys.argv[1:]:
        pathes = sys.argv[1:]
    else:
        return
    dataset = []
    for i in pathes:
        print "Reading input file: %s" % i
        cgml_model = cgml2class(i)
        if cgml_model:
            dataset.append(cgml_model)
    return dataset

def cgml2class(xml_path):
    xml = open(xml_path).read()
    try:
        cgml_model = citygml.cgml.CreateFromDocument(xml,location_base=xml_path)
    except pyxb.ValidationError as e:
        print e.details()
    return cgml_model

if __name__ == "__main__":
    dataset = data_read()
    print "Files reading completely!"
    if len(dataset)==0:
        print "None Input!"
        pass 
    #feature_count = 0
    feature_property = dict()
    for data in dataset:
        feature_property.clear()
        feature_count = 0
        print "processing data %s" % data._location().locationBase
        if type(data)!=citygml.cgmlbase_1_0.CityModelType and \
           type(data)!=citygml.cgmlbase_2_0.CityModelType:
            print "skip this data"
            continue
        #fish = fish.ProgressFish(total=len(data.content()))
        print "Feature_Count in CityModel: %s" % len(data.content())
        for value in data.content():
            if type(value)==citygml._gml.FeaturePropertyType:
                feature_count+=1
                feature_type = type(value.Feature)._Name().split('}')
                if not feature_type or len(feature_type)!=2:
                    print "feature_type problem",feature_type,value.Feature
                    continue
                f_type = feature_type[1]
                if not feature_property.has_key(f_type):
                    feature_property[f_type] = 0
                    print "Insert key %s" % f_type
                feature_property[f_type]+=1
        print "%s has been processed completely!" % data._location().locationBase
        print "the amount of all thematic objects is %d" % feature_count
        for k in feature_property.keys():
            print "%s: %d" % (k,feature_property[k])
        print '\n'
