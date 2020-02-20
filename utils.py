from termcolor import colored
import json
import winapps

'''
convert appname to support appname 
'''
def getAppName(appname) :  
    appsupport = open("Database/appSupport.txt", "r").readlines() 
    for app in appsupport : 
        if appname.startswith(app.strip()) : 
            return app.strip()
    
'''
list program and update database  
'''
def list_program() :     
    print(colored("[****] LIST ALL PROGRAM INSTALLED IN THIS COMPUTER WHICH THIS PROJECT SUPPORTED", 'yellow'))
    data = {}
    count = 1 
    strcmp = lambda x, y : y if x in y else '\x00' 
    for app in winapps.list_installed():
        appName = getAppName(app.name) 
        if appName : 
            print('\n[{}] '.format(count) + "********************")
            program_info(app)
            data[appName] = app.version
            count += 1  
    
    f = open("Database/current_version.json", 'w') 
    json.dump(data, f) 



def program_info(program) : 
    print("Program Info : ")
    print("\t[" + colored("*", 'green') + "]" +  " Name : " + str(program.name))
    print("\t[" + colored("*", 'green') + "]" +  " Publisher : " + str(program.publisher))
    print("\t[" + colored("*", 'green') + "]" +  " Version : " + str(program.version)) 
