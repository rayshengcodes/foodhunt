# This is the start of our python program.
import pygame, math, operator
import datalist
import functions
from time import sleep, clock
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
    use_price = False
    use_distance = False
    use_food = False
    running = True
    display_choice()

    while running:
        xandy = mouseclick()
        x = xandy[0]
        y = xandy[1]
        if 135 < y < 190:
            if 23 < x < 176:
                if use_price == True:
                    print("You've unselected price as a criteria")
                    use_price = False
                elif use_price == False:
                    print("You've selected price as a criteria")
                    use_price = True
            if 274 < x < 428:
                if use_distance == True:
                    print("You've unselected distance as a criteria")
                    use_distance = False
                elif use_distance == False:
                    print("You've selected distance as a criteria")
                    use_distance = True
            if 525 < x < 679:
                if use_food == True:
                    print("You've unselected food available as a criteria")
                    use_food = False
                elif use_distance == False:
                    print("You've selected food available as a criteria")
                    use_food = True

        if 275 < x < 428 and 372 < y < 410:
            running = False
            pygame.display.flip()
            # pygame.display.quit()
            return use_price,use_distance,use_food


def get_user_location():
    display_map()
    print("Click on your current location")
    currentlocation = mouseclick()
    pygame.display.flip()
    pygame.display.quit()

    print("Great, the coordinates of your location now is", currentlocation)

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
def sort_distance(user_location):
    distance_list = {}
    scale = 3.17723568367148  # in metres (1 pixel = 3.1777m)
    for i in datalist.canteendata:
        temp_cord = datalist.canteendata[i]['Coordinates']
        cal_distance = distance_a_b(user_location, temp_cord)
        distance_list[i] = cal_distance * scale

    distance_list
    # print(distance_list)

    sorted_distances = sorted(distance_list.items(), key=operator.itemgetter(1))
    # print(sorted(distance_list.items(),key=operator.itemgetter(1)))

    # for x,y in sorted_distances:
    # print("For",x,"Distance is",y,"metres")
    # #used to help understand which one is nearer or further

    # for x,y in sorted_distances:
    # print(x,":",int(y),"metres")

    return sorted_distances


# Search all canteens to return the canteen with wanted food
# Kevin
def search_by_food():
 count=0
    # food_pref = input("What food are you looking at getting? ")
 while True:
    havefood = []
    choice_food = input("What would you like to have? ")
    for i in datalist.canteendata:
        # print(i)
        for j in datalist.canteendata[i]['Food Price']:
            # print(j)
            if j.lower() == choice_food.lower() and datalist.canteendata[i]['Food Price'][j]!=0:
                havefood.append(i)
    # print("The following places sells",foodname)
    #
    # for x in havefood:
    #     print(x)
    if len(havefood)==0:
     count+=1
     if count>=3:
         print("404, food not found")
         return havefood
     print("404, food not found")
    else:
        print("The following places sells: ", choice_food)
        for i in havefood:
            print(i)
        return havefood


# Display the canteens by rank

def sort_by_rank():
    ranklist_canteens = {}
    for i in datalist.canteendata:
        ranklist_canteens[i] = datalist.canteendata[i]['Rating']
    # put all the canteen name and rating into a new dictionary
    sorted_names = sorted(ranklist_canteens.items(), key=lambda kv: kv[1], reverse=True)
    # sort the dictionary in descending order and store in a new dictionary
    for key,val in sorted_names:
        print(key," (",val,"*)", sep="")
    return sorted_names


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
