#!/usr/bin/env python

import yaml
from bs4 import BeautifulSoup as Soup

with open('inventory.yml','rb') as f_yaml, open('inventory.xml') as f_xml:
    yaml_settings = yaml.load(f_yaml)
    #print('YAML file:\n')
    #print(yaml_settings)

    soup = Soup(f_xml, 'xml')
    modnum = 0

    for chassis_info in soup.find_all('chassis'):
        print("Device model is: {}, serial number is: {}".format(
            chassis_info.find('description').text,
            chassis_info.find('serial-number').text)
        )

    print("\nModule list:")
    for c, mod in enumerate(soup.find_all('chassis-module'), 1):
        #print("{}, type {}".format(
        #    mod.find('name').text,
        #    mod.find('description').text)
        #)
        pass#print mod.next_sibling

    chassis_module = soup.find_all('chassis-module')
    for c, v in enumerate(chassis_module, 1):
        pass#print v.text

    # Working example
    #cm = soup.find('chassis-sub-module')
    ##print cm.children
    #print cm

    #for child in cm.children:
    #    print child.string.strip()

    #
    cm = soup.find_all('chassis-module')

    parte = soup.find('part-number')
    #print parte
    partes = parte.next_elements

    for part in partes:
        print part

    for sub in cm:
        #print sub.text
        if 'FPC' in sub.text:
            #print sub.text
            if 'PIC' in sub.text:
                pass#print dir(sub)
                for sub_sub in sub.children:
                    pass#print sub_sub



