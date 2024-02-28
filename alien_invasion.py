import pygame
from pygame.sprite import Group

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
    
    # Make a group to store bullets in
    bullets = Group()
 
	# main game loop
    while True:
		# loop through each event
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
