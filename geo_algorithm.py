#!/usr/bin/env python
# coding=utf-8
from geo_primitives import *

def snap_point(p1,p2):
    point1 = p1
    point2 = p2
    if type(p1)==Point and type(p2)==Point:
        point1 = p1.pos
        point2 = p2.pos
    dis = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5
    return dis
