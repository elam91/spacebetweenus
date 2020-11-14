import sys
import pygame
import os
import time
import random

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
pygame.display.init()
pygame.font.init()
DISPLAY = pygame.display.Info()
WIDTH, HEIGHT = DISPLAY.current_w, DISPLAY.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SCALED | pygame.NOFRAME)

pygame.display.set_caption("Space Between Us")



# Player Spaceship
MAIN_SPACE_SHIP = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "main_ship.png")))
SHIELD = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "main_ship_shield.png")))

# Enemy Spaceships
ENEMY_SHIP_BLUE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_ship_blue.png")),(72,55))
ENEMY_SHIP_RED = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_ship_red.png")),(72,55))
ENEMY_SHIP_GREEN = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_ship_green.png")),(72,55))
ENEMY_SHIP_YELLOW = pygame.transform.scale(pygame.image.load(os.path.join("assets", "enemy_ship_yellow.png")),(72,55))

# Enemy Bosses
FIRST_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Boss1.png")), (200, 200))
SECOND_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Boss2.png")), (200, 200))
THIRD_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Boss3.png")), (200, 200))
FOURTH_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Boss4.png")), (200, 200))
FIFTH_BOSS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Boss5.png")), (200, 200))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#projectiles
BARREL = pygame.transform.scale(pygame.image.load(os.path.join("assets", "barrel.png")), (100, 100))
BOX = pygame.transform.scale(pygame.image.load(os.path.join("assets", "box.png")), (100, 100))
ROCKET_BIG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "rocketbig.png")), (500, 500))

#powerups
BURGER = pygame.image.load(os.path.join("assets", "burger.png"))
DONUT = pygame.image.load(os.path.join("assets", "donut.png"))
DEATH = pygame.image.load(os.path.join("assets", "death.png"))
POTION = pygame.image.load(os.path.join("assets", "potion.png"))
ROCKET_SMALL = pygame.image.load(os.path.join("assets", "rocketsmall.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

# Cinematic
CIN_BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "cinematicbg.png")), (WIDTH, HEIGHT))
CIN_STARS = pygame.transform.scale(pygame.image.load(os.path.join("assets", "cinematicstars.png")), (WIDTH, HEIGHT))

STAR1_1 = pygame.image.load(os.path.join("assets","star1" ,"star1.png"))
STAR1_2 = pygame.image.load(os.path.join("assets","star1" ,"star2.png"))
STAR1_3 = pygame.image.load(os.path.join("assets","star1" ,"star3.png"))
STAR1_4 = pygame.image.load(os.path.join("assets","star1" ,"star4.png"))
STAR1_5 = pygame.image.load(os.path.join("assets","star1" ,"star5.png"))
STAR1_6 = pygame.image.load(os.path.join("assets","star1" ,"star6.png"))
STAR1_7 = pygame.image.load(os.path.join("assets","star1" ,"star7.png"))
STAR1_8 = pygame.image.load(os.path.join("assets","star1" ,"star8.png"))

STAR2_1 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star1.png")))
STAR2_2 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star2.png")))
STAR2_3 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star3.png")))
STAR2_4 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star4.png")))
STAR2_5 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star5.png")))
STAR2_6 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star6.png")))
STAR2_7 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star7.png")))
STAR2_8 = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","star2" ,"star7.png")))

COMET1 = pygame.image.load(os.path.join("assets","comet" ,"comet1.png"))
COMET2 = pygame.image.load(os.path.join("assets","comet" ,"comet2.png"))
COMET3 = pygame.image.load(os.path.join("assets","comet" ,"comet3.png"))
COMET4 = pygame.image.load(os.path.join("assets","comet" ,"comet4.png"))
COMET5 = pygame.image.load(os.path.join("assets","comet" ,"comet5.png"))
COMET6 = pygame.image.load(os.path.join("assets","comet" ,"comet6.png"))
COMET7 = pygame.image.load(os.path.join("assets","comet" ,"comet7.png"))
COMET8 = pygame.image.load(os.path.join("assets","comet" ,"comet8.png"))

DAVID = pygame.image.load(os.path.join("assets", "david.png"))
JONATHAN = pygame.image.load(os.path.join("assets", "jonathan.png"))

