import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):    # створюємо пулю в позиції пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 10)
        self.color = 255, 0, 0
        self.speed = 5.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):     # переміщення пулі
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):    # малюєм пулю на екрані
        pygame.draw.rect(self.screen, self.color, self.rect)
