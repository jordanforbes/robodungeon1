import pygame
import pygame.gfxdraw
import math
import random

pygame.init()
gameX = 50
gameY = 50
nodeSize =  15
courier1 = pygame.font.SysFont('Courier', 16)
gameDisplay = pygame.display.set_mode((gameX *nodeSize,gameY*nodeSize))
pygame.display.set_caption('A*')
clock = pygame.time.Clock()

def init():
	global openTiles, closedTiles, blockedTiles, worldTiles, startPos, goalPos
	startPos = Node(int(random.random() * gameX),int(random.random() * gameY))
	goalPos = Node(int(random.random() * gameX),int(random.random() * gameY))
	openTiles = []
	closedTiles = []
	blockedTiles = []
	worldTiles = []
	print(len(worldTiles))
class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.parent = ""
		self.gVal = 0
		self.hVal = 0
		self.fVal = self.gVal + self.hVal

def run():
	init()
	for i in range(gameX):
		for j in range(gameY):
			node = Node(i, j)
			worldTiles.append(node)
	for i in range(50):
		node = worldTiles[int(random.random() * len(worldTiles))]
		blockedTiles.append(node)
		worldTiles.remove(node)
	print(len(worldTiles))
	draw()
	running = True
	while running:

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == 113:    #Q
					print('Q')
					running = False
				if event.key == 32:    #Space
					print('Space')
					runGame()
			if event.type == pygame.MOUSEBUTTONDOWN:
				coords = pygame.mouse.get_pos()
				node = Node(int(coords[0]/nodeSize), int(coords[1]/nodeSize))
				#print(findInList(int(coords[0]/nodeSize), int(coords[1]/nodeSize), blockedTiles))
				if(pygame.mouse.get_pressed()[0] == 1):
					moveStartPos(int(coords[0]/nodeSize), int(coords[1]/nodeSize))
				elif(pygame.mouse.get_pressed()[2] == 1):
					moveGoalPos(int(coords[0]/nodeSize), int(coords[1]/nodeSize))
				elif(pygame.mouse.get_pressed()[1] == 1):
					addBlocker(int(coords[0]/nodeSize), int(coords[1]/nodeSize))
def findInList(x, y, list):
	for node in list:
		if node.x == x and node.y == y:
			return node

def moveStartPos(x, y):
	if not findInList(x, y, blockedTiles):
		startPos.x = x
		startPos.y = y
		draw()
def moveGoalPos(x, y):
	if not findInList(x, y, blockedTiles):
		goalPos.x = x
		goalPos.y = y
		draw()
def addBlocker(x, y):
	if not findInList(x, y, blockedTiles):
		node = findInList(x, y, worldTiles)
		worldTiles.remove(node)
		blockedTiles.append(node)
		draw()
def draw():
	findPath()
	gameDisplay.fill((0,0,0))
	for node in worldTiles:
		pygame.gfxdraw.box(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(255, 255,255))
		pygame.gfxdraw.rectangle(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	for node in blockedTiles:
		pygame.gfxdraw.box(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(255, 0,0))
		pygame.gfxdraw.rectangle(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	for node in openTiles:
		pygame.gfxdraw.box(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 255,0))
		pygame.gfxdraw.rectangle(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	for node in closedTiles:
		pygame.gfxdraw.box(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(127, 0,0))
		pygame.gfxdraw.rectangle(gameDisplay,(node.x*nodeSize, node.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	pygame.gfxdraw.box(gameDisplay,(startPos.x*nodeSize, startPos.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	pygame.gfxdraw.box(gameDisplay,(goalPos.x*nodeSize, goalPos.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 127,0))
	pygame.gfxdraw.rectangle(gameDisplay,(goalPos.x*nodeSize, goalPos.y*nodeSize, nodeSize, nodeSize), pygame.Color(0, 0,0))
	pygame.display.update()

def findPath():
	closedTiles = [startPos]
	for i in range(-1,2):
		for j in range(-1,2):
			node = findInList(startPos.x + i, startPos.y + j, worldTiles)
			if(node):
				worldTiles.remove(node)
				openTiles.append(node)
	print(len(openTiles))

run()