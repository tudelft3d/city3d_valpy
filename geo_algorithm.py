#!/usr/bin/env python
# coding=utf-8
from geo_primitives import *
import math

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

def unit_normal(a,b,c):
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
        raise ValueError("no magnitude")
    return (x/magnitude, y/magnitude, z/magnitude)

def orient(poly):
    normal = unit_normal([poly[0][0],poly[0][1],poly[0][2]],
    					 [poly[0][3],poly[0][4],poly[0][5]],
    					 [poly[0][6],poly[0][7],poly[0][8]])
    return normal

def angle_d(normal):
	return math.degrees(math.acos((normal[0]**2+normal[1]**2)**0.5))