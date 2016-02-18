#!/usr/bin/env python
# coding=utf-8

import sys
import cgml_reader
from geo_algorithm import *
from geo_primitives import *

def calculate(poly):
    return angle_d(orient(poly.poslist))

def semantic_check():
    if sys.argv[1]:
        path = sys.argv[1]
    else:
        print "please input the right parameter!"
        return
    data = cgml_reader.cgml2class(path)
    b_ids = cgml_reader.Building_output(data)
    for poly in cgml_reader.polys.values():
        if calculate(poly)>tolerance and poly.role == 'WallSurface':
            poly.set_valid(False)
        elif 90 - calculate(poly)>tolerance and poly.role == 'GroundSurface':
            poly.set_valid(False)
        elif 90 - calculate(poly)>tolerance * 65 and poly.role == 'RoofSurface':
            poly.set_valid(False)
        else:
            continue
        for fid in poly.fid:
            if poly.polyid not in cgml_reader.buildings[fid].invalidpolys:
                cgml_reader.buildings[fid].add_invalidpoly(poly.polyid)
    return b_ids

def write_report(b_ids):
    global invalid_wall
    global invalid_roof
    global invalid_ground
    if b_ids == None:
        print "\n"
        return
    for b_id in b_ids:
        if not cgml_reader.buildings.has_key(b_id):
            print "miss building ID %s" % b_id
            continue
        building = cgml_reader.buildings[b_id]
        report_building(building)
    print "WallSurface:%f" % (float(invalid_wall)/float(cgml_reader.wall_count))
    print "RoofSurface:%f" % (float(invalid_roof)/float(cgml_reader.roof_count))
    print "GroundSurface:%f" % (float(invalid_ground)/float(cgml_reader.ground_count))



def report_building(building):
    global invalid_wall
    global invalid_roof
    global invalid_ground
    if building.buildingparts:
        for bp in building.buildingparts:
            report_building(cgml_reader.buildings[bp])
    else:
        print "Building ID:%s" % building.fid
        for poly in building.invalidpolys:
            if poly.role == 'WallSurface':
                invalid_wall+=1
            elif poly.role == 'RoofSurface':
                invalid_roof+=1
            elif poly.role == 'GroundSurface':
                invalid_ground+=1
            print "Polygon ID:%s,%s" % (poly.polyid,poly.role)
     

invalid_wall=0
invalid_ground=0
invalid_roof=0
tolerance = 10.0
if __name__ == "__main__":
    write_report(semantic_check())
 
