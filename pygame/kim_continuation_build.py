import pygame
import random

#  Initialise pygame
pygame.init()

# Creating the Game window
gameWindow = pygame.display.set_mode((800, 600))

# Adding a Game Title
pygame.display.set_caption("Alien Shooter Game")
# Icon for the game
gameIcon = pygame.image.load('rocket.png')
pygame.display.set_icon(gameIcon)

# Defining Player Image and Starting Position of the player
playerIcon = pygame.image.load('space-invaders.png')
playerPosX = 360
playerPosY = 480
# Responsible for the change in direction when user presses left of right key
playerPosx_change = 0

# Defining Enemy Image and Starting Position of the Enemy
enemyIcon = pygame.image.load('rocket.png')
# Randomising our enemy start position to the set range
enemyPosX = random.randint(0, 800)
enemyPosY = random.randint(50, 150)
# Responsible for the change in direction of the enemy
enemyPosx_change = 0
enemyPosy_change = 0

# Player Character Function
# Arguments x_axis and y_axis to take user input for moving the player accordingly
def player_character(x_axis, y_axis):
    # the blit() method is used to draw the player's Image icon at the defined positions for x and y
    gameWindow.blit(playerIcon, (x_axis, y_axis))

# Enemy Character Function
def enemy_character(x_axis, y_axis):
    # the blit() method is used to draw the player's Image icon at the defined positions for x and y
    gameWindow.blit(enemyIcon, (x_axis, y_axis))


# Game Loop
# Makes sure the game window runs until the Quit button is pressed
gameRunning = True
while gameRunning is True:
    # Changing the game screen's background using RGB codes
    gameWindow.fill((0, 0, 255))

    # This for loop checks for the event that the quit button is pressed by the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

        # This Section Handles player movement input along the a axis.
        # If key is pressed check whether it is left or right KEYDOWN - Pressing a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosx_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerPosx_change = 0.3
        # Check if pressed key has been released KEYUP- Releasing the pressed key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerPosx_change = 0

    # This line updates the player's x-axis position according to the above keyboard press conditions
    playerPosX += playerPosx_change

    # This part is meant to create boundaries around the screen such that the player does not leave the game window
    if playerPosX <= 0:
        playerPosX = 0
    elif playerPosX >= 736:
        playerPosX = 736

    # Calling our Player to be displayed
    player_character(playerPosX, playerPosY)
    # Calling our Enemy to be displayed
    enemy_character(enemyPosX, enemyPosY)
    # constantly updating our game window
    pygame.display.update()
