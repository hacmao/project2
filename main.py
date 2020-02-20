import argparse
import json
import subprocess 
from termcolor import colored
from checkUpdate import checkUpdate 
from utils import * 
import sys 
sys.path.insert(1, 'getCVE') 
from checkVuln import checkVuln 

if __name__ == '__main__' : 
    parser = argparse.ArgumentParser(description='Project 2')  
    parser.add_argument('--list', help='List all installed program', action='store_true') 
    parser.add_argument('--updateDB', help='Update newest version into Database') 
    parser.add_argument('--support', help="List application support by this project", action='store_true') 
    parser.add_argument('--checkUpdate', help="Check update for supported applications", action='store_true')  
    parser.add_argument('--checkVulnerable', help="Search CVEdetails about installed version", action='store_true')
    args = parser.parse_args() 

    if args.list :
        list_program()

    if args.support : 
        print(colored("\n\n[****] App Support : ", "yellow"))
        print(open("Database/appSupport.txt", "r").read())

    if args.updateDB :
        if args.updateDB == 'ver' : 
            subprocess.call(['py3', '.\\getLastesVersion\\updateVersion.py']) 
    if args.checkUpdate : 
        checkUpdate()
    if args.checkVulnerable : 
        checkVuln()
    





     
