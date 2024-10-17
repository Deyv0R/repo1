import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))  # flags= pygame.NOFRAME -- убирає рамки окна
pygame.display.set_caption('game 2')
icon = pygame.image.load('python game 2\image for game\icon.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('python game 2\image for game\Game_Background_190.png').convert_alpha()
walk_right = [
    pygame.image.load('python game 2/image for game/player right/right 1.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player right/right 2.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player right/right 3.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player right/right 4.png').convert_alpha()
]

walk_left = [
    pygame.image.load('python game 2/image for game/player left/left 1.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player left/left 2.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player left/left 3.png').convert_alpha(),
    pygame.image.load('python game 2/image for game/player left/left 4.png').convert_alpha()
]

enemy = pygame.image.load('python game 2/image for game/ghost.png').convert_alpha()
enemy_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 440
player_y = 569
is_jump = False
jump_count = 9

bg_sound = pygame.mixer.Sound('python game 2\\sound for game\\forest-wind-and-birds-6881.mp3')
bg_sound.play()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 2500)

gameplay = True

run = True
while run:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1280, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    
        if enemy_list_in_game:
            for el in enemy_list_in_game:
                screen.blit(enemy, el)
                el.x -= 10

            if player_rect.colliderect(el):
                print('You lose loser')
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_a] and player_x >50:
            player_x -= 6
        elif keys[pygame.K_d] and player_x <1100:
            player_x += 6
    
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1280:
            bg_x = 0
    
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft=(1284, 550)))
    clock.tick(20)
