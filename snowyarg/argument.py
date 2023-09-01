"""
snowyarg - Simple and basic argument parser library in Python
Author: Karapatakis Aggelos 
<aggeloskarapatakis@outlook.com.gr>

snowyarg is only based on the intergreated sys module
"""
import sys # i mean, i am not gonna write my own sys.argv[] lol

arguments = [] # declaring arguments as a list - the reason we put it here is to avoid calling the below method a lot of times so it can improve effeciency
class Argument:
    @classmethod
    def ListAllArgs(starting=1, finish=100 , param=None):

        """
        Lists all arguments in the parent script.

        param:
                True if the filename argument will be included on the list


                False if the filename argument won't be included on the list
                *Any other input will be ignored and method will return nothing*            
        
        """
        if param == True:
            for i in range(0, finish): # looping from 0 (0 because it includes the filename) to finish (finish referred to as the parameter that is provided when called) in order to check if an arguments exists on this range
                try:
                    arguments.append(sys.argv[i]) # in case something is found, it is gonna be added to the list through sys.argv[i] -> i as the number of the current number location
                except IndexError: # if an argument doesnt exist on location i, an exception called IndexError is thrownm, but since we don't want that, we pass it and continue the process
                        continue
                finally: # there is not a need of below code, but it is good-to-have
                        if i == 100:
                            break
        elif param == False:
            for i in range(starting, finish): # looping from starting  (starting referred to as the parameter that is provieded when called) to finish (finish referred to as the parameter that is provided when called) in order to check if an arguments exists on this range
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
        
    @classmethod
    def arg(i):
        """
        Gets x argument in the parent script.      
        If x argument doesn't exist, it will return nothing
        """
        if arguments != []: # if the method ListAllArgs() has not been executed, it will execute now, but if it was already executed, it will grab the values from the already built array named 'arguments'
            return arguments[i] # simply returns the x value from the arguments array, considering that it is already built by the ListAllArgs() method
        else:
            return ListAllArgs(True)[i] # since the array doesn't contain anything, it is going to be built now, and return the value from it directly - this can be really helpful as the ListAllArgs() method is going to build the array and will not be re-built/re-generated for future calls
   
    @classmethod
    def GetCurrentFileName(): 
        """
        Gets the first argument in the parent script by the method ListAllArgs with the filename flag set to true.
        It should be that simple, unless there is something tricky going on   
        """

        if arguments != []: # this is explained in the arg(i) method 
            return arguments[0]
        else:
            return ListAllArgs(True)[0]