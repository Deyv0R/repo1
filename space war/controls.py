import pygame, sys
from bullet import Bullet
from enemy import Ino
import time

def events(screen, gun, bullets):               #обробка собитій
    pygame.mixer.init()
    gunshot_sound = pygame.mixer.Sound("space war\sound for game\laser 1.mp3")
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:    
                 if event.key == pygame.K_d:     # Вправо
                      gun.mright = True
                 elif event.key == pygame.K_a:   # вліво
                      gun.mleft = True
                 elif event.key == pygame.K_SPACE:
                      new_bullet = Bullet(screen, gun)
                      bullets.add(new_bullet)
                      gunshot_sound.play()
            elif event.type == pygame.KEYUP:     
                 if event.key == pygame.K_d:    # Вправо
                      gun.mright = False
                 elif event.key == pygame.K_a:    # вліво
                      gun.mleft = False

def update(bg_color, screen, stats, sc, gun, enemys, bullets):       # оновлення екрану
     screen.fill(bg_color)
     sc.show_score()
     for bullet in bullets.sprites():
          bullet.draw_bullet()
     gun.output()
     enemys.draw(screen)
     pygame.display.flip()

def update_bullets(screen, stats, sc, enemys, bullets):        # оновлення позиції пуль
     bullets.update()
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     colission = pygame.sprite.groupcollide(bullets, enemys, True, True)
     if colission:
          for enemys in colission.values():
               stats.score += 10 * len(enemys)
          sc.image_score()
          check_high_score(stats, sc)
          sc.image_guns()
     if len(enemys) == 0:
          bullets.empty()
          creat_army(screen, enemys)

def gun_kill(stats, screen, sc, gun, enemys, bullets):         #зіткнення пушки і прибульців
     if stats.guns_left > 0:
         stats.guns_left -= 1
         sc.image_guns()
         enemys.empty()
         bullets.empty()
         creat_army(screen, enemys)
         gun.create_gun()
         time.sleep(1)
     else:
         stats.run_game = False
         sys.exit()

def update_enemys(stats, screen, sc, gun, enemys, bullets):             # обновлює позицію прибульців
     enemys.update()
     if pygame.sprite.spritecollideany(gun, enemys):
          gun_kill(stats, screen, sc, gun, enemys, bullets)
     enemys_check(stats, screen, sc, gun, enemys, bullets)

def enemys_check(stats, screen, sc, gun, enemys, bullets):           # перевірка, чи дібрались прибульці до краю екрана
     screen_rect = screen.get_rect()
     for enemy in enemys.sprites():
          if enemy.rect.bottom >= screen_rect.bottom:
               gun_kill(stats, screen, sc, gun, enemys, bullets)
               break

def creat_army(screen, enemys):      # створення армії прибульців
     enemy = Ino(screen)
     enemy_width = enemy.rect.width
     number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
     enemy_height = enemy.rect.height
     number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)

     for row_number in range(number_enemy_y - 6):          
         for enemy_number in range(number_enemy_x):
             enemy = Ino(screen)
             enemy.x = enemy_width + (enemy_width * enemy_number)
             enemy.y = enemy_height + (enemy_height * row_number)
             enemy.rect.x = enemy.x
             enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
             enemys.add(enemy)

def check_high_score(stats, sc):               # перевірка нових рекордів
     if stats.score > stats.high_score:
          stats.high_score = stats.score
          sc.image_high_score()
          with open('space war\highscore.txt', 'w') as f:
               f.write(str(stats.high_score))

