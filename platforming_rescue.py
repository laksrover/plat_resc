import pgzrun

import random

WIDTH = 600 # Ширина окна
HEIGHT = 300 # Высота окна

TITLE = "platforming rescue" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

#actors and variables
char = Actor('pythonfinprojchar', size = (40, 40))
char.bottomleft = (0, HEIGHT)
char.speed_x = 0
char.speed_y = 0.0
blockjump = False
canDjump = True
score = 2
miniscore = 0
flag = 1
rngchecker = 0
rngchecker_ = 0
jumpchecker = 0
coinchecker = 0
speed = 1
speed_display = "easy"
end = False
objects = []
for i in range(12):
    if i < 6:
        gX = 575
        gY = (i+1)*50-25
    else:
        gX = 257
        gY = (i-5)*50-25
       
    Gpicture = random.randint(1,10)
    if Gpicture > 4:
        GpictureNEW = "blockpythonfinproj"
    elif Gpicture < 4:
        GpictureNEW = "blankpythonfinproj"
    elif Gpicture == 4:
        GpictureNEW = "coinpythonfinalproj"
       
    o = Actor(GpictureNEW, (gX, gY), size = (50, 50))
    objects.append(o)
   
def draw():
    screen.fill("white")
    for i in range(len(objects)):
         objects[i].draw()
    char.draw()
    screen.draw.text(str(score), center = (50, 20), color = "black", fontsize = 25)
    if score == 100:
         screen.draw.text("you win!", center = (300, 150), color = "black", fontsize = 50)
   
def update(dt):
    global canDjump, flag, blockjump, score, miniscore, rngchecker, rngchecker_, jumpchecker, coinchecker
    miniscore += 2
    if miniscore == 80:
        score += 1
        miniscore = 0
    
    
    for i in range(12):
        if i < 6:
            if objects[i].image == "blockpythonfinproj":
                rngchecker += 1
            if rngchecker == 6:
                objects[2].image = "blankpythonfinproj"
        else:
            if objects[i].image == "blockpythonfinproj":
                rngchecker_ += 1
            if rngchecker_ == 6:
                objects[8].image = "blankpythonfinproj"
    rngchecker = 0
    rngchecker_ = 0
    # Движение по горизонтали
    char.speed_x = 0
    if keyboard.left:
        char.speed_x = -7
    elif keyboard.right and char.x < 580:
        char.speed_x = 7

    char.x += char.speed_x
    if char.y < 20:
        char.speed_y = 0
    # Проверяем каждый объект
    for obj in objects:
        if char.colliderect(obj) and obj.image == 'blockpythonfinproj':
            # Если направо
            if char.speed_x > 0:
                char.right = obj.left
                flag = 1
            # Если налево
            elif char.speed_x < 0:
                char.left = obj.right
                
            # Больше не двигаемся
            elif flag == 1:
                char.right = obj.left
            elif flag == 2:
                char.left = obj.right
            char.speed_x = 0
           
    # Движение по вертикали
    char.speed_y += 1.7 # ЗДЕСЬ ПОМЕНЯТЬ, ЧТОБЫ ПАДАТЬ БЫСТРЕЕ
    char.y += char.speed_y
   
    # Проверяем каждый объект
    for obj in objects:
        if char.colliderect(obj) and obj.image == 'blockpythonfinproj':
            # Если вниз
            if char.speed_y > 0:
                # Становимся на блок
                char.bottom = obj.top
                char.speed_y = 0
                canDjump = True
                blockjump = True
        
            # Если вверх
            elif char.speed_y < 0:
                char.top = obj.bottom
                char.speed_y = 0
                
        

    # Становимся на землю
    if char.bottom >= HEIGHT:
        char.bottom = HEIGHT
        char.speed_y = 0
        canDjump = True
        blockjump = False
        if jumpchecker == 0:
            score-=2
            jumpchecker = 1
       
    for i in range(len(objects)):
         objects[i].x -= 4
         if objects[i].x < -25:
            objects[i].x = 575
            Gpicture = random.randint(1,10)
            if Gpicture > 4:
                 objects[i].image = "blockpythonfinproj"
            elif Gpicture < 4:
                 objects[i].image = "blankpythonfinproj"
            elif Gpicture == 4:
                 objects[i].image = "coinpythonfinalproj"
    for obj in objects:
        if char.colliderect(obj):
             if obj.image == "coinpythonfinalproj" and coinchecker == 0:
                 score +=2
                 coinchecker = 1
                 obj.image ="blankpythonfinproj"
             elif obj.image == "coinpythonfinalproj":
                 coinchecker = 0
    if char.x < -20:
        score = 0
        char.x =60
        char.y =260
    
def on_key_down(key):
    global canDjump, blockjump, jumpchecker
    # Прыжок
    
    if key == keys.SPACE:
        if char.bottom >= HEIGHT or canDjump == True or blockjump == True:
            # Начинаем прыгать
            char.speed_y = -20 # ЗДЕСЬ ПОМЕНЯТЬ, ЧТОБЫ ПРЫГАТЬ ВЫШЕ
            jumpchecker = 0
           
            if char.bottom < HEIGHT:
               if blockjump == True:
                   blockjump = False
               else:
                   canDjump = False
pgzrun.go()