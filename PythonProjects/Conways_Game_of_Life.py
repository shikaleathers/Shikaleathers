# Conways Game of life
import random, time, copy

WIDTH = 60
HEIGHT = 20

#Create a list for the cells

nextCells = []
for x in range(WIDTH):
    column = [] #creates a new column.
    for y in range (HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #Add a living cell.
        else:
            column.append(' ') #This adds a dead cell
    nextCells.append(column) #nextCells in a list of columns
while True: #This is the main program loop
    print('\n\n\n\n\n') #This causes the steps to be seperated with newlines.
    currentCells = copy.deepcopy(nextCells)
    #Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=' ') # Prints # or Space
        print() #Prints a newline at the end of the row.
    #Calculate the next step's cells based on the current step's cells
    for x in range (WIDTH):
        for y in range (HEIGHT):
            #get neighbouring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            #Count number of living neighbots:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
               numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
               numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
               numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
               numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
               numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
               numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
               numNeighbors += 1
            # Set cell cased on the rules of the game
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors  == 3:
                    nextCells[x][y] = '#'
            else:
                    nextCells[x][y] = ' '

    time.sleep(1)
