import time
from colorama import Fore ,Style
from application.scripts.viewsScript import UxHomeSelec, navigate




def selectedIn(home_val):
    opt_selector = [1,2,3]

    print(Style.RESET_ALL+'\n\n Selecciona tu archivo: ')
    print(Fore.GREEN + """ 
        
    Introducir Path         [ 1 ]
    Seleccionar             [ 2 ]
    Ir al Home              [ 3 ]
    
    """)
    print(Style.RESET_ALL)

    try:
   
        opt_launch = input(':')

        if str(opt_launch) not in str(opt_selector):
            
            raise ValueError             

        return UxHomeSelec(opt_launch,home_val)

    except ValueError:

        print(Fore.RED + "\n⚠️  ERROR: Por favor, selecciona un valor valido.")
        time.sleep(1)
        return selectedIn(home_val)


def HomeorNoFound(home_val,opt_selec):
      
    print(Style.RESET_ALL+'\n\nSELECCIONE UNA OPCIÓN:')
    print(Fore.LIGHTGREEN_EX + Style.DIM + """ 
        
    Archivo de Imagen       [ 1 ]
    Archivo de Audio        [ 2 ]
    Archivo de Video        [ 3 ]
    Archivo de PDF          [ 4 ]
    Archivo .doc,csv,sql    [ 5 ]
    Otras Herramientas      [ 6 ]
    Salir                   [esc]        
    """)
    print(Style.RESET_ALL)

    try:
        
        home_val = input(':')

        if str(home_val) == "6":
            return navigate()
              
        if str(home_val) not in str(opt_selec):
            
            raise ValueError             

        selectedIn(home_val)
        
        return home_val

    except ValueError:

        print(Fore.RED + "\n⚠️  ERROR: Por favor, ingrese un número válido entre 0 y 6.")
        time.sleep(1)
        return HomeorNoFound(home_val,opt_selec)


    

