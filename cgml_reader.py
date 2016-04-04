#!/usr/bin/env python
# coding=utf-8
import sys
import uuid
import pyxb
import pyxb.binding.basis
from geo_primitives import *
#from geo_algorithm import *
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
    pyxb.RequireValidWhenParsing(False) #do not validate xml file when parsing to binding instance

    try:
        cgml_model = citygml.cgml.CreateFromDocument(xml,location_base=xml_path)
    except pyxb.ValidationError as e:
        print e.details()
    return cgml_model

def Building_push(dataset):
    pass

def Building_output(data):
    b_ids = list()
    for value in data.content():
        if type(value)!=citygml._gml.FeaturePropertyType:
            continue
        if type(value.Feature)!=citygml.building_2_0.BuildingType and \
           type(value.Feature)!=citygml.building_1_0.BuildingType:
            continue
        building = value.Feature
        fid = Parsing_Building(building)
        b_ids.append(fid)
    return b_ids

def Parsing_Building(building):
    fid = str(building.id)
    bgobj = Building()
    for f in building.content():
        if type(f)==citygml.building_2_0.BoundarySurfacePropertyType or type(f)==citygml.building_1_0.BoundarySurfacePropertyType:
            role = str(f.BoundarySurface._element().name().localName())
            if f.BoundarySurface.lod2MultiSurface:
                if f.BoundarySurface.lod2MultiSurface.MultiSurface:
                    for ms in f.BoundarySurface.lod2MultiSurface.MultiSurface.content():
                        if type(ms)==citygml._gml.SurfacePropertyType:
                            bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
            if f.BoundarySurface.lod3MultiSurface:
                # if f.BoundarySurface.lod3MultiSurface.MultiSurface:
                #     for ms in f.BoundarySurface.lod3MultiSurface.MultiSurface.content():
                #         if type(ms)==citygml._gml.SurfacePropertyType:
                #             bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                for surf in f.BoundarySurface.content():
                    if type(surf)==citygml._gml.MultiSurfacePropertyType:
                        for ms in surf.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                    elif type(surf)==citygml.building_2_0.OpeningPropertyType or type(surf)==citygml.building_1_0.OpeningPropertyType:
                        for ms in surf.Opening.lod3MultiSurface.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                role_opening = surf.Opening._element().name().localName()
                                bgobj.add_surfaces(Parsing_Surface(ms,role_opening,fid))
            if f.BoundarySurface.lod4MultiSurface:
                # if f.BoundarySurface.lod4MultiSurface.MultiSurface:
                #     for ms in f.BoundarySurface.lod4MultiSurface.MultiSurface.content():
                #         if type(ms)==citygml._gml.SurfacePropertyType:
                #             bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                for surf in f.BoundarySurface.content():
                    if type(surf)==citygml._gml.MultiSurfacePropertyType:
                        for ms in surf.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                    elif type(surf)==citygml.building_2_0.OpeningPropertyType or type(surf)==citygml.building_1_0.OpeningPropertyType:
                        for ms in surf.Opening.lod4MultiSurface.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                role_opening = surf.Opening._element().name().localName()
                                bgobj.add_surfaces(Parsing_Surface(ms,role_opening,fid))
        elif type(f)==citygml.building_1_0.InteriorRoomPropertyType or type(f)==citygml.building_2_0.InteriorRoomPropertyType:
            Parsing_InnerRoom(f.Room,fid,bgobj)
        elif type(f)==citygml.building_1_0.BuildingPartPropertyType or type(f)==citygml.building_2_0.BuildingPartPropertyType:
            bgobj.add_buildingpart(Parsing_Building(f.BuildingPart))

    if building.lod1Solid:
        bgobj.add_solid(Parsing_Solid(building.lod1Solid.Solid,fid))
    if building.lod2Solid:
        bgobj.add_solid(Parsing_Solid(building.lod2Solid.Solid,fid))
    if building.lod3Solid:
        bgobj.add_solid(Parsing_Solid(building.lod3Solid.Solid,fid))
    if building.lod4Solid:
        bgobj.add_solid(Parsing_Solid(building.lod4Solid.Solid,fid))
    bgobj.set_fid(fid)
    bgobj.fid = fid
    buildings[fid]=bgobj
    return fid

