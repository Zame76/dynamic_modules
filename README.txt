This is a proof of concept on how to create a Python script, which will allow modules to be added or removed 
while the code is being run.

Modules need to have a function that starts with word exec, which will be written and called in the runtime.py.
First line of each module needs to be commented function call, ie:
# execute()
or 
# exec(arg, arg)

It requires following files and directories:

MAIN-DIRECTORY:

modules (folder)
    Folder named modules is mandatory, it is used to import and export modules. Directory itself can be empty, 
    in which case no modules are run. 

start.py
    This is the main executable, it scans modules-directory and creates runtime.py-file, which contains the
    information to run all the modules. After creating this file, it will run it and then wait for a specified
    time to do this again. The code is documented and will provide more information of its function.

runtime.py
    If this file does not exist, it will automatically be created by start.py-file. Modifying this file is 
    futile as it will always be recreated by start.py-file

test.py
    This is an example of a module, that can be inserted in modules-directory while the start.py program is
    running.

MODULES-DIRECTORY:

modules_1.py
    This is an example of a module, that can be removed from modules-directory while the start.py program is
    running.

modules_2.py
    This is an example of a module, that can be removed from modules-directory while the start.py program is
    running.


Created with Python 3.12.0
 