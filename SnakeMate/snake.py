### note that you have to install the pygame library ###
### if you have pip installed : ###
### simply open cmd and on windows type pip install pygame ###
from random import randrange, randint
try :
	import pygame
except ex:
	print("You will need to install the Pygame library for this to work")
	input("'q' than enter to quit")

### Colors RGB values ### 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,150,0)
yellow = (255,255,0)
niceYellow = (255,102,0)
niceRed = (255,178,102)
niceGreen = (102,255,102)
niceBlue = (102,178,255)
darkRed = (155,0,0)

### PACKAGE INITIALIZER ### 
pygame.init()

### IMPORTANT CONSTANTS ###
### the game is in squere screen, so HEIGHT = WIDTH = DIM ###
### the SIZE of the snake changes based on the screen size (DIM)###
### the game FPS value is controlled here aswell ###
DIM = 800
SIZE = DIM/20
FPS = 10

### FONTS ###
fontFile = 'gameFont.ttf'
smallfont = pygame.font.Font(fontFile, int(DIM/50))
mediumfont = pygame.font.Font(fontFile, int(DIM/25))
largefont = pygame.font.Font(fontFile, int(DIM/20))

### images ###
### not resizeable, so dont change DIM ###
### unless you load new images incase of resize ###
head_img_file = pygame.image.load('snake_head.png')
body_img = pygame.image.load('snake_body.png')
tail_img_file = pygame.image.load('snake_tail.png')
pie_img = pygame.image.load('pie.png')
icon = pygame.image.load('icon.png')

### Direction of the headd image ###
direction = "right"

### Settings ### 
gameDisplay = pygame.display.set_mode((DIM,DIM))
pygame.display.set_caption("SnakeMate")
pygame.display.set_icon(icon)

### Essential for the FPS ###
clock = pygame.time.Clock()

### Creating text Surface -> returns the text Surface and the text Rectangle###
def createText(text, color, size):

	if size=="small":
		textSurface = smallfont.render(text, True, color)

	elif size=="medium":
		textSurface = mediumfont.render(text, True, color)

	elif size=="large":
		largefont.set_bold(True)
		largefont.set_underline(True)
		textSurface = largefont.render(text, True, color)

	return textSurface, textSurface.get_rect()

### Putting Text on screen ### 
### note tht this function returns NOTHING ###
def messageToScreen(msg, color, posY=0 ,size="medium"):

	textSurf, textRect = createText(msg, color, size)
	textRect.center = (DIM/2, (DIM/2)+posY)
	gameDisplay.blit(textSurf, textRect)


### This function creates the snake based on an array ###
### snake = array of body parts ###
### direction = direction for the head image ###
### note tht this function returns NOTHING ###
def createSnake(size, snake, direction):

	### setting the direction for the head image ###
	if direction == "right":
		head_img = pygame.transform.rotate(head_img_file, 270)
	elif direction == "left":
		head_img = pygame.transform.rotate(head_img_file, 90)
	elif direction == "up":
		head_img = pygame.transform.rotate(head_img_file, 0)
	elif direction == "down":
		head_img = pygame.transform.rotate(head_img_file, 180)

	### snake is a list of topples. in this forloop -> XnY = (headX, headY) ###
	### we go over all the snake parts EXCEPT the last one ###
	for XnY in snake[1:-1]:
		gameDisplay.blit(body_img, (XnY[0], XnY[1]))

	### Filling the last part with the tail img ###
	### ONLY if there are more than one part to the snake (aka the head)###
	if len(snake) > 1:
		gameDisplay.blit(tail_img_file, (snake[0][0], snake[0][1]))

	### drawing the head image ###
	gameDisplay.blit(head_img, (snake[len(snake)-1][0], snake[len(snake)-1][-1]))

