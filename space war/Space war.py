import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from score import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space war')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemys = Group()
    controls.creat_army(screen, enemys)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game: 
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, enemys, bullets)
            controls.update_bullets(screen, stats, sc, enemys, bullets)
            controls.update_enemys(stats, screen, sc, gun, enemys, bullets)

run()

