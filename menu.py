import functions
# import pygame
from time import sleep
import newmenu

def startmenu():
    locationasked =False
    running = True


    while True:
        mainmenu = input\
            ("\n*****************  MENU  *****************\n\n"
             "Choose one of the following options:\n\n"
             "A. Run the program\n"
             "B. Modify data values\n\n"
             "Selected Choice (A or B): ")

        if mainmenu.isalpha():
            if mainmenu.upper() == 'A':
                newmenu.secondarymenu()

            if mainmenu.upper() == 'B':

                while True:
                    changemenu = input \
                        ("\n*****************  MENU  *****************\n\n"
                         "Which data do you want to change?\n\n"
                         "A. Food Price in a specific canteen\n"
                         "B. Rating of a food place\n"
                         "C. Coordinates of a canteen\n"
                         "D. Return to menu\n\n"
                         "Selected Choice (A-D): ")
                    if changemenu == "A":
                        functions.update_price()
                        sleep(3)
                    if changemenu == "B":
                        functions.update_rating()
                        sleep(3)
                    if changemenu == "C":
                        functions.update_coordinate()
                        sleep(3)
                    if changemenu == "D":
                        sleep(2)
                        break
        else:
            print("Please key in a choice from A-F")