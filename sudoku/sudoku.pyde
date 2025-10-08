grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]

entry_cell = []
correct_cell = []
num = []
temp = 0
status = 1
selected_cell = (-1, -1)
load = False

def draw_table():
    strokeWeight(3)
    line(0,height/3,width/2,height/3)
    line(0,height/3*2,width/2,height/3*2)
    
    line(width/2/3,0,width/2/3,height)
    line(width/2/3*2,0,width/2/3*2,height)
    strokeWeight(1)
    line(0,height/9,width/2,height/9)
    line(0,height/9*2,width/2,height/9*2)
    line(0,height/9*4,width/2,height/9*4)
    line(0,height/9*5,width/2,height/9*5)
    line(0,height/9*7,width/2,height/9*7)
    line(0,height/9*8,width/2,height/9*8)
    
    line(width/2/9,0,width/2/9,height)
    line(width/2/9*2,0,width/2/9*2,height)
    line(width/2/9*4,0,width/2/9*4,height)
    line(width/2/9*5,0,width/2/9*5,height)
    line(width/2/9*7,0,width/2/9*7,height)
    line(width/2/9*8,0,width/2/9*8,height)

def check_rule(board, row, col, num):
    # check row
    for i in range(9):
        if i != col and board[row][i] == num:
            return False

    # check column
    for i in range(9):
        if i != row and board[i][col] == num:
            return False

    # check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            r = box_start_row + i
            c = box_start_col + j
            if (r != row or c != col) and board[r][c] == num:
                return False

    return True


def find_entry_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j) #(row,col)
    return None

def sudoku():
    pos = find_entry_cell(grid)
    if(pos != None):
        row,col = pos
        for i in num:
            if(check_rule(grid,row,col,i)):
                grid[row][col]=i
                if(sudoku()):
                    return True
                grid[row][col]=0
            
        return False
    else:
        return True
                
def generate_game():
    sudoku()
    global answer
    answer = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(grid[i][j])
        answer.append(row)

    count = 0
    while count < 40:
        row = int(random(9))
        col = int(random(9))
        if (row, col) not in entry_cell:
            entry_cell.append((row, col))
            grid[row][col] = 0
            count += 1


def show():
    for i in range(9):
        for j in range(9):
            fill(0)
            textSize(20)
            cell_w = width/2 / 9
            cell_h = height / 9

            if selected_cell:
                sel_i, sel_j = selected_cell
                if i == sel_i or j == sel_j:
                    fill(220)
                    noStroke()
                    rect(j * cell_w, i * cell_h, cell_w, cell_h)
                    stroke(0)

            if (i, j) in correct_cell:
                fill(102, 255, 102)
                noStroke()
                rect(j * cell_w, i * cell_h, cell_w, cell_h)
                stroke(0)

            if grid[i][j] != 0:
                if (i, j) not in entry_cell:
                    fill(180, 220, 255)
                    noStroke()
                    rect(j * cell_w, i * cell_h, cell_w, cell_h)
                    stroke(0)
                else:
                    if(not check_rule(grid,i,j,grid[i][j])):
                        fill(180, 0, 0)
                        noStroke()
                        rect(j * cell_w, i * cell_h, cell_w, cell_h)
                        stroke(0)

            if grid[i][j] != 0:
                fill(0)
                textAlign(CENTER, CENTER)
                text(grid[i][j], j * cell_w + cell_w / 2, i * cell_h + cell_h / 2)

                if grid[i][j] != answer[i][j]:
                    fill(255, 0, 0)
                    noStroke()
                    rect(j * cell_w, i * cell_h, cell_w, cell_h)
                    stroke(0)
                    fill(0)
                    text(grid[i][j], j * cell_w + cell_w / 2, i * cell_h + cell_h / 2)

