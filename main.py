import os
import random
import time

tick = time.perf_counter()


numPlayers = 4 # will attempt to fit this many tribes onto the map space
mapData = []
worldSize = 11 # must be greater than or equal to 5
tribeData = {}
tribeMap = []
viableLines = []
for i in range(2, worldSize - 2):
    viableLines.append(i)




#Create a 2D list of (square) size "worldSize" and fill it with "▒" (chr(9617),chr(9608))
if worldSize >= 5:
    for y in range(worldSize):
        mapData.append([])
        for x in range(worldSize):
            mapData[y].append(chr(9618))

    #tribe placement viability map
    for y in range(worldSize):
        tribeMap.append([])
        for x in range(worldSize):
            tribeMap[y].append(x)
    for i in range(worldSize):
        tribeMap[0][i] = "!"
        tribeMap[1][i] = "!"
        tribeMap[-2][i] = "!"
        tribeMap[-1][i] = "!"
    for y in range(worldSize):
        for x in range(worldSize):
            tribeMap[y][0] = "!"
            tribeMap[y][1] = "!"
            tribeMap[y][-2] = "!"
            tribeMap[y][-1] = "!"

        
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def clearMapData(): ## untested: for development, not gameplay
    for y in range(len(mapData)):
        for x in range(len(mapData[y])):
            mapData[y][x] = (chr(9618))
            
    viableLines.clear()
    for i in range(2, worldSize - 2):
        viableLines.append(i)
    

def tribeSetupFirst():
    minInt = 2
    maxInt = worldSize - 3
    rand1 = random.randint(minInt, maxInt)
    rand2 = random.randint(minInt, maxInt)
    defaultRadius = 1
    radius = defaultRadius
    print(rand1, rand2)
    for y in range(3):
        for x in range(3):
            mapData[-1 + rand1 + y][-1 + rand2 + x] = chr(9617)
    mapData[rand1][rand2] = chr(9608)
    tribeData[len(tribeData)] = {"x": rand2, "y": rand1, "radius": 1}


mapFull = False
def tribeSetup():
    global mapFull
    if mapFull == False:
        #print("top")
        #print(viableLines)
        randY = random.choice(viableLines)
        randX = random.choice(tribeMap[randY][2:-2])
        #print("random assigned")
        ###print(randY, randX)
        defaultRadius = 1
        radius = defaultRadius
        
        
        if randX in tribeMap[randY]:
            if (1 < randX < (worldSize - 2)) and (1 < randY < (worldSize - 2)):
                for y in range(3):
                    for x in range(3):
                        mapData[-1 + (randY) + y][-1 + randX + x] = chr(9617)
                mapData[randY][randX] = chr(9608)
                tribeData[len(tribeData)] = {"x": randX, "y": randY, "radius": 1}
            else:
                if randX <= 1:
                    randX += random.randint(1, 8)
                if randX >= 9:
                    randX -= random.randint(1, 8)
                if randY <= 1:
                    randY += random.randint(1, 8)
                if randY >= 9:
                    randY -= random.randint(1, 8)
                if randX in tribeMap[randY]:
                    if (1 < randX < 9) and (1 < randY < 9):
                        for y in range(3):
                            for x in range(3):
                                mapData[-1 + (randY) + y][-1 + randX + x] = chr(9617)
                        mapData[randY][randX] = chr(9608)
                        tribeData[len(tribeData)] = {"x": randX, "y": randY, "name": "Imperius", "color": BLUE}
                    else:
                        tribeSetup()
                else:
                    tribeSetup()
        else:
            tribeSetup()


        for y in range(5):
            for x in range(5):
                randXRad = 2 + randX - x
                randYRad = 2 + randY - y
                if randXRad in tribeMap[randYRad]:
                    tribeMap[randYRad].remove(randXRad)
                else:
                    None

        #print("Start viableLine filtering")
        #print(viableLines)
        #print(len(viableLines))
        #drawTribeMap()
        posCounter = 2
        
        for i in tribeMap[2:-2]:
            if i.count("!") == len(i):
                #print(f"try to remove {posCounter}")
                if posCounter in viableLines:
                    viableLines.remove(posCounter)
                    #print(f"{posCounter} removed")
            posCounter += 1

        #print(viableLines)
        #print(len(viableLines))

        if len(viableLines) == 0:
            print("No available positions left. Full.")
            mapFull = True
            
        
        #drawTribeMap()
    else:
        None
        #print("No available positions left. Full.")



def drawMap():
    color = '\033[94m'
    viewMap = ""
    for y in range(len(mapData)):
        for x in range(len(mapData[y])):
            viewMap += (mapData[y][x] * 2)
        viewMap += "\n"
    print(viewMap)


def drawTribeMap():
    viewMap = ""
    for y in range(len(tribeMap)):
        for x in range(len(tribeMap[y])):
            viewMap += str(tribeMap[y][x])
        viewMap += "\n"
    print(viewMap)


### Start running code here!
#drawMap() ## draw the empty map
cls()
n = ""
while n != "q":
    for i in range(numPlayers):
        #time.sleep(0.2)
        #cls()
        tribeSetup()
        #drawMap()
        #drawTribeMap()
    n = "q" #input()

drawMap()
print("done")

tock = time.perf_counter()

print(f"Time elapsed: {tock - tick:0.4f}")

#drawMap()
#drawTribeMap()





