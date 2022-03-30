


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