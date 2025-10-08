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
    if(status == 3):
        fill(0)
        textSize(100)
        text("YOU WIN",(width/2-300)/2,150)
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
    text("start",x-35,y+10) 
    textSize(35) 

def flow_o(x, y, t):
    w = textWidth(t) + 20 
    h = 40 
    fill(0, 255, 0) 
    rect(x, y, w, h)
    fill(0) 
    textSize(35) 
    textAlign(LEFT, CENTER) 
    text(t, x + 10, y + h / 2) 

def flow_c(x, y, t): 
    textSize(20) 
    w = textWidth(t) + 140 
    h = 70 
    stroke(0) 
    strokeWeight(2) 
    left_x = x - w / 2 
    right_x = x + w / 2 
    top_y = y - h / 2 
    bottom_y = y + h / 2 
    fill(0, 255, 0) 
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
