#!/usr/bin/env python

import json
import lxml.etree as ET
from collections import defaultdict
from pprint import pprint

with open('inventory.json') as j_file, open('inventory.xml') as f_xml,\
        open('live_data.json') as l_file:

    j_template = json.load(j_file)
    live_data = json.load(l_file)

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
    # If option is sub-sub-sub it will only parse that which has MIC
    for optic in root.findall('.//{}chassis-sub-sub-module'.format(namespace)):
        #serial = optic.find('{0}serial-number'.format(namespace)).text
        #description = optic.find('{0}description'.format(namespace)).text
        name = optic.find('{0}name'.format(namespace)).text
        pic = optic.getparent().find('{0}name'.format(namespace)).text
        fpc = optic.getparent().getparent().find(\
                            '{0}name'.format(namespace)).text
        fpc_mod = optic.getparent().getparent().find(\
                            '{0}model-number'.format(namespace)).text
        intf = pic.split(" ")[1] +"/"+name.split(" ")[1]
        fpc_num = fpc.split(' ')[1]
        pic_num = pic.split(' ')[1]

        inventory_opt[fpc_num].setdefault(pic_num, [])
        inventory_opt[fpc_num][pic_num].append(intf)

        if 'PIC' in name:
            for hey in optic.findall('{0}chassis-sub-sub-sub-module'.format(\
                                     namespace)):
                xcvr = hey.find('{}name'.format(namespace)).text
                m_pic = hey.getparent().find('{}name'.format(namespace)).text
                m_mic = hey.getparent().getparent().find('{}name'.format(namespace)).text
                m_fpc = hey.getparent().getparent().getparent().find(\
                            '{}name'.format(namespace)).text

                #print xcvr, m_pic, m_mic, m_fpc

    #pprint(inventory_fpc)
    #pprint(inventory_opt)

    #Merge dictionaries
    for key,val in inventory_fpc.iteritems():
        inventory_opt.get(key, {}).update(val)

    #Go through the merged dictionary
    for k_inv_opt,v_inv_opt in sorted(inventory_opt.iteritems()):

        print "FPC: {} -- {}\n".format(k_inv_opt,inventory_opt[k_inv_opt]['model'])

        for template_item in j_template:
            fpc_model = inventory_opt[k_inv_opt]['model']

            if template_item in fpc_model:

                for tmpl_pic in sorted(j_template[template_item].keys()):
                    for inv_pic in sorted(v_inv_opt.keys()):
                        if inv_pic in tmpl_pic:

                            speed = j_template[template_item][tmpl_pic]['speed']
                            print "\tPIC: {} Speed: {}".format(tmpl_pic,speed)

                            for tmpl_ports in j_template[template_item][tmpl_pic]['ports']:
                                match = 0
                                for inv_ports in v_inv_opt[inv_pic]:
                                    if inv_ports in tmpl_ports:
                                        print "\t\t{}/{} - {}/{}".format(\
                                            tmpl_pic,tmpl_ports,tmpl_pic,inv_ports)
                                        match = 1
                                if match == 0:
                                    print "\t\t{}/{} - {}".format(\
                                        tmpl_pic,tmpl_ports,"Free")
                            print

'''
Should look somethin like this:
{
    "FPC" {
        "0" : {
            "0/0/0" : {
                "status" : "up",
                "present" : "yes"
                      }
              }
          }
}
'''
