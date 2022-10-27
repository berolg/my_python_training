import sys
import pygame

#upr_12_1 + 12_2

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('upr12_2.bmp')
        self.image = pygame.transform.scale(self.image, (350, 219))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1300, 700))
    bg_color = (0, 0, 255)
    pygame.display.set_caption('Blue sky')

    player = Player(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        player.blitme()
        pygame.display.flip()

run_game()

