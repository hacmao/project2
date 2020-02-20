import sys 
import json 

url = json.load(open("../Database/vuln_url.json", 'r')) 
url[sys.argv[1]] = sys.argv[2]
json.dump(url, open("../Database/vuln_url.json", 'w'))