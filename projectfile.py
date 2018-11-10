import functions
import pygame,sys,menu
from time import sleep

pygame.init()

menu()

pygame.quit()


def budget():
    while True:
        try:
            return float(input("What is your budget?"))
        except ValueError:
            print("Please type numerals.")

# Search all canteens to return the food within the searched range
def search_by_price():
    pricefood = {}

    howmuch = budget()
    for i in datalist.canteendata:  # iterates canteens
        food = []  # temporary list
        for j in datalist.canteendata[i]['Food Price']:  # iterates food items
            x = datalist.canteendata[i]['Food Price'][j]  # j is the dishes name

            if x <= howmuch and x != 0:
                food.append(j)
        pricefood[i] = food
    print("The food within your budget at this places are")
    for key,val in pricefood.items():
        print (key, ':', val)

    return pricefood
