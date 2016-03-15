#!/usr/bin/env python
#http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree

import yaml
from xml.etree import ElementTree as ET

with open('inventory.yml','rb') as f_yaml, open('inventory.xml') as f_xml:
    yaml_settings = yaml.load(f_yaml)
    #print('YAML file:\n')
    #print(yaml_settings)

    tree = ET.parse(f_xml)
    root = tree.getroot()

    tag1 = root[0].tag

    t_g = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}name'
    for node in tree.iter(tag='{}'.format(t_g)):
        print node.tag, node.attrib
        for nd in node:
            print nd.text

    tg = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}chassis-sub-sub-module'
    for n in tree.iter(tag='{}'.format(tg)):
        for oh in n:
            print oh.text

    for p in tree.iter(tag='{*}name'):
        print dir(p)

    tg2 = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}'
    for elem in tree.iterfind('{}'.format(tg2)):
        print elem

    #chassis1 = root[0]
    #chassis2 = root[0][0]
    #print chassis1, " chassis1"
    #print chassis2, " chassis2"

    #for g in root.iter('{}'.format(chassis1)):
    #    print g

    #for c in root.findall('chassis-module'):
    #    print c, c.tag, c.attrib

    #root_children = root.iter()
    #for ob in root_children:
    #    print ob

    #for ele in root.iter('{*}chassis'):
    #    s1 = ele.find('{*}description').text
    #    s2 = ele.find('{*}serial-number').text
