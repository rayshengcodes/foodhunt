import pygame, math, operator
import datalist
import copy
import busstop
import functions
from time import sleep, clock
from operator import itemgetter

clock = pygame.time.Clock()


def display_map():
    introScreenImage = pygame.image.load("img/Base.jpg")
    screen = pygame.display.set_mode((750, 786))
    screen.blit(introScreenImage, (0, 0))
    pygame.display.flip()
    clock.tick(60)


def display_choice():
    introScreenImage = pygame.image.load("img/choice.png")
    screen = pygame.display.set_mode((700, 431))
    screen.blit(introScreenImage, (0, 0))
    pygame.display.flip()
    clock.tick(60)


def mouseclick():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            # closes the map on ESC key
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = pygame.mouse.get_pos()
                return mouseclick


def menuoption():
    use_rank = False
    use_distance = False
    use_busstop = False
    use_price = False
    use_food = False
    use_halal = False

    running = True
    display_choice()

    while running:
        xandy = mouseclick()
        x = xandy[0]
        y = xandy[1]

        if 135 < y < 190:
            if 23 < x < 176:
                if use_rank:
                    print("You've unselected rank as a criteria")
                    use_rank = False
                elif not use_rank:
                    print("You've selected rank as a criteria")
                    use_rank = True
            if 274 < x < 428:
                if use_distance:
                    print("You've unselected distance as a criteria")
                    use_distance = False
                elif not use_distance:
                    print("You've selected distance as a criteria")
                    use_distance = True
            if 525 < x < 679:
                if use_busstop:
                    print("You've unselected bus stop as a criteria")
                    use_busstop = False
                elif not use_distance:
                    print("You've selected bus stop as a criteria")
                    use_busstop = True

        if 238 < y < 297:
            if 23 < x < 176:
                if use_price:
                    print("You've unselected price as a criteria")
                    use_price = False
                elif not use_price:
                    print("You've selected price as a criteria")
                    use_price = True
            if 274 < x < 428:
                if use_food:
                    print("You've unselected food as a criteria")
                    use_food = False
                elif not use_food:
                    print("You've selected food as a criteria")
                    use_food = True
            if 525 < x < 679:
                if use_halal:
                    print("You've unselected halal as a criteria")
                    use_halal = False
                elif not use_halal:
                    print("You've selected halal as a criteria")
                    use_halal = True

        if 275 < x < 428 and 364 < y < 402:
            pygame.display.flip()
            #pygame.display.quit()
            return use_rank, use_distance, use_busstop,use_price,use_food,use_halal


def get_user_location():
    display_map()
    print("Click on your current location")
    currentlocation = mouseclick()
    pygame.display.flip()
    pygame.display.quit()

    print("Great, the coordinates of your location now is", currentlocation)
    scale = 3.17723568367148  # in metres (1 pixel = 3.1777m)
    for i in datalist.canteendata:
        temp_cord = datalist.canteendata[i]['Coordinates']
        cal_distance = distance_a_b(currentlocation, temp_cord)
        datalist.canteendata[i]['Distance']= int(cal_distance * scale)

    return currentlocation


# The function calculate the distance between two points.
def distance_a_b(location_of_a, location_of_b):
    scale = 3.17723568367148  # in metres (1 pixel = 3.1777m)
    int_ax = int(location_of_a[0])
    int_ay = int(location_of_a[1])
    int_bx = int(location_of_b[0])
    int_by = int(location_of_b[1])

    x_distance = (int_ax - int_bx) ** 2
    y_distance = (int_ay - int_by) ** 2

    shortest_distance = math.sqrt(x_distance + y_distance)

    return shortest_distance



# Display the sorted distances from user’s current location to each canteen in ascending order.


def new_sort_distance(data):
    distance_list = {}
    for i in data:
        distance_list[i] = data[i]['Distance']

    sorted_distances = sorted(distance_list.items(), key=operator.itemgetter(1))
    # print(sorted(distance_list.items(),key=operator.itemgetter(1)))

    # for x,y in sorted_distances:
    # print("For",x,"Distance is",y,"metres")
    # #used to help understand which one is nearer or further

    # for x,y in sorted_distances:
    # print(x,":",int(y),"metres")
    temp_dict = {}
    for i,j in sorted_distances:
        temp_dict[i] = data[i]

    for i in list(temp_dict):
        for j in list(temp_dict[i]['Food Price']):  # iterates food items
            if temp_dict[i]['Food Price'][j]==0:
               del temp_dict[i]['Food Price'][j]
    return temp_dict

