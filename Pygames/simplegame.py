import pygame
successes, failures = pygame.init()
#This function returns a tuple of all successfully and failed initializations(IT won't raise an error if a modue fails to initialize)
print("{0} successes and {1} failures".format(successes,failures))# to make sure all modules work

# Creating necessities
screen = pygame.display.set_mode((720, 480))# Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 60 #This variable will define how many frames we update per second

#for readability we'll create two color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
# RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255)

#Surface for object and Rect to represent position of an object
rect = pygame.Rect((0,0), (32,32))# first tuple is position, second is size
image = pygame.Surface((32,32)) # The tuple represent size
image.fill(WHITE) #we will fill our surface with a nice white color (by default black)

while True:
    clock.tick(FPS)
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# The user pressed the close button in the top corner of  the window.
            quit()
            #close the program. Other methods like 'raise SystemExit' or 'sys.exit()'.
            #Calling 'programs.quit()' won't close the program! It will just uninitialize the modules
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0, -2) # Changes the rect's position.
            elif event.key == pygame.K_s:
                rect.move_ip(0, 2)
            elif event.key == pygame.K_a:
                rect.move_ip(-2, 0)
            elif event.key == pygame.K_d:
                rect.move_ip(2, 0)

    screen.fill(BLACK)
    screen.blit(image, rect)
    pygame.display.update() # Or 'pygame.display.flip()'.