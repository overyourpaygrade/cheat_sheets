#!/usr/bin/env python
#http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree

import yaml
import json
#from xml.etree import ElementTree as ET
#from lxml import etree
#import lxml
import lxml.etree as ET
from collections import defaultdict
from pprint import pprint

with open('inventory.yml','rb') as f_yaml, open('inventory.xml') as f_xml:
    yaml_settings = yaml.load(f_yaml)
    #print('YAML file:\n')
    #print(yaml_settings)

    ## lxml
    #parser = lxml.etree.XMLParser()
    #file_xml = lxml.etree.parse(f_xml,parser)
    #root = file_xml.getroot()

    #t_g = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}chassis-module'
    #for element in root.iterdescendants(tag=t_g):
    #    for elem in element.iterdescendants():
    #        print elem.text

    #all_info = f_xml.read()
    #root = ET.fromstring(all_info)
    #namespace = "{http://xml.juniper.net/junos/12.3R6/junos}"

    #for fpc in root.findall('//{0}chassis-module'.format(namespace)):
    #    if fpc.find('{0}name'.format(namespace)).text.split(" ")[0] == "FPC":
    #        desc = fpc.find('{0}description'.format(namespace)).text

    tree = ET.parse(f_xml)
    root = tree.getroot()
    tag1 = root[0].tag

    #t_g = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}chassis-module'
    #for node in tree.iter(tag='{}'.format(t_g)):
    #    # All I need is the text of the tag
    #    # print node.tag, node.attrib, node.text
    #    #print node.text  # Empty print
    #    #print node # prints 5. there are 5 module tags

    #    for nd in node.iter():
    #        print nd # Prints all the categories

    ## Get namespace for xml file
    namespace = root[0].tag[root[0].tag.find('{'):root[0].tag.find('}')+1]

    inventory_fpc = defaultdict(dict)
    inventory_opt = defaultdict(dict)

    for fpc in root.findall('.//{}chassis-module'.format(namespace)):
        if fpc.find('{}name'.format(namespace)).text.split(" ")[0] == "FPC":
            desc = fpc.find('{0}description'.format(namespace)).text
            slot = fpc.find('{0}name'.format(namespace)).text.split(" ")[1]
            serial = fpc.find('{0}serial-number'.format(namespace)).text
            model = fpc.find('{0}model-number'.format(namespace)).text

            inventory_fpc[slot].update( { 'model' : model } )
            inventory_fpc[slot].update( { 'serial' : serial } )

            #print desc, slot, serial, model

    for optic in root.findall('.//{}chassis-sub-sub-module'.format(namespace)):
        #serial = optic.find('{0}serial-number'.format(namespace)).text
        #description = optic.find('{0}description'.format(namespace)).text
        #fpc = optic.getparent().getparent().getparent().find('{0}name'.format(namespace)).text
        name = optic.find('{0}name'.format(namespace)).text
        pic = optic.getparent().find('{0}name'.format(namespace)).text
        fpc = optic.getparent().getparent().find('{0}name'.format(namespace)).text
        fpc_mod = optic.getparent().getparent().find('{0}model-number'.format(namespace)).text
        #intf = fpc.split(" ")[1]+"/"+ pic.split(" ")[1] +"/"+name.split(" ")[1]
        intf = pic.split(" ")[1] +"/"+name.split(" ")[1]
        fpc_num = fpc.split(' ')[1]
        pic_num = pic.split(' ')[1]

        inventory_opt[fpc_num].setdefault(pic_num, [])
        inventory_opt[fpc_num][pic_num].append(intf)


    #print pprint(dict(inventory_fpc))
    #print pprint(dict(inventory_opt))
    #print dict(inventory_opt)
    #print dict(inventory_fpc)

    for ky,vl in inventory_fpc.iteritems():
        inventory_opt.get(ky, {}).update(vl)

    #print pprint(dict(inventory_opt))

    with open('inventory.json') as j_file:
        j_template = json.load(j_file)

        for k_inv_opt,v_inv_opt in sorted(inventory_opt.iteritems()):

            fpc_model = inventory_opt[k_inv_opt]['model']
            print "FPC: {} -- {}\n".format(k_inv_opt,model)

            for template_item in j_template:

                if template_item in fpc_model:

                    for k_template in sorted(j_template[template_item].keys()):
                        for y in sorted(v_inv_opt.keys()):
                            if k_template in y:
                                print "\tPIC: {}".format(k_template)

                                for n in j_template[template_item][k_template]:
                                    match = 0
                                    for m in v_inv_opt[y]:
                                        if n in m:
                                            print "\t\t{} - {}".format(n, m)
                                            match = 1
                                    if match == 0:
                                        print "\t\t{} - {}".format(n,"Free")
                                print


    ## Prints submodule
    #tg = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}chassis-sub-sub-module'
    #for n in tree.iter(tag='{}'.format(tg)):
    #    for oh in n:
    #        print oh.text

    # Does work
    #tg2 = '{http://xml.juniper.net/junos/12.3R6/junos-chassis}name'
    #for elem in tree.iter('{}'.format(tg2)):
    #    print elem

    # Does not work
    #all_items = tree.findall('{}'.format(tg2))
    #for item in all_items:
    #    print dir(item)

    # Does not work
    #data = tree.find('{}'.format(t_g))
    #for da in data:
    #    print da

    #for p in tree.find('{}'.format(tg)):
    #    print p

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


