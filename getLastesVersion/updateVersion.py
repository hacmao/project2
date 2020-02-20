from code import * 
# import code
import sys 
import json 
import os 
import pkgutil

def updateVersion() : 
    data = {}
    for app in list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__) + '/code'])) :
        appname = eval(app + ".getName()") 
        print("update " + appname + " ....")
        data[appname] = eval(app + ".getVersion()") 
        
    ''' write to file json'''  
    if __file__ == ".\\updateVersion.py" : 
        f = open('../Database/new_version.json', 'w') 
    else : 
        f = open(os.path.dirname(os.path.dirname(__file__))  + '/Database/new_version.json', 'w') 
    json.dump(data, f) 

if __name__ == "__main__" : 
    updateVersion() 