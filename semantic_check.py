#!/usr/bin/env python
# coding=utf-8

import sys
import cgml_reader
import numpy as np
import math
from geo_algorithm import *
from geo_primitives import *
from lxml import etree

def calculate(poly):
    polynormal = orient(poly)
    normal = (0,0,1)
    if polynormal==None:
        return None
    #return angle_d(orient(poly.poslist))
    return dot(polynormal,normal)

def parsing_report(path):
    geo_report = open(path).read()
    report_root = etree.XML(geo_report)
    return [f.text for f in report_root.findall('.//face')]

def semantic_check():
    if sys.argv[1]:
        path = sys.argv[1]
    else:
        print "please input the right parameter!"
        return
    data = cgml_reader.cgml2class(path)
    #print "start semantic validation"
    b_ids = cgml_reader.Building_output(data)
    #print "buildings total number: %d" % len(b_ids)
    global inputfile
    inputfile = path
    global invalid_faces
    if len(sys.argv)>3:
        r_path = sys.argv[3]
        invalid_faces = parsing_report(r_path)

    for poly in cgml_reader.polys.values():
        if poly.fid in invalid_faces:
            continue
        p_array = np.array(poly.poslist[0])
        p_array_trans = p_array.reshape(p_array.size/3,3).tolist()
        cosnormal = calculate(p_array_trans[:-1])
        if cosnormal==None:
            continue
        orientation = angle_d(cosnormal)
        #orientation = calculate(poly)
        poly.set_orientation(orientation)
        if (cosnormal>=math.cos(85 * math.pi / 180) or cosnormal<=math.cos(95 * math.pi / 180)) and (poly.role == 'WallSurface' or poly.role == 'InteriorWallSurface'):
            #print calculate(poly),poly.role
            poly.set_valid(False)
            #poly.set_planar(isPolyPlanar(p_array_trans[:-1],normal))
        elif cosnormal>=math.cos(175 * math.pi / 180) and (poly.role == 'GroundSurface' or poly.role == 'OuterFloorSurface'  or poly.role == 'FloorSurface'):
            #print calculate(poly),poly.role
            poly.set_valid(False)
            #poly.set_planar(isPolyPlanar(p_array_trans[:-1],normal))
        elif cosnormal<=math.cos(85 * math.pi / 180) and (poly.role == 'RoofSurface' or poly.role == 'OuterCeilingSurface'or poly.role == 'CeilingSurface'):
            #print calculate(poly),poly.role
            poly.set_valid(False)
            #poly.set_planar(isPolyPlanar(p_array_trans[:-1],normal))
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
    global invalid_outerceiling
    global invalid_outerfloor
    global invalid_floor
    global invalid_ground
    global invalid_interiorwall
    global inputfile
    global tolerance
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
            if building.invalidpolys:
                invalid_building+=1
    infile_node = etree.Element('inputfile')
    infile_node.text = inputfile
    root.append(infile_node)
    tolerance_node = etree.Element('tolerance')
    tolerance_node.text = str(tolerance)
    root.append(tolerance_node)
    building_node = etree.Element('buildings')
    building_node.text = str(len(b_ids))
    root.append(building_node)
    invalidbuilding_node = etree.Element('invalidbuildings')
    invalidbuilding_node.text = str(invalid_building)
    root.append(invalidbuilding_node)
    surfaces_node = etree.Element('surfaces')
    surfaces_node.text = str(len(cgml_reader.polys.values()))
    root.append(surfaces_node)
    invalidsurfaces_node = etree.Element('invalidsurfaces')
    invalidsurfaces_node.text = str(invalid_wall+invalid_roof+invalid_ground)
    root.append(invalidsurfaces_node)
    wall_node = etree.Element('walls')
    wall_node.text = str(cgml_reader.wall_count)
    root.append(wall_node)
    invalidwall_node = etree.Element('invalidwalls')
    invalidwall_node.text = str(invalid_wall)
    root.append(invalidwall_node)
    roof_node = etree.Element('roofs')
    roof_node.text = str(cgml_reader.roof_count)
    root.append(roof_node)
    invalidroof_node = etree.Element('invalidroofs')
    invalidroof_node.text = str(invalid_roof)
    root.append(invalidroof_node)
    ground_node = etree.Element('grounds')
    ground_node.text = str(cgml_reader.ground_count)
    root.append(ground_node)
    invalidground_node = etree.Element('invalidgrounds')
    invalidground_node.text = str(invalid_ground)
    root.append(invalidground_node)
    floor_node = etree.Element('floors')
    floor_node.text = str(cgml_reader.floor_count)
    root.append(floor_node)
    invalidfloor_node = etree.Element('invalidfloors')
    invalidfloor_node.text = str(invalid_floor)
    root.append(invalidfloor_node)
    ceiling_node = etree.Element('ceilings')
    ceiling_node.text = str(cgml_reader.ceiling_count)
    root.append(ceiling_node)
    invalidceiling_node = etree.Element('invalidceilings')
    invalidceiling_node.text = str(invalid_ceiling)
    root.append(invalidceiling_node)
    outerfloor_node = etree.Element('outerfloors')
    outerfloor_node.text = str(cgml_reader.outerfloor_count)
    root.append(outerfloor_node)
    invalidouterfloor_node = etree.Element('invalidouterfloors')
    invalidouterfloor_node.text = str(invalid_outerfloor)
    root.append(invalidouterfloor_node)
    outerceiling_node = etree.Element('outerceilings')
    outerceiling_node.text = str(cgml_reader.outerceiling_count)
    root.append(outerceiling_node)
    invalidouterceiling_node = etree.Element('invalidouterceilings')
    invalidouterceiling_node.text = str(invalid_outerceiling)
    root.append(invalidouterceiling_node)
    interiorwall_node = etree.Element('interiorwalls')
    interiorwall_node.text = str(cgml_reader.interiorwall_count)
    root.append(interiorwall_node)
    invalidinteriorwall_node = etree.Element('invalidinteriorwalls')
    invalidinteriorwall_node.text = str(invalid_interiorwall)
    root.append(invalidinteriorwall_node)
    window_node = etree.Element('windows')
    window_node.text = str(cgml_reader.window_count)
    root.append(window_node)
    door_node = etree.Element('doors')
    door_node.text = str(cgml_reader.door_count)
    root.append(door_node)
    closure_node = etree.Element('closures')
    closure_node.text = str(cgml_reader.closure_count)
    root.append(closure_node)

    return root

