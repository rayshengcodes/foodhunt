#This is the start of our python program.
import pygame, math, operator
import datalist
from time import sleep,clock

display_width = 750
display_height = 786


black = (0,0,0)
white = (255,255,255)
red = (255,255,255)

def display_map():
     introScreenImage = pygame.image.load("img/Base.jpg")
     screen = pygame.display.set_mode((display_width,display_height))
     screen.blit(introScreenImage,(0,0))
     pygame.display.flip()


def display_choice():
    introScreenImage = pygame.image.load("img/choice.png")
    screen = pygame.display.set_mode((700, 431))
    screen.blit(introScreenImage, (0, 0))
    pygame.display.flip()

#main program


        #give coordinates on click
#End



# i. The user is asked to enter his/her location on NTU campus according 2D coordinates (row, column) if distance is a concern.
# ii. The user is asked to enter his inquiry criteria
# iii. The recommendation information displayed

# 1. Decomposition: (implement as major functions):
    # a. Information system set up, pre-store some information
    # b. Display the map to user
    # c. Allow user to update information
    # d. User inputs inquiry and get recommendation
    # e. Sort based on distance, price, or rank
# 2. Programming style with proper comments
# 3. Testing: Correctness of your solution.
# 4. Optional or advanced feature:


#Get user location either though console input or mouse click
#Raysheng
def get_user_location():
    print("Click on your current location")
    sleep(0)
    currentlocation = mouseclick()

    print("Great, the coordinates of your location now is", currentlocation)

    return currentlocation



#The function calculate the distance between two points.
#Keith
def distance_a_b (location_of_a,location_of_b):
    scale = 3.17723568367148 # in metres (1 pixel = 3.1777m)
    int_ax = int(location_of_a[0])
    int_ay = int(location_of_a[1])
    int_bx = int(location_of_b[0])
    int_by = int(location_of_b[1])

    x_distance = (int_ax - int_bx)**2
    y_distance = (int_ay - int_by)**2

    shortest_distance = math.sqrt(x_distance+y_distance)

    return shortest_distance

#Display the sorted distances from user’s current location to each canteen in ascending order.
#Keith
def sort_distance(user_location):
    distance_list = {}
    scale = 3.17723568367148  # in metres (1 pixel = 3.1777m)
    for i in datalist.canteendata:
        temp_cord = datalist.canteendata[i]['Coordinates']
        cal_distance = distance_a_b(user_location,temp_cord)
        distance_list[i] = cal_distance * scale

    distance_list
    #print(distance_list)

    sorted_distances = sorted(distance_list.items(),key=operator.itemgetter(1))
    #print(sorted(distance_list.items(),key=operator.itemgetter(1)))

    #for x,y in sorted_distances:
        #print("For",x,"Distance is",y,"metres")                        #used to help understand which one is nearer or further

    #for x,y in sorted_distances:
        #print(x,":",int(y),"metres")

    return sorted_distances


#Search all canteens to return the canteen with wanted food
#Kevin
def search_by_food(foodname):
    havefood = []
    #food_pref = input("What food are you looking at getting? ")
    for i in datalist.canteendata:
        #print(i)
        for j in datalist.canteendata[i]['Food Price']:
            #print(j)
            if j == foodname:
                havefood.append(i)
    # print("The following places sells",foodname)
    #
    # for x in havefood:
    #     print(x)
    return havefood


#Display the canteens by rank
#Kevin
def sort_by_rank():
    ranklist_canteens={}
    for i in datalist.canteendata:
        ranklist_canteens[i]=datalist.canteendata[i]['Rating']
    #put all the canteen name and rating into a new dictionary
    sorted_names = sorted(ranklist_canteens.items(), key=lambda kv: kv[1], reverse=True)
    #sort the dictionary in descending order and store in a new dictionary
    return sorted_names

#Search all canteens to return the food within the searched range
#Keith
def search_by_price(price,foodlist_canteens):
     pricefood = []
     # price threshold howmuch = input(float("What is your budget?"))
     for item in datalist.canteendata[i]['Food Price']:
          priceofitem = datalist.canteendata[i]['Food Price'][item]
          if priceofitem <= howmuch:
               pricefood.append(item)
          else:
               continue
     #print("The food within your budget at this place are:", pricefood)
     return pricefood    


#To return coordinate of a mouseclick
#Raysheng
def mouseclick():
    running = True

    while running:
        pygame.init()
        display_map()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            # closes the map on ESC key
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = pygame.mouse.get_pos()
                return (mouseclick)


#To return on user's choice
#Raysheng
def choiceclick():
    use_price = False
    use_distance = False
    use_food = False
    running = True

    while running:
        pygame.init()
        display_choice()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            # closes the map on ESC key
            if event.type == pygame.MOUSEBUTTONDOWN:
                choiceclick = pygame.mouse.get_pos()
                #print(choiceclick)
                x_cc = choiceclick[0]
                y_cc = choiceclick[1]
                if 135 < y_cc < 190:
                    #print("within range")
                    if 23 < x_cc < 176:
                        print("price selected")
                        use_price = True
                    elif 274 < x_cc < 428:
                        print("distance selected")
                        use_distance = True
                    elif 525 < x_cc < 679:
                        print("food selected")
                        use_food = True
                if 275 < x_cc < 428 and 372 < y_cc < 410:
                    running = False
                    pygame.display.quit()

    return (use_price,use_distance,use_food)


#allow use to update information of each canteen
def Update_information():
    pass

#allow use to get transport information from current location to the destination
def transport (user_location,dest_location):
    pass


# print("Hi there, welcome to foodhunt! Please click on your current location.")
#
current_location = get_user_location()
#
# "What is your criteria for today?" --> Image prompt
choice = choiceclick()
#print(choice)

#Use Price
if choice[0]:
    choice_price = input("What is your budget?")
    #print("We are using price")

#Use Distance
if choice[1]:
    choice_distance = sort_distance(current_location)
    #print(choice_distance)
    print("The nearest 3 food places are:")
    for i in range(0,3):
        print(choice_distance[i][0]," (",int(choice_distance[i][1]),"m)",sep='')
    #print("We are using distance")

#Use Food
if choice[2]:
    choice_food = input("What would you like to have? ")
    chosen_food = search_by_food(choice_food)
    print("The following places sells", choice_food)
    for i in chosen_food:
        print(i,end=', ')


pygame.quit()


