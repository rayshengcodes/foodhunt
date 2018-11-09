import functions

# print("Hi there, welcome to foodhunt! Please click on your current location.")
#
current_location = functions.get_user_location()
#
# "What is your criteria for today?" --> Image prompt
choice = functions.choiceclick()
#print(choice)

#Use Price
if choice[0]:
    choice_price = input("What is your budget?")
    #print("We are using price")

#Use Distance
if choice[1]:
    choice_distance = functions.sort_distance(current_location)
    #print(choice_distance)
    print("The nearest 3 food places are:")
    for i in range(0,3):
        print(choice_distance[i][0]," (",int(choice_distance[i][1]),"m)",sep='')
    #print("We are using distance")

#Use Food
if choice[2]:
    choice_food = input("What would you like to have? ")
    chosen_food = functions.search_by_food(choice_food)
    print("The following places sells", choice_food)
    for i in chosen_food:
        print(i,end=', ')


pygame.quit()

