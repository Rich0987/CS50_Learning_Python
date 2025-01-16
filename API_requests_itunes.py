import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?ent=song&limit=2&term=" + sys.argv[1])
                                                                                #name an artist to search for
print(json.dumps(response.json(), indent=2))   # dumps the json file cleaner to read with an indent

object = response.json()
for result in object["results"]:
    print(result["trackName"])         # "results": [{"trackName": "Running with the Devil" ... }] key:value
                                        # prints value of "Running with the Devil"
                                        # change limit=1 for more results # currently 2... "You really got me"