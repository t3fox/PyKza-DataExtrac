import webbrowser
import sys

from application.scripts.actionTool import TypeofLoad
 

def UxHomeSelec(opt_launch,home_val):


    if int(home_val) == 1:
        TypeofLoad(opt_launch,home_val)
        
    elif int(home_val) == 2:
        TypeofLoad(opt_launch,home_val)

    elif int(home_val) == 3:
        TypeofLoad(opt_launch,home_val)

    elif int(home_val) == 4:
        TypeofLoad(opt_launch,home_val)

    elif int(home_val) == 5:
        TypeofLoad(opt_launch,home_val)

    elif int(home_val) == 0:
        from application.view.selectorView import Bye
        Bye()    


def navigate():
    
    webbrowser.open('https://github.com/t3fox?tab=repositories')
    return sys.exit()