def Parsing_InnerRoom(room,fid,bgobj):
    for f in room.content():
        if type(f)==citygml.building_2_0.BoundarySurfacePropertyType or type(f)==citygml.building_1_0.BoundarySurfacePropertyType:
            role = str(f.BoundarySurface._element().name().localName())
            if f.BoundarySurface.lod4MultiSurface:
            # if f.BoundarySurface.lod4MultiSurface.MultiSurface:
            #     for ms in f.BoundarySurface.lod4MultiSurface.MultiSurface.content():
            #         if type(ms)==citygml._gml.SurfacePropertyType:
            #             bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                for surf in f.BoundarySurface.content():
                    if type(surf)==citygml._gml.MultiSurfacePropertyType:
                        for ms in surf.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                bgobj.add_surfaces(Parsing_Surface(ms,role,fid))
                    elif type(surf)==citygml.building_2_0.OpeningPropertyType or type(surf)==citygml.building_1_0.OpeningPropertyType:
                        for ms in surf.Opening.lod4MultiSurface.MultiSurface.content():
                            if type(ms)==citygml._gml.SurfacePropertyType:
                                role_opening = surf.Opening._element().name().localName()
                                bgobj.add_surfaces(Parsing_Surface(ms,role_opening,fid))

def Parsing_BoundarySurface(BS):
    pass

def Parsing_Solid(Solid3D,fid):
#    if type(Solid.exterior) == citygml._gml.SurfacePropertyType:
#        Parsing_Surface(Solid.exterior)
#    if type(Solid.interior) == citygml._gml.SurfacePropertyType:
#        Parsing_Surface(Solid.interior)
    solid = Solid()
    solid.set_fid(fid)
    for sh in Solid3D.content():
        if type(sh) == citygml._gml.SurfacePropertyType:
            solid.add_shell(Parsing_Surface(sh))
    if solids.has_key(fid):
        solids[fid].append(solid)
    else:
        solids[fid] = solid
    return solid

def Parsing_Surface(surface,role=None,fid=None):
    global wall_count
    global roof_count
    global ground_count
    global outerceiling_count
    global outerfloor_count
    global closure_count
    global ceiling_count
    global interiorwall_count
    global floor_count
    global window_count
    global door_count
    if type(surface.Surface) == citygml._gml.CompositeSurfaceType:
        composid = surface.Surface.id
        if composid==None:
            composid = str(uuid.uuid1())
        #print composid
        if shells.has_key(composid):
            if shells[composid]:
                return composid
        shell = Shell()
        shell.set_shellid(composid)
        shell.shellid = composid
        for s in surface.Surface.content():
            if type(s) == citygml._gml.SurfacePropertyType:
                shell.add_poly(Parsing_Surface(s,role,fid))
        shells[composid] = shell
        return composid
    elif type(surface.Surface) == citygml._gml.PolygonType:
        polyid = surface.Surface.id
        #print polyid
        if polys.has_key(polyid):
            if polys[polyid]:
                if fid not in poly.fid:
                    poly.add_fid(fid)
                    return polyid
        poly = Polygon()
        #poly.poslist = list()
        for p in surface.Surface.content():
            if type(p) == citygml._gml.AbstractRingPropertyType:
                #poslist = p.Ring.posList.value()
                poslist = []
                for pos in p.Ring.content():
                    poslist.extend(pos.value())
                poly.add_pos(poslist)
        poly.set_role(role)
        if role == 'WallSurface':
            wall_count+=1
        elif role == 'RoofSurface':
            roof_count+=1
        elif role == 'GroundSurface':
            ground_count+=1
        elif role == 'ClosureSurface':
            closure_count+=1
        elif role == 'OuterCeilingSurface':
            outerceiling_count+=1
        elif role == 'OuterFloorSurface':
            outerfloor_count+=1
        elif role == 'FloorSurface':
            floor_count+=1
        elif role == 'CeilingSurface':
            ceiling_count+=1
        elif role == 'InteriorWallSurface':
            interiorwall_count+=1
        elif role == 'Window':
            window_count+=1
        elif role == 'Door':
            door_count+=1
        if fid not in poly.fid:
            poly.add_fid(fid)
        poly.polyid = polyid
        polys[polyid]=poly
        #poly.orient()
        return polyid
    elif surface.Surface == None:
        xlink = str(surface.href)
        if xlink[0] == "#":
            xlink = xlink[1:]
        return xlink
    elif type(surface.Surface) == citygml._gml.OrientableSurfaceType:
        xlink = str(surface.Surface.baseSurface.href)
        if xlink[0] == "#":
            xlink = xlink[1:]
        return xlink
    else:
        raise ValueError("Surface error,%s" % surface.Surface)


tolerance = 0.01
points = []
polys = dict()
shells = dict()
solids = dict()
buildings = dict()
wall_count = 0
roof_count = 0
ground_count = 0
outerceiling_count = 0
outerfloor_count = 0
closure_count = 0
ceiling_count = 0
interiorwall_count = 0
floor_count = 0
window_count = 0
door_count = 0
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
