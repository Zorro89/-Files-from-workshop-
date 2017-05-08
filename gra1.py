import pygame



# PYGAME RESOURCES

pygame.init()



SCREEN = pygame.display.set_mode((800, 600))
IMG_EARTH= pygame.image.load('earth.png').convert()
IMG_ASTEROIDBIG= pygame.image('asteroid-big.png').convert_alpha() #convert alpha wczytuje obrazek z png czyli z pustym tłem

pygame.display.set_caption('Asteroids')

CLOCK = pygame.time.Clock()



# GAME CLASSES AND METHODS
class PyladiesGameObject(GameObject):
	def draw(self,surface):
		surface.blit(IMG_ASTEROID_BIG,self.pos)
	pass


# GAME INIT

done = False
gm=PyladiesGameObject((200,200),50,0,0)


while not done:

    # EVENTS

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True



    # LOGIC



    # DRAWING
SCREEN.fill(0,0,55)
SCREEN.blit(IMG_EARTH, (0,0))
SCREEN.blit(IMG_ASTEROIDS_BIG, (100,100))
SCREEN.blit(IMG_ASTEROIDS_BIG, (300,400))
pygame.display.flip()
CLOCK.tick(60)