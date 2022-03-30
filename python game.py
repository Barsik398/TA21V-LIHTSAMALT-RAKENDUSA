
from operator import truediv
from unittest import result


game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]
while(True):
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])

    next_position1 =input("Please type what position: ")

    
    
       
   

    # line 14 and 17 are same. Please make "1" and "2" to int (using int() function and -1)
    if next_position1 == "1":
        game[0] = "X"
    if next_position1 == "2":
        game[1] = "X"    
    if next_position1 == "3":
        game[2] = "X"    
    if next_position1 == "4":
        game[3] = "X"    
    if next_position1 == "5":
        game[4] = "X"    
    if next_position1 == "6":
        game[5] = "X"    
    if next_position1 == "7":
        game[6] = "X"    
    if next_position1 == "8":
        game[7] = "X"    
    if next_position1 == "9":
        game[8] = "X"    

    # this is same as on line 7. make this a function
    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])

    next_position2 =input("Please type what position: ")



    if next_position2 == "1":
        game[0] = "O"
    if next_position2 == "2":
        game[1] = "O"    
    if next_position2 == "3":
        game[2] = "O"    
    if next_position2 == "4":
        game[3] = "O"    
    if next_position2 == "5":
        game[4] = "O"    
    if next_position2 == "6":
        game[5] = "O"    
    if next_position2 == "7":
        game[6] = "O"    
    if next_position2 == "8":
        game[7] = "O"    
    if next_position2 == "9":
        game[8] = "O"    

    print(game[0] + game[1] + game[2])
    print(game[3] + game[4] + game[5])
    print(game[6] + game[7] + game[8])

    if game[0]==game[1]==game[2]:
        print("win")
        winner=True
    if game[3]==game[4]==game[5]:
        print("win")
        winner=True
    if game[6]==game[7]==game[8]:
        print("win")
        winner=True
    if game[1]==game[4]==game[8]:
        print("win")
        winner=True
    if game[6]==game[4]==game[2]:
        print("win")
        winner=True
    if game[0]==game[3]==game[6]:
        print("win")
        winner=True
    if game[2]==game[5]==game[8]:
        print("win")
        winner=True
    if game[1]==game[4]==game[7]:
        print("win")
        winner=True

        if winner == True:
            break
