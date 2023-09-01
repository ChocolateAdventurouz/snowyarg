"""
snowyarg - Simple and basic argument parser library in Python
Author: Karapatakis Aggelos 
<aggeloskarapatakis@outlook.com.gr>

snowyarg is only based on the intergreated sys module
"""
import sys # i mean, i am not gonna write my own sys.argv[] lol

arguments = [] # declaring arguments as a list - the reason we put it here is to avoid calling the below method a lot of times so it can improve effeciency


class HelpArgument: # probably needs more writing

    shortarg=None # for example -h
    fullarg=None # for example --help
    helpText=None # for example 'this is a help text'
    exitAfterShown=None # if it is set to true, the script is going to stop the execution
    defaultHelpText = f"""
        This is a help text. More information soon
    """ # in case a helptext is not provided this will show up as the default text
    
    @classmethod
    def Setup(shortargument=None, fullargument=None, exitaftershown=None, helptext=None): # this method updates the variables defined above
        HelpArgument.shortarg=shortargument
        HelpArgument.fullarg=fullargument
        if helptext == None: # if the parameter is empty, helptext will be changed to the default text defined above
             HelpArgument.helpText=HelpArgument.defaultHelpText
        else:
            HelpArgument.helpText=helptext
        HelpArgument.exitAfterShown=exitaftershown
        return
    
    @classmethod
    def HelpShow():
         print(HelpArgument.helpText)
         if HelpArgument.exitAfterShown == True:
              sys.exit(1)
         else:
              return