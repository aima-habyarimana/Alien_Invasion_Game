import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')  # This function returns a surface representing the ship, which we store in self.image
        self.rect = self.image.get_rect()   # get_rect : get the rectangular area of the Surface, even if they’re not exactly shaped like rectangles.
        '''
        Treating an element as a rectangle is efficient because rectangles are simple geometric shapes.
        This approach usually works well enough that no one playing the game will notice that we’re not working with the exact shape of each game element.
        
        When working with a rect object, you can use the x- and y-coordinates of the top, bottom, left, and right edges of the rectangle, 
        as well as the center. You can set any of these values to determine the current position of the rect.
        When you’re centering a game element, work with the center, centerx, or centery attributes of a rect. When you’re working at an edge of the screen,
        work with the top, bottom, left, or right attributes
        
        In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates
        increase as you go down and to the right. On a 1000 by 650 screen, the origin is at
        the top-left corner, and the bottom-right corner has the coordinates (1000, 650).
        
        '''

        self.screen_rect = screen.get_rect() # We’ll position the ship at the bottom center of the screen. To do so, first store the screen’s rect in self.screen_rect
                                             # and then make the value of self.rect.centerx (the x-coordinate of the ship’s center) match the centerx attribute of the screen’s rect

        # Start each new ship at the bottom center of the screen.
        '''
        Make the value of self.rect.bottom (the y-coordinate of the ship’s bottom) equal to the value of the screen rect’s
        bottom attribute. Pygame will use these rect attributes to position the ship
        image so it’s centered horizontally and aligned with the bottom of the screen. 
        '''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags.
        we use two separate if blocks rather than an elif in update() to allow the ship’s rect.centerx
        value to be increased and then decreased if both arrow keys are held down.
        """

        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # will draw the image to the screen at the position specified by self.rect.

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