def interface():
    if(status == 1):
        background(200)
        fill(0)
        textSize(100)
        text("sudoku",(width-300)/2,150)
        textSize(50)
        text("new game",(width-200)/2,height-400)
        text("load game",(width-200)/2,height-200)
        
        line(width/2-120,height-450,width/2+125,height-450)
        line(width/2-120,height-380,width/2+125,height-380)
        line(width/2-120,height-450,width/2-120,height-380)
        line(width/2+125,height-450,width/2+125,height-380)
        
        line(width/2-120,height-250,width/2+125,height-250)
        line(width/2-120,height-180,width/2+125,height-180)
        line(width/2-120,height-250,width/2-120,height-180)
        line(width/2+125,height-250,width/2+125,height-180)

def load_game():
    global answer, grid, entry_cell, status

    entry_cell = []
    answer = []
    grid = []

    f = open("save_game.txt", "r")

    for i in range(9):
        line = f.readline().strip()
        str_values = line.split(",") 
        row = []
        for v in str_values:
            if v != '':
                row.append(int(v))

        answer.append(row)

        copied_row = []
        for val in row:
            copied_row.append(val)

        grid.append(copied_row)


    header = f.readline().strip()
    if header != "ENTRY_CELL":
        print("error")
        f.close()
        return


    while True:
        line = f.readline()
        if not line:
            break
        coords = line.strip().split(",")
        if len(coords) == 2:
            r = int(coords[0])
            c = int(coords[1])
            entry_cell.append((r, c))

            for i in range(9):
                for j in range(9):
                    if i == r and j == c:
                        grid[i][j] = 0

    f.close()
    status = 2

def save_game():
    f = open("save_game.txt", 'w')
    #------------------------------save answer----------------------
    for r in range(9):
        for c in range(9):
            f.write(str(answer[r][c]) + ",")
        f.write("\n")
#------------------------------save entry cell----------------------
    f.write("ENTRY_CELL\n")
    for cell in entry_cell:
        f.write(str(cell[0])+","+str(cell[1])+"\n")
    f.close()
        