### Main Game Function ###
### note tht this function returns NOTHING ###
def gameLoop():

	### Locations -> snake starts at center height, left side of screen, pie at a random location ###
	headX = -SIZE
	headY = DIM/2
	pieX = randrange(0, DIM-SIZE, SIZE)
	pieY = randrange(0, DIM-(SIZE*2), SIZE)

	### Motion variables ### 
	motionX = SIZE
	motionY = 0

	### Snake body Score and GOAL ###
	### goal changes based on screen size ###
	snake = []
	tail = 0
	goal = int((DIM/SIZE)*4)

	### background rgb values for startGame ###
	r = 161
	g = 224
	b = 97

	## head_img direction ###
	direction = "right"

	### Game States, names speak for themselfs ### 
	startGame = False
	pauseGame = False
	gameOver = False
	gameOverGood = False
	gameExit = False

	### Main GAME LOOP, While not exited ### 
	while not gameExit:

		### If Game Has NOT STARTED yet ### 
		if not startGame and not gameOver and not pauseGame:

			###### Nothing on screen but the msg ######
			### Background Graphics ### 
			gameDisplay.fill((161, 224, 97))

			###### animation of snake in the START SCREEN ######
			###### you can move the snake in the Start screen ######
			###### ALL OF THIS IS EXPLAIND IN THE STARTGAME SECTION ######
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				else:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							startGame = True
							direction = "right"
							snake = []
							headX = -SIZE
							headY = DIM/2
							motionX = SIZE
							motionY = 0
						elif event.key == pygame.K_ESCAPE:
							gameExit = True
						elif event.key == pygame.K_LEFT:
							if motionY != 0:
								direction = "left"
								motionX = -SIZE
								motionY = 0
						elif event.key == pygame.K_RIGHT:
							if motionY != 0:
								direction = "right"
								motionX = SIZE
								motionY = 0
						elif event.key == pygame.K_UP:
							if motionX != 0:
								direction = "up"
								motionY = -SIZE
								motionX = 0
						elif event.key == pygame.K_DOWN:
							if motionX != 0:
								direction = "down"
								motionY = SIZE
								motionX = 0
			headX += motionX
			headY += motionY
			if headX < 0:
				headX = DIM-SIZE
			if headX > DIM-SIZE:
				headX = 0
			if headY < 0:
				headY = DIM-SIZE
			if headY > DIM-SIZE:
				headY = 0
			snakeHead = []
			snakeHead.append(headX)
			snakeHead.append(headY)
			snake.append(snakeHead)
			createSnake(SIZE, snake, direction)
			if len(snake) > 5:
				del snake[0]
			clock.tick(FPS)
			###### end of animation in the START SCREEN ######

			### The MSG ###
			messageToScreen("Welcome to SnakeMate!", green, -120, "large")
			messageToScreen("Use the arrow keys to move the Snake.", red, -70, "small")
			messageToScreen("The goal is to reach "+str(goal)+" Points.", red, -50, "small")
			messageToScreen("Good Luck!", red, -30, "small")
			messageToScreen("Press ENTER to Start!", niceYellow, 10, "medium")
			messageToScreen("Press ESC to Quit", niceYellow, 50, "medium")
			pygame.display.update()

		### If is PAUSED ### 
		elif startGame and pauseGame and not gameOver:
			messageToScreen("Game Paused", green, -300, "large")
			messageToScreen("Press ENTER to continue", black, -100, "medium")
			pygame.display.update()

			### Handling Pause, Back to Start and Quit - RETURN, p and ESC Keys ###
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				else:
					if event.type == pygame.KEYDOWN:

						### Key RETURN - Return to game ### 
						if event.key == pygame.K_RETURN:
								pauseGame = False

						### Key ESC - Quit ### 
						elif event.key == pygame.K_ESCAPE:
								gameExit = True

						### Key P - back to Start menu ### 
						elif event.key == pygame.K_p:
							del snake[:]
							tail = 0
							pauseGame = False
							startGame = False

		### If Game is Over ### 
		elif  gameOver and not startGame and not pauseGame:

			### Background Graphics ### 
			gameDisplay.fill(niceBlue)

			### If player reached GOAL ###
			if gameOverGood:
				messageToScreen("Congratulations!", blue, -100, "large")
				messageToScreen("Press ENTER to Restart!", niceYellow, 10, "medium")
				messageToScreen("Press ESC to Quit", niceYellow, 50, "medium")

			### If player is a NOOB ###
			else:
				messageToScreen("Game Over", red, -100, "large")
				messageToScreen("Press ENTER to Restart!", niceYellow, 10, "medium")
				messageToScreen("Press ESC to Quit", niceYellow, 50, "medium")

			pygame.display.update()

			### Reseting Motion and Location variables ### 
			motionX = SIZE
			motionY = 0
			headX = DIM/2
			headY = DIM/2

			### Handling Pause and Quit - RETURN and ESC Keys ###
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
				else:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
								gameOver = False
								gameOverGood = False
								direction = "right"
						if event.key == pygame.K_ESCAPE:
								gameExit = True

		### If Game has STARTED ### 
		elif startGame and not pauseGame and not gameOver:

			### Background Graphics - color changes with score ### 
			gameDisplay.fill((r,g,b))

			### Catching all events While playing ### 
			for event in pygame.event.get():
				### this event is clicking on the X in the corner ###		
				if event.type == pygame.QUIT:
					gameExit = True
				### this event is pressing a key ###
				elif event.type == pygame.KEYDOWN:
				####### Exiting and Pausing The Game #######
					### Key ENTER - Pause / Start Game ### 
					if event.key == pygame.K_RETURN:
						if not startGame:
							startGame = True
						else:
							pauseGame = True
					### Key ESCAPE - Exit Game ### 
					elif event.key == pygame.K_ESCAPE:
						gameExit = True
					### Key P - back to Start menu ### 
					elif event.key == pygame.K_p:
						startGame = False
						del snake[:]
						tail = 0
				####### MOVEMENT ######
					### Key LEFT ### 	
					elif event.key == pygame.K_LEFT:
						if motionY != 0:
							direction = "left"
							motionX = -SIZE
							motionY = 0
					### Key RIGHT ### 
					elif event.key == pygame.K_RIGHT:
						if motionY != 0:
							direction = "right"
							motionX = SIZE
							motionY = 0
					### Key UP ### 
					elif event.key == pygame.K_UP:
						if motionX != 0:
							direction = "up"
							motionY = -SIZE
							motionX = 0
					### Key DOWN ### 
					elif event.key == pygame.K_DOWN:
						if motionX != 0:
							direction = "down"
							motionY = SIZE
							motionX = 0

			### setting motion for the snake (head -> body) ###
			headX += motionX
			headY += motionY

			### Border Colision Detection, snake will apear on the other side ### 
			if headX < 0:
				headX = DIM-SIZE
			if headX > DIM-SIZE:
				headX = 0
			if headY < 0:
				headY = DIM-SIZE
			if headY > DIM-SIZE:
				headY = 0

			### Drawing Snake head and pie.. Snake OVER Pie ###
			### this head is not being draw, its only for simple colision detection ###
			pie = pygame.Rect(pieX, pieY, SIZE, SIZE)
			head = pygame.Rect(headX, headY, SIZE,SIZE)
			gameDisplay.blit(pie_img, (pieX, pieY))

			### Snakes' Body, snakeHead is a topple = (headX, headY) ###
			snakeHead = []
			snakeHead.append(headX)
			snakeHead.append(headY)

			### appending the head all the time ###
			snake.append(snakeHead)

			### drawing the snake all the time, creating the snake ###
			### note tht this function returns NOTHING ###
			createSnake(SIZE, snake, direction)

			### Deleting last (first in array) part of snake to create movement illusion ###
			### the bigger the tail variable, the longer the snake ### 
			if len(snake) > tail:
				del snake[0]

			### Handling snake Self colision ###
			### if topple(partX, partY)==topple(headX, headY): collision ###
			for part in snake[:-1]:
				if part == snakeHead:
					del snake[:]
					tail = 0
					### Changing game state ###
					startGame = False
					gameOver = True

			### Colision detection pie and head, in case of colision, tail++ ### 
			### colliderect() function works only with rectangle obj ###
			### that is why I created head ###
			if head.colliderect(pie):
				### changing the pie coordinates ###
				pieX = randrange(0, DIM-SIZE, SIZE)
				pieY = randrange(0, DIM-SIZE, SIZE)
				### this loop is supposed to varify that the new pie will not apear on snakes body ###
				### sadly this doesnt fully work, and is terrible inefficient ###
				### TODO: need to find an algorithm to solve this ###
				for part in snake:
					while part[0] == pieX and part[1] == pieY:
						pieX = randrange(0, DIM-SIZE, SIZE)
						pieY = randrange(0, DIM-SIZE, SIZE)
				### adding a score + adding a tail -> adding a snake part ### 
				tail += 1
				### changing the screen color, every time a pie is being eaten ### 
				r = randint(0, 255)
				g = randint(0, 255)
				b = randint(0, 255)
				### because of pie apearing on snake, I put a goal the player needs to reach ###
				### in oppose to simply filling the screen with the snake ###
				### so here I'm checking if the tail(score) has reached the goal ### 
				if tail == goal:
					del snake[:]
					tail = 0
					startGame = False
					gameOver = True
					gameOverGood = True

			### Showing SCORE = TAIL, in different colors to keep it visible, and RGB values (just for fun) ###
			if tail is not 0:
				### if the background is bright, score is black ###
				if r > 200 or g > 200 or b > 200: 
					messageToScreen("R : "+str(r)+ "     G : "+str(g)+ "     B : "+str(b), black, -200, "small")
					messageToScreen(str(tail), black, -250, "medium")
				### if the background is dark, score is white ###
				else:
					messageToScreen("R : "+str(r)+ "     G : "+str(g)+ "     B : "+str(b), white, -200, "small")
					messageToScreen(str(tail), white, -250, "medium")
			### Updating the Screen, as in rendering graphics ###
			pygame.display.update()

			### FPS ###
			### ticking the game clock -> NEXT FRAME ### 
			clock.tick(FPS)

	### Quiting the Game, after leaving the game loop <- gameExit = True ### 
	pygame.quit()
	quit()

### The Main Game Function Call ### 
gameLoop()


