#!/usr/bin/env python

import yaml
import json
import csv
from xml.etree import ElementTree as ET

print("")

with open('settings.yml','rb') as f_yaml:
    yaml_settings = yaml.load(f_yaml)
    print('YAML file:\n')
    print(yaml_settings)

print("")

with open('settings.json','rb') as f_json:
    json_settings = json.load(f_json)
    print('JSON file:\n')
    print(json_settings)

print("")

with open('settings.csv','rb') as f_csv:
    csv_settings = list(csv.reader(f_csv))
    print('CSV file:\n')
    print(csv_settings)
    
print("")

with open('settings.xml', 'rb') as f_xml:
    xml_settings = ET.parse(f_xml)
    root = xml_settings.getroot()
    data = root.find('Data')

    all_data = []

    for observation in data:
        record = {}
        for item in observation:

            lookup_key = item.attrib.keys()[0]

            if lookup_key == 'Numeric':
                rec_key = 'NUMERIC'
                rec_value = item.attrib['Numeric']
            else:
                rec_key = item.attrib[lookup_key]
                rec_value = item.attrib['Code']

            record[rec_key] = rec_value

        all_data.append(record)

    print("XML File:\n")
    print all_data
