import time
import random
import pygame as pg

from settings import *
from player import Player
from ball import Ball


class PongObjects:
    BALL_OBJ = Ball
    PLAYER_OBJ = Player


def checking_player_movement(player: Player, key) -> None:
    """ Checking player movement """
    match player.side:
        case 'left':
            if key[pg.K_w]:
                player.dir = "top"
                player.move()
            if key[pg.K_s]:
                player.dir = "bottom"
                player.move()
        case 'right':
            if key[pg.K_UP]:
                player.dir = "top"
                player.move()
            if key[pg.K_DOWN]:
                player.dir = "bottom"
                player.move()


def checking_player_and_ball_collision(player: Player, ball: Ball) -> None:
    """ Checking the collision of the ball with the player """
    match player.side:
        case 'left':
            if player.rect.colliderect(ball):
                match ball.dir:
                    case "bottom-left": ball.dir = "bottom-right"
                    case "top-left"   : ball.dir = "top-right"
        case 'right':
            if player.rect.colliderect(ball):
                match ball.dir:
                    case "bottom-right": ball.dir = "bottom-left"
                    case "top-right"   : ball.dir = "top-left"


def checking_y_collision(obj: Ball | Player) -> None:
    """ Checking the collision of the ball or player by the y-coordinate """
    match type(obj):
        case PongObjects.BALL_OBJ:
            if obj.rect.y <= 0:
                obj.rect.y = 0
                match obj.dir:
                    case "top-right": obj.dir = "bottom-right"
                    case "top-left" : obj.dir = "bottom-left"
            if obj.rect.y >= HEIGHT:
                obj.rect.y = HEIGHT
                match obj.dir:
                    case "bottom-left" : obj.dir = "top-left"
                    case "bottom-right": obj.dir = "top-right"
        case PongObjects.PLAYER_OBJ:
            if obj.rect.y <= 0:
                obj.rect.y = 0
            if obj.rect.y + obj.rect.height >= HEIGHT:
                obj.rect.y = HEIGHT - obj.rect.height


def checking_x_collision(player_left: Player, player_right: Player, ball: Ball) -> None:
    """ Checking the collision of the ball by the x-coordinate """
    if ball.rect.x <= 0 or ball.rect.x >= WIDTH:
        if ball.rect.x <= 0:
            ball.dir = random.choice(["top-left", "bottom-left"])
            player_right.score = player_right.score + 1
        if ball.rect.x >= WIDTH:
            ball.dir = random.choice(["top-right", "bottom-right"])
            player_left.score = player_left.score + 1
        ball.rect.x = BALL["dx"]
        ball.rect.y = BALL["dy"]
        time.sleep(.25)


def run() -> None:
    """ Launching the Pong """
    pg.init()
    pg.display.set_caption("Pong")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    ball = Ball()
    player_left = Player('left')
    player_right = Player('right')
    score_left = pg.font.SysFont(SCORE["font"], SCORE["size"])
    score_right  = pg.font.SysFont(SCORE["font"], SCORE["size"])
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        score_left_surface = score_left.render(str(player_left.score), False, SCORE["color"])
        score_right_surface = score_right.render(str(player_right.score), False, SCORE["color"])
        
        screen.fill(BG_COLOR)

        pg.draw.line(screen, CENTRAL_LINE["color"], (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), CENTRAL_LINE["width"])

        pg.draw.rect(screen, BALL["color"], ball.rect)
        pg.draw.rect(screen, PLAYER["color"], player_left.rect)
        pg.draw.rect(screen, PLAYER["color"], player_right.rect)

        screen.blit(score_left_surface, (SCORE["dx"] - (score_left_surface.get_width() // 2), SCORE["dy"]))
        screen.blit(score_right_surface, (WIDTH - SCORE["dx"] - (score_left_surface.get_width() // 2), SCORE["dy"]))
        
        key = pg.key.get_pressed()
        checking_player_movement(player_left, key)
        checking_player_movement(player_right, key)

        checking_player_and_ball_collision(player_left, ball)
        checking_player_and_ball_collision(player_right, ball)

        checking_y_collision(player_left)
        checking_y_collision(player_right)
        checking_y_collision(ball)

        checking_x_collision(player_left, player_right, ball)

        ball.move()
        
        pg.display.flip()
        clock.tick(FPS)
        

if __name__ == "__main__": run()