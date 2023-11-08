# This script will periodically generate runtime.py list, which will run all the modules in the 
# modules-directory. After generating the file, it will then execute it to run all the modules.
# - modules-directory should contain only those .py files that are designed to be run.
# - each module should have contain a function named execute(), which will be run automatically
# - while this script is being run, user should be able to insert or remove modules in modules-directory
# - this uses sleep to time these events, but other options exists and can be implemented

# This will be the handler of modules and runtime executions
# Import only the needed functions from libraries
from os import listdir, system, name as os_name
from time import sleep

# Alter this to modify runtime ( i * seconds = runtime )
i = 5
# Alter this to modify wait time
seconds = 30

# Clear terminal for clean output
if os_name == "nt":
    system("cls")
else:
    system("clear")

# Run until runtime comes to end
while i != 0:
    print("Round countdown:", i)
    # Reset variables    
    module = ""

    # Check the contents of modules directory, listdir content might be different in linux (".modules")
    modules = []
    modules = listdir("modules")

    # Remove all other files/directories except .py files from module list
    for module in modules:
        if module.endswith(".py") == False:
            modules.remove(module)
    
    # If there are no files left, wait and go to next iteration 
    if len(modules) == 0:
        sleep(seconds)
        i -= 1
        continue

    # Read first line of each module, should be commented function call to be executed
    line = ""
    lines = []
    rm_module = []
    # Loop through modules
    for module in modules:
        try:
            # Open module and read the first line removing any leading and trailing spaces, # and \n
            file = open("modules/" + module, "r")
            line = file.readline().strip('# \n')
            # If the read line does not start with "exec", mark module to be removed
            if line.startswith("exec") == False:
                rm_module.append(module)
            # Otherwise, add line to lines list
            else:
                lines.append(line)
            file.close
        except IOError:
            # File read failed, print error msg, wait and try again
            print("Error: Couldn't read the file")
            sleep(seconds)
            continue
    # Remove invalid modules from modules list
    modules = [j for j in modules if j not in rm_module]
    
    # Remove .py ending from files
    for module in range(0, len(modules)):
        modules[module] = modules[module][:-3]

    # Try to (re)write runtime.py file (This is where to make alterations to that file, if needed)
    try:
        file = open("runtime.py","w")
        file.write("# This file run all the modules in modules-directory.\n")
        file.write("# This file will be rewritten periodically, do not make changes here.\n")
        # Write the code to create function runlist
        file.write("def runlist():\n")
        # Loop through modules and lines lists and write correct imports and function calls
        for j in range(0, len(modules)):
            file.write(f"\tfrom modules import {modules[j]}\n")
            file.write(f"\t{modules[j]}.{lines[j]}\n")
        # Write the command to execute runlist function
        file.write("\nrunlist()")
        file.close()
    except IOError:
        # File write failed, print error msg, wait and try again
        print("Error: Couldn't write the file")
        sleep(seconds)
        continue

    # Run this newly created runtime.py, this might need to be altered depending on os    
    if os_name == "nt":
        system("py runtime.py")
    else:
        system("python3 runtime.py")

    # Decrease iteration and wait before doing this again
    i -= 1
    if i != 0:
        sleep(seconds)
    print()
