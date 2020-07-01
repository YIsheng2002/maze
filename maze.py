#python maze game 

#map setting
py_map = [
    ["#","#","-","$","-"],
    ["#","-","-","#","-"],
    ["#","-","#","#","-"],
    ["#",".","-","#","-"],
    ["#","#","-","-","-"]
]

#current position
pos_x,pos_y=(1,3)

#running
running = True

#movement:up,left,down , right

def checkWin(pos,sign):
    global running,pos_x,pos_y

    if pos == "y":
        if py_map[pos_y + sign][pos_x] == "$":
            running = False
            print("You Win")
    elif pos == "x":
        if py_map[pos_y][pos_x + sign] == "$":
            running = False
            print("You Win")

def movement(move):
    global pos_x,pos_y

    if move == "right":
        checkWin("x",1)
        if py_map[pos_y][pos_x+1] == "-":
            pos_x += 1 
            showPos(">")
    elif move == "left":
        checkWin("x",-1)
        if py_map[pos_y][pos_x-1] == "-":
            pos_x -= 1 
            showPos("<")
    elif move == "up":
        checkWin("y",-1)
        if py_map[pos_y-1][pos_x] == "-":
            pos_y -= 1
            showPos("^")
    elif move == "down":
        checkWin("y",1)
        if py_map[pos_y+1][pos_x] == "-":
            pos_y += 1
            showPos("v")

def showPos(direction):
    py_map[pos_y][pos_x] = direction
    print(py_map)

print(py_map)

#game loop 

while running:
    step = input("What is your next step:(right,left,up,down)\n")
    movement(step)