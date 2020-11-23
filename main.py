# Simple pygame program
from randomSentence import getRandomSentence, getRandomWord
# Import and initialize the pygame library
import pygame
pygame.init()

windowWidth = 1000
windowHeight = 400

# Set up the drawing window
screen = pygame.display.set_mode([windowWidth, windowHeight])

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 20)

stringToType = getRandomSentence()
text = font.render("Type the following: " + stringToType, True, green, blue) 
textRect = text.get_rect()  
textRect.center = (windowWidth // 2, windowHeight // 2) 
currentChar = 0

# Run until the user asks to quit
running = True
finished = False
while running:

    screen.fill((255, 255, 255)) # (255, 255, 255) RGB value for WHITEfd
    if (finished == False):
        screen.blit(text, textRect) 
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if (finished == False):
                mods = pygame.key.get_mods()
                if (event.unicode == stringToType[currentChar]):
                    print("yes")
                    currentChar += 1
                    if (currentChar == len(stringToType)):
                        #finished = True
                        print("done")
                        stringToType = getRandomSentence()
                        text = font.render("Type the following: " + stringToType, True, green, blue) 
                        textRect = text.get_rect()  
                        textRect.center = (windowWidth // 2, windowHeight // 2) 
                        currentChar = 0
                else:
                    print("no")

    # Fill the background with white
    #screen.fill((255, 255, 255))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()