# This script will periodically generate runtime.py list, which will run all the modules in the 
# modules-directory. After generating the file, it will then execute it to run all the modules.
# - modules-directory should contain only those .py files that are designed to be run.
# - each module should have contain a function named execute(), which will be run automatically
# - while this script is being run, user should be able to insert or remove modules in modules-directory
# - this uses sleep to time these events, but other options exists and can be implemented

# This will be the handler of modules and runtime executions
# Import only the needed functions from libraries
from os import listdir
from os import system
from time import sleep

# Alter this to modify runtime ( i * seconds = runtime )
i = 5
# Alter this to modify wait time
seconds = 30

# Clear terminal for clean output
system("cls")

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

    # Remove .py ending from files
    for module in range(0, len(modules)):
        modules[module] = modules[module][:-3]

    # Try to (re)write runtime.py file (This is where to make alterations to that file, if needed)
    try:
        file = open("runtime.py","w")
        file.write("# This file run all the modules in modules-directory.\n")
        file.write("# This file will be rewritten periodically, do not make changes here.\n")
        file.write("def runlist():\n")
        for module in modules:
            file.write(f"\tfrom modules import {module}\n")
            file.write(f"\t{module}.execute()\n")
        file.write("\nrunlist()")
        file.close()
    except IOError:
        # File write failed, print error msg, wait and try again
        print("Error: Couldn't write the file")
        sleep(seconds)
        continue

    # Run this newly created runtime.py    
    system("py runtime.py")

    # Decrease iteration and wait before doing this again
    i -= 1
    if i != 0:
        sleep(seconds)
    print()
