import requests
import pprint

resp = requests.get("https://stepik.org/api/courses/210064")
resp = resp.json()
pprint.pprint(resp['courses'][0]["learners_count"])
