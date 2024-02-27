import pygame

class Ship():
    
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images\ship.ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()