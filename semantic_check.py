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
            #print calculate(poly),poly.role
            poly.set_valid(False)
        elif 90 - calculate(poly)>tolerance and poly.role == 'GroundSurface':
            #print calculate(poly),poly.role
            poly.set_valid(False)
        elif 90 - calculate(poly)>tolerance * 65 and poly.role == 'RoofSurface':
            #print calculate(poly),poly.role
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
    print "WallSurface:%.5f%%" % (float(invalid_wall)/float(cgml_reader.wall_count)*100)
    print "RoofSurface:%.5f%%" % (float(invalid_roof)/float(cgml_reader.roof_count)*100)
    print "GroundSurface:%.5f%%" % (float(invalid_ground)/float(cgml_reader.ground_count)*100)



def report_building(building):
    global invalid_wall
    global invalid_roof
    global invalid_ground
    if building.buildingparts:
        for bp in building.buildingparts:
            report_building(cgml_reader.buildings[bp])
    else:
        if building.invalidpolys: 
            print "Building ID:%s" % building.fid
            for poly in building.invalidpolys:
                role = cgml_reader.polys[poly].role
                if role == 'WallSurface':
                    invalid_wall+=1
                elif role == 'RoofSurface':
                    invalid_roof+=1
                elif role == 'GroundSurface':
                    invalid_ground+=1
                print "Polygon ID:%s,%s" % (poly,role)
     

invalid_wall=0
invalid_ground=0
invalid_roof=0
tolerance = 10.0
if __name__ == "__main__":
    bids = semantic_check()
    print "Building amount %d" % len(bids)
    if cgml_reader.wall_count !=0 and cgml_reader.roof_count !=0 and cgml_reader.ground_count !=0:
        print "WallSurface amount %d" % cgml_reader.wall_count
        print "RoofSurface amount %d" % cgml_reader.roof_count
        print "GroundSurface amount %d" % cgml_reader.ground_count
        write_report(bids)
        print invalid_wall
        print invalid_roof
        print invalid_ground
     
