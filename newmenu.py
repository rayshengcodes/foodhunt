import functions
import pygame
from time import sleep
import datalist
from functions import menuoption
import pygame
import sys



locationasked =False
running = True


def secondarymenu():
    pygame.init()
    print("\n")
    user_location = functions.get_user_location()
    choice = menuoption()

    start = False
    for i in choice:
        if i == True:
            start = True


    if start:

        print("\n")

        data = datalist.canteendata
        if choice[0]: #rank
            data = functions.new_sort_by_rank(data)

        if choice[1]: #distance
            data = functions.new_sort_distance(data)

        if choice[3]: #price
            output = functions.new_search_by_price(data)
            data = output[0]
            pricepref = output[1]

        if choice[4]: #food
            output = functions.new_search_by_food(data)
            data = output[0]
            foodpref = output[1]

        if choice[5]: #halal
            data = functions.halal(data)

        print("\nProcessing your preferences...\n\n")
        sleep(2)

        if choice[4]:  # food
            print("We took into account your food preference, so all the canteens listed will all sell ",foodpref,"!",sep='')
        print("Of course we didn't forget about",end='')

        if choice[0]: #rank
            print(", the ranking of the canteen",end='')

        if choice[1]:  # distance
            print(", the distance of the canteen from your location",end='')

        if choice[3]:  # price
            print(", and your budget of $", pricepref,". ",sep='')

        if choice[5]:  # halal
            print("\nNo worries the food options are also Halal certified.")

        if choice[2]:  # busstop
            functions.find_bus(user_location)

        k = 1

        for i in data:
            print("\n",k,". ",i,end='',sep='') #prints canteen name
            k+=1
            print(" (",data[i]['Rating'],"*)", sep='',end='')
            print(" (", data[i]['Distance'],"m) : ", sep='', end='')#prints rating
            for j in data[i]['Food Price']:
                print(j, end=' ',sep=",")
                print("($",data[i]['Food Price'][j],")",end=", ",sep='')

        print("\n")
        sys.exit()
        pygame.quit()