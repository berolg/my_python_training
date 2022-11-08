import sys
import pygame
from pygame.sprite import Sprite, Group

class Settings():
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (106, 106, 155)

        self.tyan_speed_factor = 4
        self.donut_speed_factor = 6

        self.donuts_allowed = 3

class Tyan():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('upr12_2.bmp')
        self.image = pygame.transform.scale(self.image, (350, 219))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.left = self.screen_rect.left - 100
        self.rect.centery = self.screen_rect.centery

        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.tyan_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.tyan_speed_factor

        self.rect.centery = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Donut(Sprite):
    def __init__(self, ai_settings, screen, tyan):
        super().__init__()
        self.screen = screen
        self.tyan = tyan
        self.donut_image = pygame.image.load('donut.bmp')
        self.donut_image = pygame.transform.scale(self.donut_image, (60, 50))
        self.rect = self.donut_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centery = self.tyan.rect.centery
        self.rect.left = tyan.rect.left + 150

        # Позиция пули хранится в вещественном формате
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.donut_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.donut_image, self.rect)

def check_keydown_events(event, ai_settings, screen, tyan, donuts):
    if event.key == pygame.K_DOWN:
        tyan.moving_down = True
    elif event.key == pygame.K_UP:
        tyan.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_donut(ai_settings, screen, tyan, donuts)

def fire_donut(ai_settings, screen, tyan, donuts):
    if len(donuts) < ai_settings.donuts_allowed:
        new_donut = Donut(ai_settings, screen, tyan)
        donuts.add(new_donut)

def check_keyup_events(event, tyan):
    if event.key == pygame.K_DOWN:
        tyan.moving_down = False
    elif event.key == pygame.K_UP:
        tyan.moving_up = False

def check_events(ai_settings, screen, tyan, donuts):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, tyan, donuts)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, tyan)

def update_screen(ai_settings, screen, tyan, donuts):
    screen.fill(ai_settings.bg_color)
    for donut in donuts.sprites():
        donut.blitme()
    tyan.blitme()
    pygame.display.flip()

def update_donuts(ai_settings, donuts):
    donuts.update()
    for donut in donuts.copy():
        if donut.rect.right > donut.screen_rect.right:
            donuts.remove(donut)

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, 
        ai_settings.screen_height))
    pygame.display.set_caption('Angry tyan donuts')
    tyan = Tyan(ai_settings, screen)
    donuts = Group()

    while True:
        check_events(ai_settings, screen, tyan, donuts)
        tyan.update()
        update_screen(ai_settings, screen, tyan, donuts)
        update_donuts(ai_settings, donuts)

run_game()