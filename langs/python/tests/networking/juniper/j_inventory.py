#!/usr/bin/env python

import json
import lxml.etree as ET
from collections import defaultdict
from pprint import pprint

with open('inventory.json') as j_file, open('inventory.xml') as f_xml:

    j_template = json.load(j_file)

    tree = ET.parse(f_xml)
    root = tree.getroot()
    tag1 = root[0].tag

    ## Get namespace for xml file
    namespace = root[0].tag[root[0].tag.find('{'):root[0].tag.find('}')+1]

    inventory_fpc = defaultdict(dict)
    inventory_opt = defaultdict(dict)

    # Go though fpcs and get model and serial
    for fpc in root.findall('.//{}chassis-module'.format(namespace)):
        if fpc.find('{}name'.format(namespace)).text.split(" ")[0] == "FPC":
            desc = fpc.find('{0}description'.format(namespace)).text
            slot = fpc.find('{0}name'.format(namespace)).text.split(" ")[1]
            serial = fpc.find('{0}serial-number'.format(namespace)).text
            model = fpc.find('{0}model-number'.format(namespace)).text

            inventory_fpc[slot].update( { 'model' : model } )
            inventory_fpc[slot].update( { 'serial' : serial } )

    # Go through sub sub modules and 
    for optic in root.findall('.//{}chassis-sub-sub-module'.format(namespace)):
        #serial = optic.find('{0}serial-number'.format(namespace)).text
        #description = optic.find('{0}description'.format(namespace)).text
        name = optic.find('{0}name'.format(namespace)).text
        pic = optic.getparent().find('{0}name'.format(namespace)).text
        fpc = optic.getparent().getparent().find('{0}name'.format(namespace)).text
        fpc_mod = optic.getparent().getparent().find('{0}model-number'.format(namespace)).text
        intf = pic.split(" ")[1] +"/"+name.split(" ")[1]
        fpc_num = fpc.split(' ')[1]
        pic_num = pic.split(' ')[1]

        inventory_opt[fpc_num].setdefault(pic_num, [])
        inventory_opt[fpc_num][pic_num].append(intf)

    #Merge dictionaries
    for ky,vl in inventory_fpc.iteritems():
        inventory_opt.get(ky, {}).update(vl)

    #Go through the merged dictionary
    for k_inv_opt,v_inv_opt in sorted(inventory_opt.iteritems()):

        fpc_model = inventory_opt[k_inv_opt]['model']
        print "FPC: {} -- {}\n".format(k_inv_opt,model)

        for template_item in j_template:

            if template_item in fpc_model:

                for k_template in sorted(j_template[template_item].keys()):
                    for y in sorted(v_inv_opt.keys()):
                        if k_template in y:
                            print "\tPIC: {}".format(k_template)
                            print "{}".format(j_template[template_item]['ports'])

                            for n in j_template[template_item][k_template]:
                                match = 0
                                for m in v_inv_opt[y]:
                                    if n in m:
                                        print "\t\t{}/{} - {}".format(k_template,n,m)
                                        match = 1
                                if match == 0:
                                    print "\t\t{}/{} - {}".format(k_template,n,"Free")
                            print


