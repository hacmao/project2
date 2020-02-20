import json 
from getCVE import get_vulnerable_ver 
from termcolor import colored 

def checkVuln() : 
    current_installed = json.load(open("Database/current_version.json", "r")) 
    urlCheck = json.load(open("Database/vuln_url.json", "r"))
    for app in current_installed.keys() : 
        check_version = current_installed[app] 
        url = urlCheck[app]
        print("[" + colored("*****", "green") + "] Checking Vulnerable in {} version {}".format(app, check_version)) 
        vuln_list = get_vulnerable_ver(check_version, url) 
        
        if len(vuln_list) == 0 : 
            print("No vulnerable")
        else : 
            for vuln in vuln_list[:3] : 
                vuln.get_info() 

if __name__ == "__main__" : 
    checkVuln()
