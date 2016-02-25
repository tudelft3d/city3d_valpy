#!/usr/bin/env python
# coding=utf-8

import sys
import cgml_reader
from geo_algorithm import *
from geo_primitives import *
from lxml import etree

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
        orientation = calculate(poly)
        poly.set_orientation(90-orientation)
        if orientation>tolerance and poly.role == 'WallSurface':
            #print calculate(poly),poly.role
            poly.set_valid(False)
        elif 90 - orientation>tolerance and poly.role == 'GroundSurface':
            #print calculate(poly),poly.role
            poly.set_valid(False)
        elif 90 - orientation> 70-tolerance and poly.role == 'RoofSurface':
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
    global invalid_building
    root = etree.Element('Semantic')
    if b_ids == None:
        print "\n"
        return
    for b_id in b_ids:
        if not cgml_reader.buildings.has_key(b_id):
            print "miss building ID %s" % b_id
            continue
        building = cgml_reader.buildings[b_id]
        child = report_building(building,'building')
        if len(child):
            root.append(child)
            invalid_building+=1
    building_node = etree.Element('buildings')
    building_node.text = str(len(b_ids))
    root.append(building_node)
    invalidbuilding_node = etree.Element('invalidbuilding')
    invalidbuilding_node.text = str(invalid_building)
    root.append(invalidbuilding_node)
    surfaces_node = etree.Element('surfaces')
    surfaces_node.text = str(len(cgml_reader.polys.values()))
    root.append(surfaces_node)
    invalidwall_node = etree.Element('invalidwalls')
    invalidwall_node .text = str(invalid_wall)
    root.append(invalidwall_node)
    invalidroof_node = etree.Element('invalidroofs')
    invalidroof_node.text = str(invalid_roof)
    root.append(invalidroof_node)
    invalidground_node = etree.Element('invalidground')
    invalidground_node.text = str(invalid_ground)
    root.append(invalidground_node)

    return root

    #print "WallSurface:%.5f%%" % (float(invalid_wall)/float(cgml_reader.wall_count)*100)
    #print "RoofSurface:%.5f%%" % (float(invalid_roof)/float(cgml_reader.roof_count)*100)
    #print "GroundSurface:%.5f%%" % (float(invalid_ground)/float(cgml_reader.ground_count)*100)

def surface_node(surface):
    global invalid_wall
    global invalid_roof
    global invalid_ground
    global invalid_building
    if cgml_reader.polys.has_key(surface):
        poly = cgml_reader.polys[surface]
        child = etree.Element('surface', ID=surface, type=poly.role)
        grandchild1 = etree.Element('validity')
        grandchild1.text = str(poly.valid)
        child.append(grandchild1)
        if not poly.valid:
            grandchild2 = etree.Element('orientation')
            grandchild2.text = str(poly.orientation)
            child.append(grandchild2)
            role = poly.role
            if role == 'WallSurface':
                invalid_wall+=1
            elif role == 'RoofSurface':
                invalid_roof+=1
            elif role == 'GroundSurface':
                invalid_ground+=1
        return child
    elif cgml_reader.shells.has_key(surface):
        shell = cgml_reader.shells[surface]
        child = etree.Element('compositesurface', ID=surface, type='Compositesurface')
        for sh in shell.poslist:
            child.append(surface_node(sh))
        return child
    else:
        raise ValueError('generate error')

def report_building(building,node_name):
    # global invalid_wall
    # global invalid_roof
    # global invalid_ground
    # global invalid_building
    child = etree.Element(node_name, ID=building.fid)
    if building.buildingparts:
        for bp in building.buildingparts:
            grandchild=report_building(cgml_reader.buildings[bp],'buildingpart')
            if len(grandchild)!=0:
                child.append(grandchild)
    else:
        if building.invalidpolys:
            for surface in building.surfaces:
                grandchild=surface_node(surface)
                child.append(grandchild)    

            #print "Building ID:%s" % building.fid
            # for poly in building.invalidpolys:
            #     role = cgml_reader.polys[poly].role
            #     if role == 'WallSurface':
            #         invalid_wall+=1
            #     elif role == 'RoofSurface':
            #         invalid_roof+=1
            #     elif role == 'GroundSurface':
            #         invalid_ground+=1
            #     print "Polygon ID:%s,%s" % (poly,role)
    return child
     

invalid_wall=0
invalid_ground=0
invalid_roof=0
invalid_building=0
if sys.argv[2]:
    tolerance = int(sys.argv[2])
else:
    tolerance = 5.0
if __name__ == "__main__":
    bids = semantic_check()
    #print "Building amount:%d" % len(bids)
    if cgml_reader.wall_count !=0 and cgml_reader.roof_count !=0 and cgml_reader.ground_count !=0:
        #print "WallSurface amount:%d" % cgml_reader.wall_count
        #print "RoofSurface amount:%d" % cgml_reader.roof_count
        #print "GroundSurface amount:%d" % cgml_reader.ground_count
        root = write_report(bids)
        #print invalid_wall
        #print invalid_roof
        #print invalid_ground
        print etree.tostring(root,pretty_print=True)
