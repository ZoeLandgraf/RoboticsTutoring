import pygame


# define global variables here

class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """

    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        # self.image = pygame.Surface([segment_width, segment_height])
        # self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y



def run_game():
    pass



# initialize the window here

# create an initial snake