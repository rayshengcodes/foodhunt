def get_number():
    num = int(input("Insert a number between 100 to 250"))
    count=0
    while True:
        if num >= 100 and num <= 250:
            return num
        else:
            count+=1
            if count>=3:
                return 250
            num = int(input("Insert a number between 100 to 250"))


def get_color():
    clr = input("Insert either r or b")
    count=0
    while True:
        if clr=="r":
            return (255, 0, 0)

        elif clr=="b":
            return (0, 0, 255)
        else:
            count+=1
            if count>=3:
                return (0, 255, 0)
            clr= input("Insert either r or b")

print(get_number())
print(get_color())