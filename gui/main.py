#!/usr/bin/python
import pygame
from screen import Screen
def main():
	gamebuilder = Screen("gamebuilder",720,480)
	gamebuilder.open()
	clock = pygame.time.Clock()
	while gamebuilder.isOpen():
		gamebuilder.update()
		gamebuilder.render()
		clock.tick(25)
	gamebuilder.close()
	print("terminado")
	
main()
