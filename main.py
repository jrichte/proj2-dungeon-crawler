# Authors: Joshua R., Grant S.
# Last Updated: 11-11
# Description: Holds main function for EE 551 Project 2.

import pygame

# classes to handle player/inventory, map, minimap, enemies?

# file of functions for movement, tie together player (position in class) and map (coordinates in class)
# combat functions (use elements of enemy classes to determine required dodge?)

def main():
    # pygame setup (basic structural code borrowed from docs)
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    running = True

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        # draw squares of different colors in different locations to make ui elements

        pygame.draw.circle(screen, "black", player_pos, 40)

        BUTTON_SIZE = 48
        pygame.draw.rect(screen, "blue", pygame.Rect(400, 250, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.rect(screen, "blue", pygame.Rect(450, 250, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.rect(screen, "blue", pygame.Rect(500, 250, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.rect(screen, "blue", pygame.Rect(400, 300, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.rect(screen, "blue", pygame.Rect(450, 300, BUTTON_SIZE, BUTTON_SIZE))
        pygame.draw.rect(screen, "blue", pygame.Rect(500, 300, BUTTON_SIZE, BUTTON_SIZE))

        VIEWPORT_XSIZE = 280
        VIEWPORT_YSIZE = 240
        pygame.draw.rect(screen, "green", pygame.Rect(60, 60, VIEWPORT_XSIZE, VIEWPORT_YSIZE))

        MINIMAP_XSIZE = 160
        MINIMAP_YSIZE = 120
        pygame.draw.rect(screen, "red", pygame.Rect(395, 60, MINIMAP_XSIZE, MINIMAP_YSIZE))



        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
        main()