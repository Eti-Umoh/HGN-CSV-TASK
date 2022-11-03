import json
import csv

import hashlib
m = hashlib.sha256()

csv_file_path = 'NFT Naming csv - Team Engine.csv'

data = {}
object_list = []

with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        series_number = row['Series Number']
        file_name = row['FILE NAME']
        uuid = row['UUID']
        description = row['Description']
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
                "value":""
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

with open('NFT Naming csv - Team Engine.output.csv', mode='w') as new_csv_file:
    fieldnames = ['Series Number','FILE NAME','UUID','Description','hashed_key']
    writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for single_json_object in object_list:
        writer.writerow({'Series Number': single_json_object['series_number'], 
                        'FILE NAME': single_json_object['name'], 'UUID': single_json_object['collection']['id'], 
                        'Description': single_json_object['description'], 'hashed_key': single_json_object['hashed_key']}),
