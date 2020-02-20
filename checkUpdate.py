import json 
from packaging import version 
from utils import * 
from termcolor import colored 

def checkUpdate() : 
    print("[" + colored("******", 'yellow') + "] Checking for update .......") 
    current_installed = json.load(open("Database/current_version.json", "r")) 
    new_version = json.load(open("Database/new_version.json", "r")) 
    for app in current_installed.keys() : 
        if version.parse(current_installed[app]) < version.parse(new_version[app]) : 
            print("\t[" + colored("***", 'green') + "] {} can update from {} to {}".format(app, current_installed[app], new_version[app]))