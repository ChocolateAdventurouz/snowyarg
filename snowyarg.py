
# Maximum arguments: 100
# Όριο παραμέτρων: 100

import sys

def ListAllArgs(param=None):

    """
    Lists all arguments in the parent script.

    param:
              True if the filename argument will be included on the list


              False if the filename argument won't be included on the list
            *Any other input will be ignored and method will return nothing*            
    
    """
    arguments = [] # declaring arguments as a list

    if param == True:
        for i in range(0, 100): # looping from 0 (0 because it includes the filename) to 100 in order to check if an arguments exists on this range (have to implement it with a better way)
            try:
                arguments.append(sys.argv[i]) # in case something is found, it is gonna be added to the list through sys.argv[i] -> i as the number of the current number location
            except IndexError: # if an argument doesnt exist on location i, an exception called IndexError is thrownm, but since we don't want that, we pass it and continue the process
                    continue
            finally: # there is not a need of below code, but it is good-to-have
                    if i == 100:
                        break
    elif param == False:
        for i in range(1, 100): # looping from 1 (1 because it doesn't include the filename) to 100 in order to check if an arguments exists on this range (have to implement it with a better way)
            try:
                arguments.append(sys.argv[i]) # in case something is found, it is gonna be added to the list through sys.argv[i] -> i as the number of the current number location
            except IndexError: # if an argument doesnt exist on location i, an exception called IndexError is thrownm, but since we don't want that, we pass it and continue the process
                    continue
            finally: # there is not a need of below code, but it is good-to-have
                    if i == 100:
                        break           
    else:
         return   # ignoring all other inputs apart from True/False and returns nothing
    return arguments # returning all contents of the list to parent script
    
    
def GetCurrentFileName(): # not implemented
    return sys.argv[0] # should be that simple, unless there is something tricky going on 