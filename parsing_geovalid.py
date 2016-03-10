#!/usr/bin/env python
# coding=utf-8
from lxml import etree

def parsing_report(path):
    xml = open(path).read()
    root = etree.XML(xml)
    return [f.text for f in root.findall('.//face')]

if __name__="__main__":
    print "\n"
