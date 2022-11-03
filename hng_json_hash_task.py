import json
import csv

import hashlib
m = hashlib.sha256()

csv_file_path = 'HNGi9 CSV FILE - Sheet1.csv'

data = {}
object_list = []

with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        series_number = row['Series Number']
        file_name = row['Filename']
        uuid = row['UUID']
        description = row['Description']
        gender = row['Gender']
        data[series_number] = row 
        output_json = {
            "format":"CHIP-0007",
            "name":file_name,
            "description":description,
            "minting_tool":"Team Engine",
            "sensitive_content": False,
            "series_number":series_number,
            "series_total":526,
            "attributes": [
                {"trait_type":"gender",
                "value":gender
                }
            ],
            "collection":{
                "name": "Zuri NFT Tickets for Free Lunch",
                "id":uuid,
                "attributes":[
                    {
                        "type":"description",
                        "value":"Rewards for accomplishments during HNGi9."
                    }
                ]
            }

        }
        json_object = json.dumps(output_json, indent=4)
        m.update(json_object.encode('utf-8'))

        hashed_key = m.hexdigest()
        print(hashed_key)

        output_json['hashed_key'] = hashed_key
        object_list.append(output_json)

with open('HNGi9 CSV FILE - Sheet1.output.csv', mode='w') as new_csv_file:
    fieldnames = ['Series Number','Filename','Name','Description','Gender','UUID','hashed_key']
    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for single_json_object in object_list:
        writer.writerow({'Series Number': single_json_object['series_number'], 
                        'Filename': single_json_object['name'],'Name': single_json_object['name'],
                        'Description': single_json_object['description'],'Gender': single_json_object['attributes'][0]['value'],
                        'UUID': single_json_object['collection']['id'], 'hashed_key': single_json_object['hashed_key']}),
