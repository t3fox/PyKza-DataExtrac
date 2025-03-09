from pathlib import Path
from exiftool import ExifToolHelper
import sys
from colorama import Fore

from tkinter import *
from tkinter import filedialog



def TypeofLoad(opt,home_val):

    try:

        if int(opt) == 1:

            la_path = str(input('/. *.jpg *.png *.jpeg :'))    
            custom_path = Path(la_path)
            print("Path >",custom_path)

            with ExifToolHelper() as xif:

                for dat in xif.get_metadata(custom_path):

                    for k,v in dat.items():
                        print(Fore.LIGHTBLACK_EX + f"> {k} = {v} ")

            # xiff proccess
                
        if int(opt) == 2:

            try:

                file_typ =  Path(fileFormat(home_val))
                print("Path >",Path(file_typ))

                
                with ExifToolHelper() as xif:

                    for dat in xif.get_metadata(file_typ):

                        for k,v in dat.items():
                            print(Fore.LIGHTBLACK_EX + f"> {k} = {v} ")
                    
                    sys.exit()    
                                

            except Exception as e:
                print(Fore.RED + f"Error: {e}")
                sys.exit()

            # xiff proccess


        if int(opt) == 3:

            opt_selec = [1,2,3,4,5,0]
            home_val = None
            
            from application.view.selectorView import HomeorNoFound as goHome        
            goHome(home_val,opt_selec) 

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return TypeofLoad(opt,home_val)
        
        
def fileFormat(home_val):


    # if home_val 
    if int(home_val) == 1:
                
        root = Tk()
        root.withdraw()
        file_typ = filedialog.askopenfilename(title="Seleccionar una imagen",defaultextension=".jpg", filetypes=[("IMGS", "*.png *.jpg *.jpeg")])
        root.destroy()
        return file_typ

    elif int(home_val) == 2:
        
        root = Tk()
        root.withdraw()
        file_typ = filedialog.askopenfilename(title="Seleecciona un audio",defaultextension=".wav",filetypes=[("AUDIO","*.mp3 *.wav *.ogg")])
        root.destroy()
        return file_typ
    
    elif int(home_val) == 3:
        
        root = Tk()
        root.withdraw()
        file_typ = filedialog.askopenfilename(title="Seleecciona un Video",defaultextension=".mp4",filetypes=[("VIDEO","*.mp4 *.avi")])
        root.destroy()
        return file_typ
    
    elif int(home_val) == 4:        
        
        root = Tk()
        root.withdraw()
        file_typ = filedialog.askopenfilename(title="Seleecciona un DOC | PDF",defaultextension=".pdf",filetypes=[("DOC,PDF","*.doc *.pdf")])
        root.destroy()
        return file_typ
    
    elif int(home_val) == 5:
        
        root = Tk()
        root.withdraw()

        file_typ = filedialog.askopenfilename(title="Seleecciona un CSV | SQL",defaultextension=".csv",filetypes=[("CSV,SQL","*.csv *.sql")])
        root.destroy()
        return file_typ
