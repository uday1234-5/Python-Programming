move = [' ',' ',' ',' ',' ',' ',' ',' ',' ']*9

def display(move):
  x ="""
     
       {1}  |  {2}  |  {3} 
     _____|_____|_____
       {4}  |  {5}  |  {6} 
     _____|_____|_____
       {7}  |  {8}  |  {9}  
          |     |    
        """.format(*move)
  print(x)


turn = "X"
while True:
    input1 = int(input(f"To display {turn}, Enter the position : "))
    move[input1] = turn
    display(move)
    
  
    turn = "O" if turn == "X" else "X"