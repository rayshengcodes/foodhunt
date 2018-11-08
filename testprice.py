import datalist


def search_by_price():
    pricefood = {}
    howmuch = float(input("What is your budget?"))
    for i in datalist.canteendata:  #iterates canteens
        food =[] #temporary list
        for j in datalist.canteendata[i]['Food Price']: #iterates food items
            x = datalist.canteendata[i]['Food Price'][j] #j is the dishes name

            if x <= howmuch and x != 0:
                food.append(j)
        pricefood[i] = food
    print("The food within your budget at this place are:", pricefood)
    return pricefood

search_by_price()


