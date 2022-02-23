
import os
 
def ConsoleClear(): # Clear all output in console.
    # This works regardless of Operating System prevailing.
    try:
        from IPython import get_ipython
        get_ipython().magic("clear")
        get_ipython().magic("reset -f")
    except:
        pass
    return()  # End of function: Console_Clear 

def Paths_Get():
    # Get the current paths and file names of this app.
    #   https://docs.python.org/3/library/os.path.html
    FullPath = os.path.abspath(__file__)
    print("\nThis app's full path and file name: \n","    ", FullPath )
    
    FileName = os.path.basename(FullPath)
    print("\nThis app's file name: \n ","    ", FileName )
    
    ProjectPath = os.path.dirname(FullPath)
    print("\nPath to this app without file name: \n","     ",ProjectPath )
    
    return()  # End of function: Paths_Get

def Mainline():
    ConsoleClear()  #Clear all output in console.
    print("Version 1")
    Paths_Get()
    return()  # End of function: Mainline.
        
Mainline()   # Start run.