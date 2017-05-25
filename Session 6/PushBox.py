#box-pusher
#map
#box
#destination

#set pusher coordinate
#rep: P
pusher_x = 1
pusher_y = 0

#set box coordinate
#rep: B

boxes = [
    {
    "x" : 3,
    "y" : 4
    },
    {
    "x" : 1,
    "y" : 2
    }
    ]
#set destination coordinate
#rep: D
dests = [
    {"x" : 6,
     "y" : 7
     },
    {"x" : 5,
     "y" : 8
     }
    ]
#set map_size
size_x = 9
size_y = 9

def is_in_map(size_x, size_y, x, y):
    return  0 <= x <size_x and 0 <= y <size_y

def check_overlap(x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

def check_box(x,y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return item

def print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests):
    for y in range(size_y):
        for x in range(size_x):
            if x == pusher_x and y == pusher_y:
                print("P",end="")
            elif check_overlap(x, y, boxes):
                print("B",end="")
            elif check_overlap(x, y, dests):
                print("D",end="")
            else:
                print("-",end="")
        print()

##    if i != pusher_y:
##        print("-"* size_y)
##    else:
##        print("{0}{1}{2}".format("-"*pusher_x,"P","-"*(size_x - pusher_x-1)))

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "w":
        dy = -1
    elif direction == "s":
        dy =  1
    elif direction == "a":
        dx = -1
    elif direction == "d":
        dx =  1
    else:
        print("Wrong move !!")
    return dx,dy

print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)

while True:
    
    direction = input("Next move? Please: w,a,s,d ")
    
    dx, dy = input_process(direction)
    
    if check_overlap(pusher_x + dx, pusher_y + dy, boxes):
        
        if is_in_map(size_x, size_y, pusher_x + dx, pusher_y + dy):
            pusher_x += dx
            pusher_y += dy
            box = check_box(pusher_x,pusher_y, boxes)
            box["x"] += dx
            box["y"] += dy
            
        else:
            print(" Box isn't in map")

    else:
        if is_in_map(size_x, size_y, pusher_x + dx, pusher_y + dy):
            pusher_x += dx
            pusher_y += dy
        else:
            print("Can't move out of the map")
        
    
    if check_overlap(pusher_x + dx, pusher_y + dy, boxes):

        for box in boxes:

            for dest in dests:
            
                if box["x"]==dest["x"] and box["y"]==dest["y"]:

                    print("Mission Complete!!!")

                break
    print_map(size_x, size_y, pusher_x, pusher_y, boxes, dests)
