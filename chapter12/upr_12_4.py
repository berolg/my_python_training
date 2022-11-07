import pygame
import sys

class Settings():
    def __init__(self):
        self.bg_color = (0, 0, 100)
        self.screen_width = 1500
        self.screen_height = 700

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)

def update_screen(ai_settings, screen):
    screen.fill(ai_settings.bg_color)
    pygame.display.flip()

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Event key')

    while True:
        check_events()
        update_screen(ai_settings, screen)

run_game()

