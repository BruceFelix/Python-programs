"""
Adding background music and sound effects
"""
import pygame
import time

pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode((420, 420))

playlist = list()
playlist.append( "music.mp3")
playlist.append( "music.mp3")
playlist.append( "music.mp3")


pygame.mixer.music.load ( playlist.pop() ) # Get the first track from the playlist
pygame.mixer.music.queue ( playlist.pop() ) # Queue the 2nd song
pygame.mixer.music.set_endevent ( pygame.USEREVENT ) # Setup the end track event
pygame.mixer.music.play() # Play the music

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: # A track has ended
                if len ( playlist ) > 0: # If there are more tr acks in the queue...
                    pygame.mixer.music.queue ( playlist.pop() )      # Q        