def mousePressed():
    global selected_cell,status
    if (status==1):
        x = mouseX
        y = mouseY
        if(width/2-120<x<width/2+125 and height-450<y<height-380):
            print("new")
            status = 2
        elif(width/2-120<x<width/2+125 and height-250<y<height-180):
            print("load")
            load_game()
            
    if(status != 1):
        cell_w = width/2 / 9
        cell_h = height / 9
        col = int(mouseX // cell_w)
        row = int(mouseY // cell_h)
        if 0 <= row < 9 and 0 <= col < 9:
            if (row, col) in entry_cell:
                selected_cell = (row, col)
            else:
                selected_cell = (-1, -1) 

    
def keyPressed():
    global status, correct_cell
    if selected_cell == (-1, -1):
        return
    row, col = selected_cell
    if key in ['1','2','3','4','5','6','7','8','9'] and status==2:
        if (row, col) in entry_cell:
            grid[row][col] = int(key)
    elif key == '0' or key == DELETE:
        if (row, col) in entry_cell:
            grid[row][col] = 0

    correct_cell = []
    for r, c in entry_cell:
        if grid[r][c] == answer[r][c]:
            correct_cell.append((r, c))
    if key == 's':
        print("save")
        save_game()
    if grid == answer:
        status = 3

#-------------------------------------------------------------flow-chart------------------------------------------------------
def flow_s(x,y): 
    fill(0,255,0) 
    ellipse(x,y,110,50) 
    fill(0) 
    text("start",x,y) 
    textSize(35) 

def flow_e(x,y,s): 
    if s == 0:
        fill(255)
    else:
        fill(0,255,0) 
    ellipse(x,y,110,50) 
    fill(0) 
    text("end",x-25,y) 
    textSize(35) 

def flow_o(x, y, t, s):
    w = textWidth(t) + 20 
    h = 40 
    if s == 1:
        fill(0, 255, 0) 
    else:
        fill(255)
    rect(x, y, w, h)
    fill(0) 
    textSize(35) 
    textAlign(LEFT, CENTER) 
    text(t, x + 10, y + h / 2) 

def flow_c(x, y, t, s): 
    textSize(20) 
    w = textWidth(t) + 350 
    h = 70 
    stroke(0) 
    strokeWeight(2) 
    left_x = x - w / 2 
    right_x = x + w / 2 
    top_y = y - h / 2 
    bottom_y = y + h / 2 
    if s == 1:
        fill(0, 255, 0) 
    else:
        fill(255, 0, 0)
    beginShape() 
    vertex(x, top_y)
    vertex(right_x, y) 
    vertex(x, bottom_y) 
    vertex(left_x, y) 
    endShape(CLOSE) 
    fill(0) 
    textAlign(CENTER, CENTER) 
    textSize(35) 
    text(t, x, y)
       
def flowchart(x,y):
    r,c = selected_cell
    flow_s(x,y) 
    flow_o(x-100,y+50,"create sudoku",1)
    if(grid == answer):
        s1 = 1
    else:
        s1 = 0
    flow_c(x+5,y+160,"All the answer are correct?",s1)
    if grid[r][c] != 0:
        s2 = 1
    else:
        s2 = 0
    flow_c(x+5,y+270,"Have the answer from player?",s2)
    if (r, c) in correct_cell and grid[r][c] != 0:
        s3 = 1
        s4 = 0
    elif grid[r][c] == 0:
        s3 = 0
        s4 = 0
    else:
        s3 = 0
        s4 = 1
    flow_c(x+5,y+380,"Is the answer correct?",s3)
    flow_o(x+120,y+470,"Let the box be green",s3)              
    flow_o(x-400,y+470,"Let the box be red",s4)                     
    flow_e(x,y+625,s1)                            
#-----------------------------------------arrow------------------------------
    fill(0)
    textSize(20)
    line(x,y+25,x,y+50)
    line(x-5,y+40,x,y+50)
    line(x+5,y+40,x,y+50)
    
    line(x,y+90,x,y+125)
    line(x-5,y+115,x,y+125)
    line(x+5,y+115,x,y+125)
    
    text("No",x+10,y+215)
    line(x,y+195,x,y+235)
    line(x-5,y+225,x,y+235)
    line(x+5,y+225,x,y+235)
    
    text("No",x+10,y+325)
    line(x,y+305,x,y+345)
    line(x-5,y+335,x,y+345)
    line(x+5,y+335,x,y+345)
    
    text("No",x-295,y+430)
    line(x-265,y+380,x-265,y+470)
    line(x-270,y+460,x-265,y+470)
    line(x-260,y+460,x-265,y+470)
    
    text("Yes",x+285,y+430)
    line(x+275,y+380,x+275,y+470)
    line(x+280,y+460,x+275,y+470)
    line(x+270,y+460,x+275,y+470)
    
    line(x-265,y+510,x-265,y+550)
    line(x+270,y+510,x+270,y+550)
    line(x+270,y+550,x+260,y+545)
    line(x+270,y+550,x+260,y+555)
    
    line(x-265,y+550,x+455,y+550)
    line(x+455,y+550,x+455,y+110)
    line(x+455,y+110,x,y+110)
    line(x,y+110,x+10,y+105)
    line(x,y+110,x+10,y+115)
    
    text("No",x+350,y+260)
    line(x+300,y+270,x+455,y+270)
    line(x+455,y+270,x+445,y+265)
    line(x+455,y+270,x+445,y+275)
    
    text("Yes",x-350,y+150)
    line(x-280,y+160,x-420,y+160)
    line(x-420,y+160,x-420,y+580)
    line(x-420,y+580,x,y+580)
    line(x,y+580,x,y+600)
    line(x-5,y+590,x,y+600)
    line(x+5,y+590,x,y+600)
                  
def setup():
    for i in range(9):
        temp = int(random(1,10))
        while(temp in num):
            temp = int(random(1,10))
        num.append(temp)
    size(1800,900)
    generate_game()
    print(answer)

def draw():
    
    if (status == 1):
        interface()
    else:
        background(250)
        line(width/2,0,width/2,height)
        show()
        draw_table()     
        fill(0)
        textSize(35)
        text("Flow chart",width/2+100,20) 
        flowchart(width*3/4-20,60)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
