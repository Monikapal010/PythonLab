import random 

def display(grid):
   
   horizantal_line="__"*len(grid)
   print(horizantal_line)
   for row in grid:
    s="|{}"* len(grid)+"|"
    print(s.format(*row))
   # print("|".join(row),"|",sep="")
    print(horizantal_line)


def fill():
     grid_size=int(input("Enter the size of gird"));
     game_state=[list(" "* grid_size)  for _ in range(grid_size)]
     pos_b={i for i in range(1,grid_size+1)}
     for row in range(grid_size):
        for column in range(grid_size):
          available=set(game_state[row] + [tr[column] for tr in game_state])
          print(available)
          c=list(pos_b-available)
          #game_state[row][column]=c.pop(randint(0,len(c)-1))
          
          if c:
                game_state[row][column] = str(c.pop(random.randint(0, len(c) - 1)))
          else:
                game_state[row][column] = ' ' 
          
     return game_state
       
  

def initialize():
  
  grid_size=int(input("Enter the size of gird"));
  
  game_state=[list(" "* grid_size)  for _ in range(grid_size)]
  
  game_state[0][0]=1
  game_state[1][1]=2
  
  display(game_state)

 
def sudoku():
  initialize() 
  
  fill()
  
 # start_game()
  
 # end_game()
  
sudoku()
