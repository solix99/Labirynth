import turtle
import tkinter as tk
import random


random.seed()
t = turtle.Turtle()
turtle.title("Labirint")
ts = turtle.getscreen()

turtle.tracer(0, 0)

tsX = 1000
tsY = 1000
sqSize = 30

tSpeed = sqSize/2.5

t.speed(10)

ts.screensize(tsX,tsY)

def isMoveAllowed(direction):
	if(direction=="UP"):
		if(gSquareColor[getCurrentSquareI(getPosX())][getCurrentSquareJ(getPosY() - tSpeed)] == "path"):
			return True
	if(direction=="DOWN"):
		if(gSquareColor[getCurrentSquareI(getPosX())][getCurrentSquareJ(getPosY() + tSpeed)] == "path"):
			return True
	if(direction=="R"):
		if(gSquareColor[getCurrentSquareI(getPosX() + tSpeed)][getCurrentSquareJ(getPosY())] == "path"):
			return True
	if(direction=="L"):
		if(gSquareColor[getCurrentSquareI(getPosX() - tSpeed)][getCurrentSquareJ(getPosY())] == "path"):
			return True
	return False

def isInRange(direction):
	if(direction=="UP"):
		if(getPosY() - tSpeed >= 0): return True
	if(direction=="DOWN"):
		if(getPosY() + tSpeed <= tsY): return True
	if(direction=="R"):
		if(getPosX() + tSpeed <= tsX): return True
	if(direction=="L"):
		if(getPosX() - tSpeed >= 0): return True
	return False


def myGoto(x,y):
		t.goto(x-(tsX/2),(tsY/2)-y)
def getPosX():
	return(int(t.xcor())-(tsX/2)+1000)
def getPosY():
	return((tsY/2)-int(t.ycor()))

def goInsideSquare(i,j):
	t.penup()
	myGoto(i*sqSize+sqSize/2,j*sqSize+sqSize/2)
	t.pendown()

def getCurrentSquareI(posX):
	return (int(posX/sqSize))

def getCurrentSquareJ(posY):
	return (int(posY/sqSize))

def drawSquare(i,j,color):
	t.penup()
	myGoto(i,j)
	t.pendown()
	t.fillcolor(color)
	t.begin_fill()
	t.fd(sqSize)
	t.rt(90)
	t.fd(sqSize)
	t.rt(90)
	t.fd(sqSize)
	t.rt(90)
	t.fd(sqSize)
	t.rt(90)
	t.end_fill()

def moveUp():
	#print(getPosX(),getPosY())
	if(isInRange("UP") and isMoveAllowed("UP")):
		t.setheading(90)
		t.fd(tSpeed)
	#print(getCurrentSquareI(),getCurrentSquareJ())
def moveDown():
	#print(getPosX(),getPosY())
	if(isInRange("DOWN") and isMoveAllowed("DOWN")):
		t.setheading(270)
		t.fd(tSpeed)
def moveRight():
	#print(getPosX(),getPosY())
	if(isInRange("R") and isMoveAllowed("R")):
		t.setheading(0)
		t.fd(tSpeed)
def moveLeft():
	#print(getPosX(),getPosY())
	if(isInRange("L") and isMoveAllowed("L")):
		t.setheading(180)
		t.fd(tSpeed)


def getNextMove():
	roll = random.randint(0,3)
	#print(roll)
	if(roll==0): return "UP"
	elif(roll==1): return "DOWN"
	elif(roll==2): return "RIGHT"
	elif(roll==3): return "LEFT"

#ts.textinput("NIM", "Name of first player:")

#Drawing Code

t.penup()
myGoto(0,0);
t.pendown()

gSquare = [[0 for x in range(int(tsX/sqSize)+1)] for y in range(int(tsY/sqSize)+1)] 
gSquareColor = [[0 for x in range(int(tsX/sqSize)+1)] for y in range(int(tsY/sqSize)+1)] 
iSquarePath = [0]  * 999
jSquarePath = [0] * 999

k = 0;

#Generate Labyrinth

for i in range(int(tsX/sqSize)):
	t.penup()
	for j in range(int(tsY/sqSize)):
		drawSquare(i*sqSize,j*sqSize,"black")
		gSquareColor[i][j] = "wall"
		gSquare[i][j] = 0;
		k=k+1


iStart = int(random.uniform(0,int(tsX/sqSize)))
drawSquare(iStart*sqSize,0,"white")
gSquareColor[iStart][0] = "startPoint"
gSquare[iStart][0] = 1;

