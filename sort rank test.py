import functions
from operator import itemgetter

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
    return new_dict


def new_sort_distance(user_location,data):
    distance_list = {}
    scale = 3.17723568367148  # in metres (1 pixel = 3.1777m)
    for i in data:
        temp_cord = data[i]['Coordinates']
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
    temp_dict = {}
    for i,j in sorted_distances:
        temp_dict[i] = data[i]
    return temp_dict