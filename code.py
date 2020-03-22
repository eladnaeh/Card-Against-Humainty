white = open("white.txt", "r")
black = open("black.txt", "r")
whiteList = []
blackList = []
numOfCards = []

def retrieveData():
    for line in white.readlines():
       whiteList.append(line[::-1].strip('\n'))

    for line in black.readlines():
        blackList.append(line[::-1].strip('\n'))
    
    for blackCard in blackList:
        num = 0
        for i in blackCard:
            if(i == '_'):
                num += 1
        if(num == 0):
            num = 1
        
        numOfCards.append(num)
    
    return whiteList, blackList, numOfCards
