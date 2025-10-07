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
    line(0,height/3,width,height/3)
    line(0,height/3*2,width,height/3*2)
    
    line(width/3,0,width/3,height)
    line(width/3*2,0,width/3*2,height)
    strokeWeight(1)
    line(0,height/9,width,height/9)
    line(0,height/9*2,width,height/9*2)
    line(0,height/9*4,width,height/9*4)
    line(0,height/9*5,width,height/9*5)
    line(0,height/9*7,width,height/9*7)
    line(0,height/9*8,width,height/9*8)
    
    line(width/9,0,width/9,height)
    line(width/9*2,0,width/9*2,height)
    line(width/9*4,0,width/9*4,height)
    line(width/9*5,0,width/9*5,height)
    line(width/9*7,0,width/9*7,height)
    line(width/9*8,0,width/9*8,height)

def check_rule(board,row,col,num):
    #check row
    for i in range(9):
        if num == board[row][i]:
            return False
        
    #check column
    for i in range(9):
        if num == board[i][col]:
            return False
        
    #check box 3x3

    
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[box_start_row + i][box_start_col + j] == num:
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
            cell_w = width / 9
            cell_h = height / 9
            
            if (i, j) in correct_cell:
                fill(102, 255, 102)
                noStroke()
                rect(j * cell_w, i * cell_h, cell_w, cell_h)
                stroke(0)
            
            if (i, j) == selected_cell :
                fill(180, 180, 180)
                noStroke()
                rect(j * cell_w, i * cell_h, cell_w, cell_h)
                stroke(0)

                
            if grid[i][j] != 0:
                if((i, j) not in entry_cell):
                    fill(204, 255, 255)
                    noStroke()
                    rect(j * cell_w, i * cell_h, cell_w, cell_h)
                    stroke(0)
                fill(0)
                text(grid[i][j], width/18*2*j+(width/18), height/18*2*i+(height/18))

                if(status == 3 and grid[i][j] != answer[i][j]):
                    fill(255, 0, 0)
                    noStroke()
                    rect(j * cell_w, i * cell_h, cell_w, cell_h)
                    stroke(0)
                    fill(0)
                    text(grid[i][j], width/18*2*j+(width/18), height/18*2*i+(height/18))
            #if grid[i][j] == 0 and status == 3:    
            #    fill(255, 0, 0)  
            #    noStroke()
            #    rect(j * cell_w, i * cell_h, cell_w, cell_h)
            #    stroke(0)
def interface():
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
        cell_w = width / 9
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
    elif key == ENTER:
        if (status == 2):
            status = 3
            correct_cell = []
            for r, c in entry_cell:
                if grid[r][c] == answer[r][c]:
                    correct_cell.append((r, c))
        else:
            status = 2
    elif key == 's':
        print("save")
        save_game()


                
def setup():
    for i in range(9):
        temp = int(random(1,10))
        while(temp in num):
            temp = int(random(1,10))
        num.append(temp)
    size(900,900)
    generate_game()
    print(answer)
def draw():
    if (status == 1):
        interface()
    else:
        background(250)
        show()
        draw_table()      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
