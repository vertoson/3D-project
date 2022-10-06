import math as m

# game settings

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

## player settings

PLAYER_POS = 2, 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004 
PLAYER_ROT_SPEED = 0.002

## RAYCASTING settings

FOV = m.pi / 3 # 60 degress fov
HALF_FOV = FOV / 2 # because ray is split into two sections as the middle split will be equal to half, to find the start of the ray simply get the player angle - the half of the FOV will make sure the ray starts at the start
NUM_RAYS = WIDTH // 2 
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS # angle between all the rays
MAX_DEPTH = 20

## 3D DISPLAY

SCREEN_DIST = HALF_WIDTH / m.tan(HALF_FOV) # found by using trigonometry by halving the triangle of distance to make a right angled triangle then do the math
SCALE = WIDTH // NUM_RAYS