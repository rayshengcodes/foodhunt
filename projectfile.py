#This is the start of our python program.
import pygame
from time import sleep,clock

def display_map():
 introScreenImage = pygame.image.load("NTU campus.png")
 screen = pygame.display.set_mode((900,700))
 screen.blit(introScreenImage,(0,0))
 pygame.display.flip()

#main program
running = True

while running:
    pygame.init()
    display_map()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        #closes the map on ESC key
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclick = pygame.mouse.get_pos()
            print(mouseclick)

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
    pass


#The function calculate the distance between two points.
#Keith
def distance_a_b (location_of_a,location_of_b):
    pass

#Display the sorted distances from user’s current location to each canteen in ascending order.
#Keith
def sort_distance(user_location,canteens_location):
    pass


#Search all canteens to return the canteen with wanted food
#Kevin
def search_by_food(foodname,foodlist_canteens):
    pass

#Display the canteens by rank
#Kevin
def sort_by_rank(ranklist_canteens):
    pass

#Search all canteens to return the food within the searched range
#Keith
def Search_by_price(price,foodlist_canteens):
    pass

#To return coordinate of a mouseclick
#Raysheng
def Mouseclick():
    pass

#allow use to update information of each canteen
def Update_information():
    pass

#allow use to get transport information from current location to the destination
def transport (user_location,dest_location):
    pass