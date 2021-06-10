"""
This version is an explained version of pygame tutorial.
"""
import pygame

pygame.display.set_caption('Rectangle')# Names the pywindow game
background_color = (255, 255, 255) # white color
(width, height) = (300, 200) # Screen size
color = (0, 0, 0) # For rectangle

screen = pygame.display.set_mode((width, height)) # setting screen
screen.fill(background_color) # Fills white to screen
pygame.draw.rect(screen, color, (100,50,30,40), 2) # Drawing the rectangle
pygame.display.update()

# loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()