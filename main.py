# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 32)
stringToType = 'test'
text = font.render("Type the following: " + stringToType, True, green, blue) 
textRect = text.get_rect()  
textRect.center = (500 // 2, 500 // 2) 
currentChar = 0

# Run until the user asks to quit
running = True
finished = False
while running:

    
    if (finished == False):
        screen.blit(text, textRect) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                running = False
            if (pygame.key.name(event.key) == stringToType[currentChar]):
                print("yes")
                currentChar += 1
                if (currentChar == len(stringToType)):
                    finished = True
            else:
                print(currentChar)
            

    # Fill the background with white
    #screen.fill((255, 255, 255))



    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()