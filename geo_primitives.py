#!/usr/bin/env python
# coding=utf-8

class Point(object):

    def __init__(self,pos=(0,0,0),fid=[],polyid=[]):
        self.pos = pos
        self.fid = fid
        self.polyid = polyid

    def set_pos(self,pos):
        self.pos = pos

    def add_fid(self,fid):
        self.fid.append(fid)

    def add_polyid(self,polyid):
        self.polyid.append(polyid)

class Polygon(object):

    def __init__(self,poslist=[],fid=[],polyid=None,role=None):
        self.poslist = poslist
        self.fid = fid
        self.polyid = polyid
        self.role = role

    def set_role(self,role):
        self.role = role

    def set_poslist(self,poslist):
        self.poslist = poslist

    def add_fid(self,fid):
        self.fid.append(fid)

    def set_polyid(self,polyid):
        self.polyid = polyid

    def add_pos(self,pos):
        self.poslist.add(pos)

    def det(a):
        return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

    def unit_normal(a,b,c):
        x = det([[1,a[1],a[2]],
                 [1,b[1],b[2]],
                 [1,c[1],c[2]]])

        y = det([[1,a[1],a[2]],
                 [1,b[1],b[2]],
                 [1,c[1],c[2]]])

        z = det([[1,a[1],a[2]],
                 [1,b[1],b[2]],
                 [1,c[1],c[2]]])
        
        magnitude = (x**2 + y**2 + z**2)**.5
        if magnitude == 0.0:
            raise ValueError("no magnitude")
        return (x/magnitude, y/magnitude, z/magnitude)

    def orient(self):
        self.normal = self.unit_normal(self.poslist[0][0],self.poslist[0][1],self.poslist[0][2])
        return self.normal

class Shell(object):
    
    def __init__(self,polylist=[],shellid=None,fid=None,role=None):
        self.polylist = polylist
        self.shellid = shellid
        self.fid = fid
        self.role = role

    def add_poly(self,poly):
        self.polylist.append(poly)

    def set_shellid(self,shellid):
        self.shellid = shellid

    def set_fid(self,fid):
        self.fid = fid

    def set_role(self,role):
        self.role = role

class Solid(object):

    def __init__(self,shelllist=[],solidid=None,fid=None,role=None):
        self.shelllist = shelllist
        self.solidid = solidid
        self.fid = fid
        self.role = role

    def add_shell(self,shell):
        self.shelllist.append(shell)
    
    def set_solidid(self,solidid):
        self.solidid = solidid

    def set_fid(self,fid):
        self.fid = fid

    def set_role(self,role):
        self.role = role

class Feature(object):
    
    def __init__(self,solids=[],surfaces=[],fid=None):
        self.solids = solids
        self.surfaces = surfaces
        self.fid = fid

    def add_solid(self,solid):
        self.solids.append(solid)

    def add_surfaces(self,surfaces):
        self.surfaces.append(surfaces)

    def set_fid(self,fid):
        self.fid.append(fid)

class Building(Feature):

    def __init__(self,buildingparts=[],solids=[],surfaces=[],fid=None):
        self.solids = solids
        self.surfaces = surfaces
        self.fid = fid
        self.buildingparts = buildingparts
    
    def add_buildingpart(self,buildingpart):
        self.buildingparts.append(buildingpart)

