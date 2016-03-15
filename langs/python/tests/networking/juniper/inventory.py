#!/usr/bin/env python

import yaml
import xmltodict

with open('inventory.yml','rb') as f_yaml, open('inventory.xml') as fd:
    yaml_settings = yaml.load(f_yaml)
    print('YAML file:\n')
    print(yaml_settings)
    #print(yaml_settings[0]['name'])
    #print(yaml_settings[0]['ports'])

    #for line in yaml_settings[0]['ports']['10g']:
    #    print line

    mydict = xmltodict.parse(fd.read())

    cheat = {}

    for mod in mydict['rpc-reply']['chassis-inventory']['chassis']['chassis-module']:
        if "FPC" in mod['name']:
            print mod['name']
            print mod['model-number']

            for line in mod['chassis-sub-module']:
                print "Name: {}".format(line['name'])
                print "Desc: {}".format(line['description'])
                print "PNum {}".format(line['part-number'])

                if 'chassis-sub-sub-module' in line:

                    for fk in line['chassis-sub-sub-module']:
                        if not isinstance(fk, basestring):
                            for lin in yaml_settings[3]['pics'][0]['ports']['10g']:
                                if fk['name'] in lin:
                                    print "    subs:{} == {}".format(lin,fk['name'])
                        else:
                            li = line['chassis-sub-sub-module']['name']
                            for lin in yaml_settings[3]['pics'][0]['ports']['10g']:
                                if li in lin:
                                    print "    subs:{} == {}".format(lin,li)
                                else:
                                    print "    subs:{} == None".format(lin)
                print


