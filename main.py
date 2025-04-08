import pygame
import sys
from game import Game
from colors import Colors

# Inicializace pygame
pygame.init()

# Nastavení fontu a textových nápisů
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.bila)
next_surface = title_font.render("Next", True, Colors.bila)
game_over_surface = title_font.render("GAME OVER", True, Colors.bila)
high_score_surface = title_font.render("High Score", True, Colors.bila)

# Obdélníky pro zobrazení skóre a dalšího bloku
score_rect = pygame.Rect(320, 55, 170, 60)
high_score_rect = pygame.Rect(320, 500, 170, 65)
next_rect = pygame.Rect(320, 215, 170, 180)

# Vytvoření herního okna
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Hodiny pro řízení FPS
clock = pygame.time.Clock()

# Vytvoření instance hry
game = Game()

# Vlastní událost pro automatický pád bloku dolů
GAME_UPDATE = pygame.USEREVENT
initial_speed = 500
pygame.time.set_timer(GAME_UPDATE, initial_speed)

# Hlavní herní smyčka
while True:
    for event in pygame.event.get():
        # Klávesové vstupy
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
                pygame.time.set_timer(GAME_UPDATE, initial_speed)
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()

        # Automatický pohyb bloku dolů
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

            if game.score > 1500:
                faster_speed = 200
                pygame.time.set_timer(GAME_UPDATE, faster_speed)
                if game.score > 3000:
                    faster_speed = 100
                    pygame.time.set_timer(GAME_UPDATE, faster_speed)


    # Výpočet a vykreslení skóre
    score_value_surface = title_font.render(str(game.score), True, Colors.bila)
    high_score_value_surface = title_font.render(str(game.high_score), True, Colors.bila)

    # Vyplnění pozadí barvou
    screen.fill(Colors.lososova)

    # Vykreslení nápisů
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    screen.blit(high_score_surface, (330, 470, 170, 65))

    # Rámeček a text pro skóre
    pygame.draw.rect(screen, Colors.svetla_modra, score_rect, 0, 30)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))

    # Rámeček a text pro high score
    pygame.draw.rect(screen, Colors.svetla_modra, high_score_rect, 0, 30)  # nove high skore
    screen.blit(high_score_value_surface, high_score_value_surface.get_rect(centerx=high_score_rect.centerx, centery=high_score_rect.centery))

    # Rámeček pro další blok
    pygame.draw.rect(screen, Colors.svetla_modra, next_rect, 0, 100)

    # Vykreslení herního pole a bloků
    game.draw(screen)

    # Aktualizace obrazovky
    pygame.display.update()

    # Omezení na 60 snímků za sekundu
    clock.tick(60)
    #game over
    if game.game_over == True:
        screen.fill(Colors.cerna)
        pygame.draw.rect(screen, Colors.fialova, [150, 90, 200, 100], 10, 10)
        pygame.draw.rect(screen, Colors.cervena, [150, 243, 200, 100], 10, 10)
        pygame.draw.rect(screen, Colors.modra, [150, 400, 200, 100], 10, 10)
        screen.blit(game_over_surface, (165, 280, 50, 50))
        screen.blit(high_score_surface, (175, 110, 50, 50))
        screen.blit(high_score_value_surface, (215, 150, 200, 200))
        screen.blit(score_surface, (210, 420, 50, 50))
        score_value_surface = title_font.render(str(game.score), True, Colors.bila)
        screen.blit(score_value_surface, score_value_surface.get_rect(center=(250, 470)))
        pygame.display.flip()

        pygame.time.wait(5000)

        pygame.quit()
        sys.exit()

