import pygame, sys
pygame.init()

size = width, height = 320,240

screen = pygame.display.set_mode(size)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	state = pygame.key.get_pressed()
	print "W:" + str(state[pygame.K_w]) + " S:" + str(state[pygame.K_s]) + " A:" + str(state[pygame.K_a]) + " D:" + str(state[pygame.K_d])