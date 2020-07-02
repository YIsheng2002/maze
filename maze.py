#python maze game 

#map setting
py_map = [
    ["#","#","-","$","-"],
    ["#","-","-","#","-"],
    ["#","-","#","#","-"],
    ["#",".","-","#","-"],
    ["#","#","-","-","-"]
]

real_map = py_map[0][0]+","+py_map[0][1]+" "+py_map[0][2]+" "+py_map[0][3]+" "+py_map[0][4]+"/n"+py_map[1][0]+" "+py_map[1][1]+" "+py_map[1][2]+" "+py_map[1][3]+" "+py_map[1][4]+"/n"+py_map[2][0]+" "+py_map[2][1]+" "+py_map[2][2]+" "+py_map[2][3]+" "+py_map[2][4]+"/n"+py_map[3][0]+" "+py_map[3][1]+" "+py_map[3][2]+" "+py_map[3][3]+" "+py_map[3][4]+"/n"+py_map[4][0]+" "+py_map[4][1]+" "+py_map[4][2]+" "+py_map[4][3]+" "+py_map[4][4]+"/n"
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
    print(str(py_map[0])+"\n"+
    str(py_map[1])+"\n"+
    str(py_map[2])+"\n"+
    str(py_map[3])+"\n"+
    str(py_map[4])+"\n"
)

print(str(py_map[0])+"\n"+
    str(py_map[1])+"\n"+
    str(py_map[2])+"\n"+
    str(py_map[3])+"\n"+
    str(py_map[4])+"\n"
)

#game loop 

while running:
    step = input("What is your next step:(right,left,up,down)\n")
    movement(step)