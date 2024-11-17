import pygame
from pygame import *

#Игра стоит, если не двигать мышкой и не нажимать кнопки, не нашел как это исправить

pygame.init()
win_width = 1024
win_height = 768
clock = pygame.time.Clock()
display.set_caption('Game')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('all_sprites/background.jpg'), (win_width, win_height))

#Звук выстрела
sound = pygame.mixer.Sound('all_sprites/shot.wav')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        #Движение с ограничением по границе окна
        keys = key.get_pressed()
        if  keys[K_LEFT]: #Почему просит ':' если объединяю условия через AND?
            if self.rect.x > 0:
                self.rect.x -= self.speed
        if keys[K_RIGHT]:
            if self.rect.x < win_width - 80:
                self.rect.x += self.speed

        #Движение вверх и вниз
        if keys[K_UP]:
            if self.rect.y > 160:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y < win_height - 80:
                self.rect.y += self.speed

    def fire(self):
        bullet = Bullet('all_sprites/bullet.png', self.rect.right - 20, self.rect.top, 15, 20, 15)
        #Второй бластер
        bullet2 = Bullet('all_sprites/bullet.png', self.rect.left, self.rect.top, 15, 20, 15)
        bullets.add(bullet, bullet2)

class Enemy(GameSprite):
    direction = 'right'

    def move(self):
        if self.rect.x < 0:
            self.direction = 'right'
        if self.rect.x > win_width - 80:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

ship = Player('all_sprites/ship.png', 472, 660, 80, 80, 10)
enemy = Enemy('all_sprites/ship-enemy.png', 472, 10, 80, 80, 3)
enemy2 = Enemy('all_sprites/ship-enemy.png', 472, 90, 80, 80, 3)
enemy3 = Enemy('all_sprites/ship-enemy.png', 472, 170, 80, 80, 3)
enemy4 = Enemy('all_sprites/ship-enemy.png', 472, 250, 80, 80, 3)
enemy5 = Enemy('all_sprites/ship-enemy.png', 472, 330, 80, 80, 3)
bullets = sprite.Group()
enemies = sprite.Group()

#Добавляем пять врагом
enemies.add(enemy, enemy2, enemy3, enemy4, enemy5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #Воспроизводим звук выстрела
                sound.play()
                ship.fire()
        window.blit(background, (0, 0))
        sprite.groupcollide(enemies, bullets, True, True)
        bullets.update()
        bullets.draw(window)
        ship.reset()
        ship.move()
        enemies.update()
        enemies.draw(window)
        enemy.move()
        enemy2.move()
        enemy3.move()
        enemy4.move()
        enemy5.move()
        pygame.display.update()
        pygame.time.delay(35)