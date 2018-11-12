from functions import display_choice,menuoption

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



menuoption()