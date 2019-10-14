#import json
#import requests

#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#response = requests.get("https://api.eosn.io/v1/chain/get_table_rows")
#r = requests.post('https://api.eosn.io/v1/chain/get_table_rows',header = {"accept": "application/json"},data = {"code":"proxy4nation","table":"voters","scope":"proxy4nation","json": True, "limit": 2500})
#print(r.text)

import requests
import json

url = "https://eos.eosn.io/v1/chain/get_table_rows"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
}

data = json.dumps({
    "code":"proxy4nation",
    "table":"voters",
    "scope":"proxy4nation",
    "json": True,
    "limit": 2500
})

response = requests.post(url, data=data, headers=headers)
json = response.json()

print("owner,staked,referral")
for row in json['rows']:
	print(",".join([row['owner'], str(row['staked']), row['referral']]))

"""
curl --request POST \
  --url https://api.eosn.io/v1/chain/get_table_rows \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"code":"proxy4nation","table":"voters","scope":"proxy4nation","json": true, "limit": 2500}'
"""

