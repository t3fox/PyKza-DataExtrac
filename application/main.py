import sys

import time
from colorama import Fore
from pynput import keyboard
import threading

from application.view.selectorView import HomeorNoFound


class ExifScript:

    def __init__(self):
        self.opt_selec = [1,2,3,4,5]
        self.image = None
        self.audio = None
        self.video = None
        self.pdf = None
        self.docfile = None
        self.nofound = None

    def main(self):
        self.home_val = None

        # other

    def HomeView(self):

        
        print(Fore.LIGHTRED_EX +'\t[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        print(Fore.LIGHTRED_EX +'\t   [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')        
        print(Fore.LIGHTGREEN_EX + """
             
        0101         0100    101    1001010101100          01010111010       011010110110    1001010101    010110010
         0110      0101      001    1101                   1010     100      1010            11101        100     010
           0010  1001        011    1010                   0101     100      0011            100          01       10
            110001           001   0001100110             01100001001       10100100101     101           01       00
            011 101          111    1111                   1001   110        1100            001          10       01   
          1100    1101       011    1011         1001      0011     010      1011            10001        001     010    
         0101       0101     001    1100         0100      0100      1011    101010100001    1001001101    010011001     

              
              \n\t\t\t\t\t\t\t\t\t\t\t\t\t| V 1.0 | by | T3fox  |
        """)

        print(Fore.WHITE+'\t\t\t\tHerramienta de reconocimiento e investigacion para pentesting. \n\t\t\t\tEsta herramienta es meramente educativa. ')
        print(Fore.LIGHTRED_EX +'\t   [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        print(Fore.LIGHTRED_EX +'\t[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]')
        time.sleep(2.5)

        self.__init__()
        self.main()



        key_thread = threading.Thread(target=self.key_listen)
        key_thread.daemon = True
        key_thread.start()
        
        self.home_val = HomeorNoFound(self.home_val,self.opt_selec)
        
        while True:
            time.sleep(1)
        
        


    def on_press(self, key):
        try:
            if key == keyboard.Key.esc: 
                self.Bye()
        except AttributeError:
            pass

    def key_listen(self):
        
        try:
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
        except Exception as e:
            print(f"Key listener err - {e}")

    def Bye(self):
        
        print('...Finalizando...')
        return sys.exit()
        
        
        