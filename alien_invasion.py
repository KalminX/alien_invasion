import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Kalmin's Alien Invasion")
    
    # Make a ship
    ship = Ship(ai_settings, screen)
 
	# main game loop
    while True:
		# loop through each event
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
