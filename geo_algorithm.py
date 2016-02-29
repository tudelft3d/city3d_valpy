#!/usr/bin/env python
# coding=utf-8
from geo_primitives import *
import math
import numpy as np

def snap_point(p1,p2):
    point1 = p1
    point2 = p2
    if type(p1)==Point and type(p2)==Point:
        point1 = p1.pos
        point2 = p2.pos
    dis = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5
    return dis

def det(a):
   	return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

def unit_normal(a,b,c,poly):
    x = det([[1,a[1],a[2]],
             [1,b[1],b[2]],
             [1,c[1],c[2]]])

    y = det([[a[0],1,a[2]],
             [b[0],1,b[2]],
             [c[0],1,c[2]]])

    z = det([[a[0],a[1],1],
             [b[0],b[1],1],
             [c[0],c[1],1]])
     
    magnitude = (x**2 + y**2 + z**2)**.5
    if magnitude == 0.0:
    	c = poly.pop(2)
    	#print a,b,c
    	if len(poly)<3:
        	raise ValueError("no magnitude %s" % str(poly))
        else:
        	return unit_normal(a,b,poly[2],poly)
    return (x/magnitude, y/magnitude, z/magnitude)

def orient(poly):
	#end = len(poly[0])-1
    # p_array = np.array(poly[0])
    # p_array2 = p_array.reshape(p_array.size/3,3).tolist()
    normal = unit_normal(poly[0],poly[1],poly[2],poly)
    #if (normal[0]**2+normal[1]**2+normal[2]**2)**0.5
    return normal

def angle_d(normal):
	cos = (normal[0]**2+normal[1]**2)**0.5
	#return math.degrees(math.acos((normal[0]**2+normal[1]**2)**0.5))
	if math.fabs(cos)>1:
		#raise ValueError(str(normal[1]))
		cos = 1
	return math.degrees(math.acos(cos))

def isPolyPlanar(polypoints,normal):
    """Checks if a polygon is planar."""
    #-- Normal of the polygon from the first three points
    # try:
    #     normal = unit_normal(polypoints[0], polypoints[1], polypoints[2])
    # except:
    #     return False
    #-- Number of points
    npolypoints = len(polypoints)
    #-- Tolerance
    eps = 0.01
    #-- Assumes planarity
    planar = True
    for i in range (3, npolypoints):
        vector = [polypoints[i][0] - polypoints[0][0], polypoints[i][1] - polypoints[0][1], polypoints[i][2] - polypoints[0][2]]
        if math.fabs(dot(vector, normal)) > eps:
            planar = False
    return planar

def dot(a, b):
    """Dot product of vectors a and b."""
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