def surface_node(surface):
    global invalid_wall
    global invalid_roof
    global invalid_ground
    global invalid_building
    global invalid_outerceiling
    global invalid_outerfloor
    global invalid_floor
    global invalid_ceiling
    global invalid_interiorwall
    if cgml_reader.polys.has_key(surface):
        poly = cgml_reader.polys[surface]
        child = etree.Element('surface', ID=surface, type=poly.role)
        grandchild1 = etree.Element('validity')
        grandchild1.text = str(poly.valid)
        child.append(grandchild1)
        grandchild2 = etree.Element('orientation')
        grandchild2.text = str(poly.orientation)
        child.append(grandchild2)
        if not poly.valid:
            grandchild0 = etree.Element('code')
            role = poly.role
            if role == 'WallSurface':
                invalid_wall+=1
                grandchild0.text = 'S102'
            elif role == 'RoofSurface':
                invalid_roof+=1
                grandchild0.text = 'S103'
            elif role == 'GroundSurface':
                invalid_ground+=1
                grandchild0.text = 'S101'
            elif role == 'OuterFloorSurface':
                invalid_outerfloor+=1
                grandchild0.text = 'S104'
            elif role == 'OuterCeilingSurface':
                invalid_outerceiling+=1
                grandchild0.text = 'S105'
            elif role == 'FloorSurface':
                invalid_floor+=1
                grandchild0.text = 'S106'
            elif role == 'CeilingSurface':
                invalid_ceiling+=1
                grandchild0.text = 'S107'
            elif role == 'InteriorWallSurface':
                invalid_interiorwall+=1
                grandchild0.text = 'S108'
            child.append(grandchild0)          
            # grandchild3 = etree.Element('planar')
            # grandchild3.text = str(poly.planar)
            # child.append(grandchild3)
        return child
    elif cgml_reader.shells.has_key(surface):
        shell = cgml_reader.shells[surface]
        child = etree.Element('compositesurface', ID=surface, type='Compositesurface')
        for sh in shell.polylist:
            child.append(surface_node(sh))
        return child
    else:
        raise ValueError('generate error,%s' % surface)

def report_building(building,node_name):
    child = etree.Element(node_name, ID=building.fid)
    if building.buildingparts:
        for bp in building.buildingparts:
            grandchild=report_building(cgml_reader.buildings[bp],'buildingpart')
            if len(grandchild)!=0:
                child.append(grandchild)
    else:
        #if building.invalidpolys:
        for surface in building.surfaces:
            grandchild=surface_node(surface)
            child.append(grandchild)    

    return child
     

invalid_wall=0
invalid_ground=0
invalid_roof=0
invalid_building=0
invalid_outerceiling=0
invalid_outerfloor=0
invalid_floor=0
invalid_ceiling=0
invalid_interiorwall=0
inputfile=None
invalid_faces=list()
if len(sys.argv)>3:
    tolerance = int(sys.argv[2])
else:
    tolerance = 5.0
if __name__ == "__main__":
    bids = semantic_check()
    #print "Building amount:%d" % len(bids)
    root = write_report(bids)
    print etree.tostring(root,pretty_print=True)
