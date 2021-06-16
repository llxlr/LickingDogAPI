#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
https://zhuanlan.zhihu.com/p/54269963
"""

#from xml.etree import ElementTree as  etree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import ElementTree

from xml.dom import minidom

# generate root node
root = Element('root')

# generate first child-node head
head = SubElement(root, 'head')

# child-node of head node
title = SubElement(head, 'title')
title.text = "Well Dola!"

# generate second child-node body
body = SubElement(root, 'body')
body.text = "I Love Dola!"

tree = ElementTree(root)

# write out xml data
tree.write('result.xml', encoding = 'utf-8')