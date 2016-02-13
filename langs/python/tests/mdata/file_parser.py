#!/usr/bin/env python

import yaml
import json
import csv

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
    
