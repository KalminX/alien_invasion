import sys
import pygame


def run_game():
    # initialize screen and game play
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Kalmin's Alien Invasion")
 
    # Set the background color
    bg_color = (230, 230, 230)

	# main game loop
    while True:
		# loop through each event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # redraw the screen during each pass through the loop
        screen.fill(bg_color)
        # update the screen
        pygame.display.flip()


run_game()
