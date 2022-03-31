map = [
    [12,0,1,0,1],
    [1,1,1,0,1],
    [0,0,1,1,0],
    [24,0,1,0,0],
    [1,1,1,0,0],
]
startposX=0
startposY=0

xrows=5
ycolumn=5
def get_next_free_possition(currentlypossitionX,currentlypossitionY):

    if currentlypossitionY+1 < ycolumn and map[currentlypossitionX][currentlypossitionY+1] == 1:
        print("can go right")
        return[currentlypossitionX,currentlypossitionY+1]

    if currentlypossitionY-1 > 0 and map[currentlypossitionX][currentlypossitionY-1] == 1:
        print("can go left")
        return[currentlypossitionX,currentlypossitionY-1]

    if currentlypossitionX+1 < xrows and map[currentlypossitionX+1][currentlypossitionY] == 1:
        print("can go bottom")
        return[currentlypossitionX+1,currentlypossitionY]

    if currentlypossitionX-1 > 0 and map[currentlypossitionX-1][currentlypossitionY] == 1:
        print("can go top")
        return[currentlypossitionX-1,currentlypossitionY]

   


next_free_possition=get_next_free_possition(startposX,startposY)
print("get_next_free_possition is", next_free_possition)

while next_free_possition:
    next_free_possition=get_next_free_possition(next_free_possition[0],next_free_possition[1])
    print("get_next_free_possition is", next_free_possition)


