import functions
import pygame
from time import sleep



locationasked =False
running = True

while running:
    mainmenu = input \
        ("\n*****************  MENU  *****************\n\n"
         "Choose one of the following options:\n\n"
         "A. Select your current location\n"
         "B. Search for specific food items\n"
         "C. Search for nearby food places\n"
         "D. Search for food within your budget\n"
         "E. Sort by ranking of canteens\n"
         "F. Update data stored\n\n"
         "Selected Choice (A-E): ")

    if mainmenu.isalpha():
        if mainmenu == 'A':
            current_location = functions.get_user_location()
            sleep(3)
            locationasked = True
            print("Loading menu...")
            sleep(3)

        if mainmenu == 'B':
            functions.search_by_food()
            sleep(4)
            print("Loading menu...")
            sleep(3)

        if mainmenu == 'C':
            if locationasked == True:
                choice_distance = functions.sort_distance(current_location)
                # print(choice_distance)
                print("The nearest 3 food places are:")
                for i in range(0, 3):
                    print(choice_distance[i][0], " (", int(choice_distance[i][1]), "m)", sep='')
                # print("We are using distance")
                print("Loading menu...")
                sleep(3)
            else:
                print("Please select option A to key in your location first")
                print("Loading menu...")
                sleep(3)

        if mainmenu == 'D':
            functions.search_by_price()
            print("Loading menu...")
            sleep(3)

        if mainmenu == 'E':
            functions.sort_by_rank()
            print("Loading menu...")
            sleep(3)

        if mainmenu == 'F':
            changemenu = input \
                ("\n*****************  MENU  *****************\n\n"
                 "Which data do you want to change?\n\n"
                 "A. Food Price in a specific canteen\n"
                 "B. Rating of a food place\n"
                 "C. Coordinates of a canteen\n\n"
                 "Selected Choice (A-C): ")


    else:
        print("Please key in a choice from A-F")