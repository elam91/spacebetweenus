import sys
import pygame
import os
import time
import random

pygame.font.init()
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey Fracas Jr.")

# Player Spaceship
MAIN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "main_ship.png"))

# Enemy Spaceships
ENEMY_SHIP_BLUE = pygame.image.load(os.path.join("assets", "enemy_ship_blue.png"))
ENEMY_SHIP_RED = pygame.image.load(os.path.join("assets", "enemy_ship_red.png"))
ENEMY_SHIP_GREEN = pygame.image.load(os.path.join("assets", "enemy_ship_green.png"))

# Enemy Bosses
FIRST_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "monkey.png")), (200, 200))
SECOND_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "lrrr.png")), (200, 200))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
BARREL = pygame.transform.scale(pygame.image.load(os.path.join("assets", "barrel.png")), (100, 100))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(self, obj)


class BossLaser(Laser):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
        self.horizontal = random.choice(['LEFT', 'RIGHT'])
        self.vertical = random.choice(['TOP', 'BOTTOM'])
        self.shoot_random = random.randint(1, 3)

    def move(self, vel):
        if self.vertical == 'TOP':
            y_vel = -vel
        elif self.vertical == 'BOTTOM':
            y_vel = vel
        if self.horizontal == 'RIGHT':
            x_vel = vel
        elif self.horizontal == 'LEFT':
            x_vel = -vel
        if self.shoot_random == 1:
            self.x += x_vel
            self.y += y_vel
        elif self.shoot_random == 2:
            self.x += x_vel
        elif self.shoot_random == 3:
            self.y += y_vel


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = MAIN_SPACE_SHIP
        self.laser_img = GREEN_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                if laser.off_screen(HEIGHT):
                    self.lasers.remove(laser)
                for obj in objs:
                    if laser.collision(obj):
                        if not isinstance(obj, Boss):
                            if not laser.off_screen(HEIGHT):
                                objs.remove(obj)
                        else:
                            obj.health -= (obj.level * 3)
                            if obj.health <= 0:
                                objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))


class Enemy(Ship):
    COLOR_MAP = {'red': (ENEMY_SHIP_RED, YELLOW_LASER),
                 'green': (ENEMY_SHIP_GREEN, BLUE_LASER),
                 'blue': (ENEMY_SHIP_BLUE, RED_LASER)
                 }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 15, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Boss(Ship):
    BOSS_MAP = {
        5: (FIRST_BOSS, YELLOW_LASER, BARREL),
        10: (SECOND_BOSS, RED_LASER, BARREL)
    }
    COOLDOWN = 2

    def __init__(self, x, y, level):
        super().__init__(x, y)
        try:
            self.ship_img, self.laser_img, self.projectile_img = self.BOSS_MAP[level]
        except:
            self.ship_img, self.laser_img, self.projectile_img = random.choice(FIRST_BOSS, SECOND_BOSS), random.choice(
                RED_LASER, YELLOW_LASER, GREEN_LASER, BLUE_LASER), BARREL
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health = 100 * level
        self.max_health = self.health
        self.level = level
        self.movedir = random.choice(['RIGHT', 'LEFT'])

    def move(self, vel):
        if self.y < (HEIGHT // 2) - (self.get_height() // 2):
            self.y += vel
        else:
            if (self.movedir == 'RIGHT'):
                if (self.x <= (WIDTH - self.get_width())):
                    self.x += vel
                else:
                    self.movedir = 'LEFT'
            elif (self.movedir == 'LEFT'):
                if (self.x > 0):
                    self.x -= vel
                else:
                    self.movedir = 'RIGHT'

    def shoot(self):
        laser = BossLaser(self.x - 15, self.y, self.laser_img)
        self.lasers.append(laser)

    def shoot_projectile(self):
        projectile = BossLaser(self.x - 15, self.y, self.projectile_img)
        self.lasers.append(projectile)
        self.cool_down_counter = 1

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def move_lasers(self, vel, obj):
        vel = vel * (self.max_health // 100)
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 20
                self.lasers.remove(laser)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(text):
    big_font = pygame.font.Font(os.path.join("assets", "Pixelation.ttf"), 50)
    if len(text) > 10:
        big_font = pygame.font.Font(os.path.join("assets", "Pixelation.ttf"), 40)
    TextSurf, TextRect = text_objects(text, big_font)
    TextRect.center = ((WIDTH // 2), (HEIGHT // 2))
    WIN.blit(TextSurf, TextRect)


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.Font(os.path.join("assets", "Pixelation.ttf"), 25)
    big_font = pygame.font.Font(os.path.join("assets", "Pixelation.ttf"), 50)
    enemies = []
    wave_length = 5
    enemy_vel = 1
    main.display_level_text = False
    player_vel = 5
    player_laser_vel = 6
    laser_vel = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, ((WIDTH - level_label.get_width() - 10), 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if main.display_level_text:
            if level % 5 == 0:
                message_display(f"""
                Level {level} - BOSS FIGHT 
                """)
            else:
                message_display(f"Level {level}")
            if ((time.time() - start_time) > 3):
                main.display_level_text = False

        if lost:
            lost_label = big_font.render("GAME OVER", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH // 2 - lost_label.get_width() // 2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if lives <= 0:
            lost = True
            lost_count += 1

        elif player.health <= 0:
            lives -= 1
            player.health = player.max_health

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            main.display_level_text = True
            start_time = time.time()
            if ((level) % 5 == 0):
                boss = Boss(WIDTH // 2, -200, level)
                boss.x = (WIDTH // 2) - (boss.get_width() // 2)
                enemies.append(boss)
            else:
                wave_length += 5
                if level > 1:
                    player.health += 10
                    player.healthbar(WIN)
                    player_laser_vel += 2
                    player_vel += level // 3
                    if level < 7:
                        player.COOLDOWN -= 4
                    if level > 2:
                        enemy_vel = level // 3

                for i in range(wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                  random.choice(['red', 'blue', 'green']))
                    enemies.append(enemy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and (player.x - player_vel > 0):  # left
            player.x -= player_vel
        if keys[pygame.K_d] and (player.x + player_vel + player.get_width() < WIDTH):  # right
            player.x += player_vel
        if keys[pygame.K_w] and (player.y - player_vel > 0):  # up
            player.y -= player_vel
        if keys[pygame.K_s] and (player.y + player_vel + player.get_height() + 15 < HEIGHT):  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            if not isinstance(enemy, Boss):
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if (random.randrange(0, 2 * FPS) == 1) and (enemy.y >= 0):
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy)
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)
            else:
                enemy.move(enemy_vel + 2)
                enemy.move_lasers(laser_vel, player)
                if (random.randrange(0, int(0.5 * FPS)) == 1):
                    enemy.shoot()
                if (random.randrange(0, 1 * FPS) == 1):
                    enemy.shoot_projectile()
                if collide(enemy, player):
                    player.health -= 10

        player.move_lasers(-player_laser_vel, enemies)


def main_menu():
    title_font = pygame.font.Font(os.path.join("assets", "Pixelation.ttf"), 30)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press any key to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH // 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()


main_menu()
