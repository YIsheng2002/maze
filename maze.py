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

next_step=[]
pos_step=[]#possible step
queue=[]#queue

#Breadth first search algorithm

def bfs():
    global pos_step,next_step

    visited=[pos_y,pos_x]
    next_step.extend([(visited[-2]+1,visited[-1]),(visited[-2]-1,visited[-1]),(visited[-2],visited[-1]+1),(visited[-2],visited[-1]-1)])
    for coor in next_step:
        if py_map[coor[0]][coor[1]] == "-" or py_map[coor[0]][coor[1]] == "$":
            pos_step.append((coor[0],coor[1]))

    print(pos_step)
    next_step.clear()
    pos_step.clear()
    
"""
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
"""
#game loop 

while running:
    bfs()
    step = input("What is your next step:(right,left,up,down)\n")
    movement(step)