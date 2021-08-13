from board import Board
from knott import Knott
from tic_tac_toe import Cross



choices = 'X0'
player1_choice = input("Choose X or 0 ")
player2_choice = choices.replace(player1_choice,'')
print(f"Player1 chooses {player1_choice}")
print(f"Player2 gets {player2_choice}")

value = None
box_number = None

object1 = 2
object2 = 3
object3 = 4
object4 = 5
object5 = 6
object6 = 7
object7 = 8
object8 = 9
object9 =  10

def object_call (value , box_number):
    if box_number == 1:
        global object1
        object1 = value

    if box_number == 2:
        global object2
        object2  = value

    if box_number == 3:
        global object3
        object3 = value

    if box_number == 4:
        global object4
        object4 = value

    if box_number == 5:
        global object5
        object5 = value

    if box_number == 6:
        global object6
        object6 = value

    if box_number == 7:
        global object7
        object7 = value

    if box_number == 8:
        global object8
        object8 = value

    if box_number == 9:
        global object9
        object9 = value

    

def victory_check():
    
    if object1 == object2 == object3 or object7 == object8 == object9 or object4 == object5 == object6 or object1 == object4 == object7 or object2 == object5 == object8 or object3 == object6 == object9  or object1 == object5 == object9 or object3 == object5 == object7 :
        return 0
    else:
        return 1

count = 0
while True :
    box_number = int(input("Player 1 enter "))
    if player1_choice == 'X':
        object = Cross(box_number)
        value = object.value
        
    elif player1_choice == '0':
        object = Knott(box_number)
        value = object.value
        
    object_call(value,box_number)

    count = count+1  
    if count==9:
        print("no one wins")
        break
    
    status_1 = victory_check()
        
    if status_1 == 1:
        pass

    elif status_1 == 0 :
        print("player1 wins")
        break
    
    box_number = int(input("Player 2 enter "))
    if player2_choice == 'X':
        object = Cross(box_number)
        value = object.value
        
    elif player2_choice == '0':
        object = Knott(box_number)
        value = object.value
    
    object_call(value,box_number)

    count = count+1
    if count==9:
        print("no one wins")
        break
    
    status_2 = victory_check()
        
    if status_2 == 1:
        pass

    elif status_2 == 0:
        print("player2 wins")
        break

    