iterations = 0
iCur = iStart
jCur = 0
iLast = iStart
jLast = 0
nextMove = ""
pathFormed = False
iFinal = 0
jFinal = 0
k=0

while(pathFormed == False):

	iterations=0

	for i in range(int(tsX/sqSize)):
		for j in range(int(tsY/sqSize)):
			gSquare[i][j] = 0
			iSquarePath[i] = 0
			jSquarePath[j] = 0

	iCur = iStart
	jCur = 0
	iLast = iStart
	jLast = 0
	k=0
	while(iterations<=tsX/10):
		nextMove = getNextMove()
		#print(nextMove)
		if(nextMove=="UP" and jCur>1):
			jCur = jCur
		elif(nextMove=="DOWN" and jCur < int(tsY/sqSize)):
			jCur = jCur +1
		elif(nextMove=="LEFT" and iCur>1):
			iCur = iCur -1
		elif(nextMove=="RIGHT" and iCur < int(tsX/sqSize)-1):
			iCur = iCur +1
		
		conns = 0
		if(gSquare[iCur+1][jCur]==1):
			conns = conns + 1
		if(gSquare[iCur-1][jCur]==1):
			conns = conns + 1
		if(jCur<int(tsY/sqSize)):
			if(gSquare[iCur][jCur+1]==1):
				conns = conns + 1
		if(gSquare[iCur][jCur-1]==1):
			conns = conns + 1

		if(gSquare[iCur][jCur]==1 or conns>1):
			iCur=iLast
			jCur=jLast
		else:
			iLast = iCur;
			jLast = jCur;
			iSquarePath[k] = iCur
			jSquarePath[k] = jCur
			gSquare[iCur][jCur] = 1
			k = k + 1

		iterations=iterations+1

		if(jCur == int(tsY/sqSize)):
			iFinal = iCur
			jFinal = jCur-1
			pathFormed = True
			break


pathFormed = False
divergentPaths = 0;
iCur = 0
jCur = 0
iLast = 0
jLast = 0

while(divergentPaths<tsX):
	pathFormed = False
	iCur = int(random.uniform(0,int(tsX/sqSize)))
	jCur = int(random.uniform(0,int(tsX/sqSize)))
	#iCur = iSquarePath[divergentPaths] 
	#jCur = jSquarePath[divergentPaths]
	print(iCur)
	print(jCur)
	iLast = 0
	jLast = 0
	while(pathFormed == False):
		iterations=0
		while(iterations<=100):
			nextMove = getNextMove()
			#print(nextMove)
			if(nextMove=="UP" and jCur>1):
				jCur = jCur -1 
			elif(nextMove=="DOWN" and jCur < int(tsY/sqSize)):
				jCur = jCur +1
			elif(nextMove=="LEFT" and iCur>1):
				iCur = iCur -1
			elif(nextMove=="RIGHT" and iCur < int(tsX/sqSize)-1):
				iCur = iCur +1
	
			conns = 0
			if(gSquare[iCur+1][jCur]==1):
				conns = conns + 1
			if(gSquare[iCur-1][jCur]==1):
				conns = conns + 1
			if(jCur<int(tsY/sqSize)):
				if(gSquare[iCur][jCur+1]==1):
					conns = conns + 1
			if(gSquare[iCur][jCur-1]==1):
				conns = conns + 1

			if(gSquare[iCur][jCur]==1 or conns>1):
				iCur=iLast
				jCur=jLast
			else:
				iLast = iCur;
				jLast = jCur;
				gSquare[iCur][jCur] = 1
			iterations=iterations+1
		pathFormed = True
	divergentPaths = divergentPaths+1
	


#Draw Labyrinth

for i in range(int(tsX/sqSize)):
	for j in range(int(tsY/sqSize)):
		if(gSquare[i][j]==1):
			drawSquare(i*sqSize,j*sqSize,"white")
			gSquareColor[i][j] = "path"


drawSquare(iFinal*sqSize,jFinal*sqSize,"red")

t.color("red")

t.penup()
goInsideSquare(iStart,0)

t.pendown()

turtle.tracer(1, 1)

#Input code

ts.onkey(moveUp,"Up")
ts.onkey(moveDown,"Down")
ts.onkey(moveLeft,"Left")
ts.onkey(moveRight,"Right")

ts.listen()


ts.mainloop()


