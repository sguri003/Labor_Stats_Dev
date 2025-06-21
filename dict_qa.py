import os            
import json
import requests
import csv
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
FILE_NM = 'DICT_OUT.CSV'
#blank dictionary
#open file
def str_json_meth():
    with open('json_ex.json', 'r') as f:  
        #load into dictionary
    #    my_dict = json.load(f)
    #    print(my_dict[0])
        #get string
        obj_json = json.loads(f.read())   
        print(obj_json['glossary']['title'])
        title_dict = obj_json['glossary']['title']
        print(title_dict)
        print(type(title_dict))

def json_dict():
    my_dict = {}
    with open('json_ex.json', 'r') as f:
        my_dict = json.load(f)
        print(my_dict['glossary']['title'])
#states example
#git==>https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-JSON/json_demo.py      
def read_st():
    my_dict = {}
    with open('states.json', 'r')as st:
        my_dict = json.load(st)
        print(my_dict)
        for x in my_dict['states']:
            #print(x['name'], x['abbreviation'], x['area_codes'])
            #del x['area_codes']
            break
    #REMOVING JSON DUMB IF EXISTS. 
    if os.path.exists('new_states.json'):
        os.remove('new_states.json')
        print('File removed')
    else:
        print('Creating File')
    with open('new_states.json', 'w') as f:
        json.dump(my_dict, f, indent=4, sort_keys=True)
    #iterate over all states in JSON sorted
    for k, v in my_dict.items():
        print(k + str(v))
    with open('JSON_CSV.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'area_code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in my_dict:
            writer.writerow({'name': key, 'area_code': my_dict[key]})
        

read_st()
    

