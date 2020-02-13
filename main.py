import winapps
import argparse

def list_program() : 
    count = 1 
    for app in winapps.list_installed():
        print('\t[{}] '.format(count) + app.name) 
        count += 1 

def get_program(index) : 
    if index <= 0 : 
        raise Exception("Index start from 1.")
    app_list = list(winapps.list_installed()) 
    return app_list[index - 1] 

def program_info(program) : 
    print("\nProgram Info : ")
    print("\t[*] Name : " + program.name) 
    print("\t[*] Publisher : " + program.publisher)
    print("\t[*] Version : " + program.version)  

if __name__ == '__main__' : 
    parser = argparse.ArgumentParser(description='Project 2')  
    parser.add_argument('--list', help='List all installed program', action='store_true') 
    parser.add_argument('--index', help='Program installed index') 
    args = parser.parse_args() 
     
    if args.index is not None : 
        program = get_program(int(args.index))
    if args.list :
        if args.index is None:  
            list_program()
        else :  
            program_info(program)





     
