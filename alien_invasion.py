import sys
import pygame

from settings import Settings


def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Kalmin's Alien Invasion")
 
	# main game loop
    while True:
		# loop through each event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        # update the screen
        pygame.display.flip()


run_game()