if WIDTH > 1000 and HEIGHT > 1000:
    DISPLAY_MODE = 2
else:
    DISPLAY_MODE = 1

class StarSprite:
    STAR1_LIST = [STAR1_1,STAR1_2,STAR1_3,STAR1_4,STAR1_5,STAR1_6,STAR1_7,STAR1_8]
    STAR2_LIST = [STAR2_1,STAR2_2,STAR2_3,STAR2_4,STAR2_5,STAR2_6,STAR2_7,STAR2_8]
    COMET_LIST = [COMET1,COMET2,COMET3,COMET4,COMET5,COMET6,COMET7,COMET8]
    def __init__(self,arg,x,y):
        self.x = x
        self.y = y
        self.frame = 0
        if arg == 'comet':
            self.img_list = self.COMET_LIST
        elif arg == 'star1':
            self.img_list = self.STAR1_LIST
        elif arg == 'star2':
            self.img_list = self.STAR2_LIST
        else:
            self.img_list = []

    def draw(self,window):
        window.blit(self.img_list[self.frame//3],(self.x,self.y))
        self.frame += 1
        if self.frame // 3 > 7:
            self.frame = 0


class PowerUp:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def move(self,vel):
        self.y += vel

    def off_screen(self,height):
        return not self.y <= height and self.y >= 0

    def collision(self,obj):
        return collide(self, obj)

    def draw(self,window):
        window.blit(self.img, (self.x, self.y))

    def which_powerup(self):
        if self.img == BURGER:
            return 'BURGER'
        elif self.img == DONUT:
            return 'DONUT'
        elif self.img == POTION:
            return 'POTION'
        elif self.img == DEATH:
            return 'DEATH'
        elif self.img == ROCKET_SMALL:
            return 'ROCKET'

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
                if isinstance(obj,Player):
                    if obj.shield_on == False:
                        obj.health -= 10
                else:
                    obj.health -= 10
                if laser.img != ROCKET_BIG:
                    self.lasers.remove(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+5, self.y-self.get_height()//2, self.laser_img)
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
        self.rocket_count = 0
        self.power_up_start_time = None
        self.laser_vel = 6
        self.cooldown_saver = None
        self.vel_saver = None
        self.shield_start_time = None
        self.shield_on = False
        self.mega_laser_on = False

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        if not isinstance(obj, Boss):
                            if not laser.off_screen(HEIGHT):
                                if not obj.y + obj.ship_img.get_height() < 0:
                                    objs.remove(obj)
                        else:
                            obj.health -= (obj.level * 3)
                            if obj.health <= 0:
                                objs.remove(obj)
                        if laser in self.lasers:
                            if laser.img != ROCKET_BIG:
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
    def shoot_rocket(self):
        if self.rocket_count > 0:
            if self.cool_down_counter == 0:
                self.cooldown()
                rocket = Laser(self.x - (ROCKET_BIG.get_width()//2) + (self.ship_img.get_width()//2) , self.y-self.get_height()//2, ROCKET_BIG)
                self.lasers.append(rocket)
                self.cool_down_counter = 1
                self.rocket_count -= 1

    def give_laser(self):
        self.power_up_start_time = time.time()
        if self.mega_laser_on == False:
            self.laser_img = RED_LASER
            self.cooldown_saver = self.COOLDOWN
            self.vel_saver = self.laser_vel
            self.COOLDOWN = 2
            self.laser_vel = 15
            self.mega_laser_on = True
        else:
            pass

    def take_laser(self):
        if self.mega_laser_on == True:
            if self.power_up_start_time != None:
                if (time.time() - self.power_up_start_time >= 5):
                    self.laser_img = GREEN_LASER
                    self.COOLDOWN = self.cooldown_saver
                    self.laser_vel = self.vel_saver
                    self.mega_laser_on = False


class Enemy(Ship):
    COLOR_MAP = {'red': (ENEMY_SHIP_RED, YELLOW_LASER),
                 'green': (ENEMY_SHIP_GREEN, BLUE_LASER),
                 'blue': (ENEMY_SHIP_BLUE, RED_LASER),
                 'yellow' : (ENEMY_SHIP_YELLOW, RED_LASER)
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
        10: (SECOND_BOSS, RED_LASER, BOX),
        15: (THIRD_BOSS,BLUE_LASER, BARREL),
        20: (FOURTH_BOSS, GREEN_LASER,BOX),
        25: (FIFTH_BOSS, RED_LASER, BARREL)
    }
    COOLDOWN = 2

    def __init__(self, x, y, level):
        super().__init__(x, y)
        try:
            self.ship_img, self.laser_img, self.projectile_img = self.BOSS_MAP[level]
        except:
            self.ship_img, self.laser_img, self.projectile_img = random.choice([FIRST_BOSS,SECOND_BOSS,THIRD_BOSS,FOURTH_BOSS,FIFTH_BOSS]), random.choice(
                [RED_LASER, YELLOW_LASER, GREEN_LASER, BLUE_LASER]), random.choice([BARREL,BOX])
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
        self.cool_down_counter = 1

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
                self.lasers.remove(laser)
                if obj.shield_on == False:
                    obj.health -= 20


    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
        self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health),
        10))

def randomize_powerup(powerups):
    rand_powerup = PowerUp(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),random.choice([BURGER,DONUT,POTION,ROCKET_SMALL,DEATH]))
    powerups.append(rand_powerup)


def give_shield(player):
    player.shield_start_time = time.time()
    if player.shield_on == False:
        player.ship_img = SHIELD
        player.shield_on = True


def take_shield(player):
    if player.shield_start_time != None:
        if player.shield_on ==  True:
            if (time.time() - player.shield_start_time >= 10):
                player.ship_img = MAIN_SPACE_SHIP
                player.shield_on = False

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def cinematic_story_display(text,surface,x,y,type1='story'):
    story_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 25 * DISPLAY_MODE)
    speech_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 15 * DISPLAY_MODE)
    if type1 == 'story':
        font = story_font
    elif type1 == 'speech':
        font = speech_font
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = WIDTH-10, HEIGHT-10
    pos = x,y
    for line in words:
        for word in line:
            word_surface = font.render(word, 1, (255,255,255))
            word_width, word_height = word_surface.get_size()
            surface.blit(word_surface, (x, y))
            x += word_width + space
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.

        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def message_display(text):
    big_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 70*DISPLAY_MODE)
    if len(text) > 10:
        big_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 50*DISPLAY_MODE)
    TextSurf, TextRect = text_objects(text, big_font)
    TextRect.center = ((WIDTH // 2), (HEIGHT // 2))
    WIN.blit(TextSurf, TextRect)


def main():
    run = True
    FPS = 60
    player = Player(300, 630)
    level = 0
    lives = 5
    main_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 35*DISPLAY_MODE)
    big_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 50*DISPLAY_MODE)
    enemies = []
    wave_length = 5
    enemy_vel = 1
    main.display_level_text = False
    player_vel = 5
    laser_vel = 5
    powerups = []




    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window(player):
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        for i in range(player.rocket_count):
            pygame.draw.rect(WIN, (255, 255,255),  (10+(i*40),60,ROCKET_SMALL.get_height(), ROCKET_SMALL.get_width()))
            WIN.blit(ROCKET_SMALL,(10+(i*40),60))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, ((WIDTH - level_label.get_width() - 10), 10))

        for enemy in enemies:
            enemy.draw(WIN)

        for powerup in powerups:
            powerup.draw(WIN)

        player.draw(WIN)

        if main.display_level_text:
            if level % 5 == 0:
                message_display(f"Level {level} - BOSS FIGHT")
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
        redraw_window(player)

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
                    player.laser_vel += 2
                    player_vel += level // 3
                    if level < 7:
                        player.COOLDOWN -= 4
                    elif level < 10:
                        player.COOLDOWN -= 1
                    if level > 2:
                        enemy_vel = level // 3

                for i in range(wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                                  random.choice(['red', 'blue', 'green']))
                    enemies.append(enemy)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
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
        if keys[pygame.K_RSHIFT]:
            if player.rocket_count > 0:
                player.shoot_rocket()
        if keys[pygame.K_p]:
            pause()



        for powerup in powerups:
            powerup.move(enemy_vel)
            if collide(powerup,player):
                current_powerup = powerup.which_powerup()
                if current_powerup == 'ROCKET':
                    player.rocket_count += 1
                elif current_powerup == 'DONUT':
                    give_shield(player)
                elif current_powerup == 'POTION':
                    player.give_laser()
                elif current_powerup == 'DEATH':
                    for enemy in enemies:
                        if enemy.y > 0 - enemy.ship_img.get_height():
                            if not isinstance(enemy,Boss):
                                enemies.remove(enemy)
                            else:
                                enemy.health -= 200
                                if enemy.health <= 0:
                                    enemies.remove(enemy)

                elif current_powerup == 'BURGER':
                    lives += 1
                powerups.remove(powerup)
        player.take_laser()
        take_shield(player)

        for enemy in enemies[:]:
            if not isinstance(enemy, Boss):
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)
                if (random.randrange(0, 2 * FPS) == 1) and (enemy.y >= 0):
                    enemy.shoot()

                if collide(enemy, player):
                    enemies.remove(enemy)
                    if player.shield_on == False:
                        player.health -= 10
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
                    if player.shield_on == False:
                     player.health -= 10
        if level != 1:
            if (random.randrange(0, int((100//level)* FPS)) == 1):
                randomize_powerup(powerups)

        player.move_lasers(-player.laser_vel, enemies)


def main_menu():
    run = True
    title_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 30*DISPLAY_MODE)
    main_title_font = pygame.font.Font(os.path.join("assets", "pixel2.otf"), 45*DISPLAY_MODE)
    main_title_label = main_title_font.render("Space Between Us", 1, (255, 255, 255))
    title_label = title_font.render("Press any key to begin...", 1, (255, 255, 255))
    while run:
        WIN.blit(BG, (0, 0))
        WIN.blit(title_label, (WIDTH // 2 - title_label.get_width() // 2, HEIGHT//2+title_label.get_height()*2))
        WIN.blit(main_title_label,(WIDTH // 2 - main_title_label.get_width() // 2,HEIGHT//2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                cinematic()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
    pygame.quit()

def cinematic():
    FPS = 60
    frame_time = 0
    frame = 1
    clock = pygame.time.Clock()
    run = True
    clock.tick(FPS)
    sprites = []
    fake_player = Player(WIDTH//2,HEIGHT-MAIN_SPACE_SHIP.get_width())
    fake_enemies = []
    for i in range(20):
        fake_enemies.append(Enemy(random.randint(10*DISPLAY_MODE,WIDTH),random.randint(10*DISPLAY_MODE,HEIGHT),'red'))
    for i in range(10):
        sprites.append(StarSprite(random.choice(['star1','star2','comet']),random.randint(10,WIDTH-10),random.randint(10,HEIGHT-10)))
    skip_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 15 * DISPLAY_MODE)
    speech_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 10 * DISPLAY_MODE)
    main_title_font = pygame.font.Font(os.path.join("assets", "pixel2.otf"), 45 * DISPLAY_MODE)
    main_title_label = main_title_font.render("Space Between Us", 1, (255, 255, 255))
    frame4_label = skip_font.render("""But Starbreit will never give up. 
    He will do whatever it takes to rescue his love.
    Even now you can hear his voice echo inside the walls of his spaceship.
     """, 1, (255, 255, 255))
    frame3_speech = speech_font.render("David, it's time to cross the space between us", 1, (255, 255, 255))

    skip_label = skip_font.render("Press ENTER to skip...", 1, (255, 255, 255))
    while run:

        if frame == 1:
            WIN.blit(CIN_BG, (0, 0))
            WIN.blit(CIN_STARS, (0, 0))
            WIN.blit(main_title_label, (WIDTH // 2 - main_title_label.get_width() // 2, HEIGHT // 2))
            WIN.blit(skip_label,
                 (WIDTH // 2 - skip_label.get_width() // 2, HEIGHT - skip_label.get_height() - 10 * DISPLAY_MODE))
            frame_time += 1
            if frame_time > 2*FPS:
                frame += 1
                frame_time = 0
            pygame.display.update()
        elif frame == 2:
            WIN.blit(CIN_BG, (0, 0))
            WIN.blit(CIN_STARS,(0,0))
            WIN.blit(skip_label,
                     (WIDTH // 2 - skip_label.get_width() // 2, HEIGHT - skip_label.get_height() - 10 * DISPLAY_MODE))
            for sprite in sprites:
                sprite.draw(WIN)
            cinematic_story_display("""It's the second sunset on planet Querton Utera 7-A,
where hours from now Jonathan Starbreit will marry his one true love - David Novacohn""",WIN,20,20)
            pygame.display.update()
            frame_time +=1
            if frame_time > 2*FPS:
                frame += 1
                frame_time = 0
        elif frame == 3:
            WIN.blit(JONATHAN,(10+JONATHAN.get_width(),HEIGHT-JONATHAN.get_height()))
            cinematic_story_display('I love you David', WIN, JONATHAN.get_width(), (HEIGHT-JONATHAN.get_height())- skip_font.get_height(),'speech')
            pygame.display.update()
            frame_time += 1
            if frame_time > 4*FPS:
                frame += 1
                frame_time = 0
        elif frame == 4:
            WIN.blit(DAVID,(WIDTH-DAVID.get_width()*2 ,HEIGHT-DAVID.get_height()))
            cinematic_story_display('I love you too Jonathan', WIN,WIDTH - DAVID.get_width()*2, (HEIGHT - DAVID.get_height()) - skip_font.get_height(), 'speech')
            pygame.display.update()
            frame_time += 1
            if frame_time > 4 * FPS:
                frame += 1
                frame_time = 0
        elif frame == 5:
            WIN.blit(CIN_BG, (0, 0))
            WIN.blit(CIN_STARS, (0, 0))
            cinematic_story_display("""But what's this? An attack by the Xeteros,
the abominable alien nation that seeks to destroy mankind,
and the attackers managed to capture David!""", WIN, 20, 20)
            for enemy in fake_enemies:
                enemy.move(-10)
                enemy.draw(WIN)
            pygame.display.update()
            frame_time += 1
            if frame_time > 2 * FPS:
                frame += 1
                frame_time = 0
        elif frame == 6:
            WIN.blit(CIN_BG, (0, 0))
            WIN.blit(CIN_STARS, (0, 0))
            cinematic_story_display("""But Starbreit will never give up.
He will do whatever it takes to rescue his love.
Even now you can hear his voice echo inside the
walls of his spaceship.
     """, WIN, 20, 20)
            WIN.blit(JONATHAN, (10 + JONATHAN.get_width(), HEIGHT - JONATHAN.get_height()))
            cinematic_story_display("""David, my love,
it's time to cross
the space between us""", WIN, JONATHAN.get_width(),
                                    (HEIGHT - JONATHAN.get_height()) - skip_font.get_height()*4, 'speech')
            fake_player.draw(WIN)
            fake_player.y -= 100
            pygame.display.update()
            frame_time += 1
            if frame_time > 2 * FPS:
                frame += 1
                frame_time = 0
        elif frame == 7:
            main()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                frame += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False





def pause():
    run = True
    while run:
        title_font = pygame.font.Font(os.path.join("assets", "pixel.ttf"), 30*DISPLAY_MODE)
        main_title_font = pygame.font.Font(os.path.join("assets", "pixel2.otf"), 45 * DISPLAY_MODE)
        main_title_label = main_title_font.render("Space Between Us", 1, (255, 255, 255))
        paused_label = title_font.render("PAUSED", 1, (255, 255, 255))
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press any key to continue", 1, (255, 255, 255))
        WIN.blit(main_title_label, (WIDTH // 2 - main_title_label.get_width() // 2, HEIGHT // 2))
        WIN.blit(title_label, (WIDTH // 2 - title_label.get_width() // 2, HEIGHT // 2+title_label.get_height()*2))
        WIN.blit(paused_label, (WIDTH // 2 - paused_label.get_width() // 2, HEIGHT // 2 - paused_label.get_height() * 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                run = False

    return None
main_menu()