# Search all canteens to return the canteen with wanted food
# Kevin



# Display the canteens by rank



def new_sort_by_rank(data):
    ranklist_canteens = {}
    for i in data:
        ranklist_canteens[i] = data[i]['Rating']
    # put all the canteen name and rating into a new dictionary
    sorted_names = sorted(ranklist_canteens.items(), key=lambda kv: kv[1], reverse=True)
    # sort the dictionary in descending order and store in a new dictionary
    new_dict = {}
    for key,val in sorted_names:
        new_dict[key] = data[key]

    for i in list(new_dict):
        for j in list(new_dict[i]['Food Price']):
            if new_dict[i]['Food Price'][j]==0:
                del new_dict[i]['Food Price'][j]



    return new_dict


def budget():
    while True:
        try:
            return float(input("What is your budget? "))
        except ValueError:
            print("Please type numerals.")

# Search all canteens to return the food within the searched range




# Allow use to get transport information from current location to the destination
def transport(user_location, dest_location):
    pass


def update_coordinate():
    k = input("Enter the canteen name to change its coordinates: ")
    n_x = input("Enter the new x coordinate")
    n_y = input("Enter the new y coordinate")
    datalist.canteendata[k]['Coordinates']= (n_x,n_y)


def update_rating():
    while True:
        j = input("Enter the canteen name to change its rating: ")
        n_rating = float(input("Enter the new rating"))
        if 0 <= n_rating <= 5:
            datalist.canteendata[j]['Rating']= n_rating
            break
        else:
            print("Error in input")


def update_price():
    getcanteen = input("Enter the canteen name to change a dish price: ")
    food = input("Enter the food item: ")
    price = float(input("Enter the new price: "))

    datalist.canteendata[getcanteen]['Food Price'][food] = price

    print("The price of ",food," has been changed to $", price,sep='')


def new_search_by_price(data):
    pricefood = dict(data)

    howmuch = budget()
    for i in list(pricefood):  # iterates canteens  # temporary list
        for j in list(pricefood[i]['Food Price']):  # iterates food items
            if pricefood[i]['Food Price'][j]>howmuch or pricefood[i]['Food Price'][j]==0:
               del pricefood[i]['Food Price'][j] # j is the dishes name
        if len(pricefood[i]['Food Price'])==0:
            del pricefood[i]

    # print("The food within your budget at this places are")
    return pricefood,howmuch


def new_search_by_food(data):
    count=0
     # food_pref = input("What food are you looking at getting? ")
    while count<3:
        newfoodlist=copy.deepcopy(data)
        choice_food = input("What would you like to have? ")
        for i in list(newfoodlist):
            for j in list(newfoodlist[i]['Food Price']):

                if j.lower() != choice_food.lower() or newfoodlist[i]['Food Price'][j]==0:
                    del newfoodlist[i]['Food Price'][j]

            if len(newfoodlist[i]['Food Price'])==0:
                del newfoodlist[i]

        if len(newfoodlist)==0:
            count+=1
            if count==3:
                continue
            print("404, food not found")
        else:
            return newfoodlist, choice_food

    print("Maximum tries reached!!")
    return data, choice_food




def find_bus(nearest_location):
    nearestbus = {}
    for i,y in busstop.stops.items():
        distance = distance_a_b((nearest_location),y)
        nearestbus[i] = distance
    nearestbus = sorted(nearestbus.items(), key=operator.itemgetter(1))
    wantedbus = nearestbus[0]
    print("The nearest bus stop is at ", wantedbus[0]," which is ",int(wantedbus[1]),".0m away",sep='')

def halal(data):
    halaldict = {}
    halald=copy.deepcopy(data)
    for i in list(halald):
        for j in list(halald[i]['Food Price']):  # iterates food items
            if halald[i]['Food Price'][j]==0:
               del halald[i]['Food Price'][j]
        if halald[i]['Halal']:
            halaldict[i]=halald[i]

    return halaldict
