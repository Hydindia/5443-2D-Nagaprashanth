# Import necessary modules
import pygame
import sys
import os
import random

# Change the current working directory to 'resource'
os.chdir("Assets")

# Initialize pygame modules for font and mixer
pygame.font.init()
pygame.mixer.init()

# Define the main game class
class univshipGame:
    # Set the game window dimensions
    width = 1200
    height = 700

    randNumbackground = str(random.randint(0,5))
    randNumShip = str(random.randint(0,1))

    # Define the game's center line
    lines_gam = pygame.Rect(width//2 - (3+1), 0, 10, height)

    # Load spaceship images
    red_color = pygame.image.load("univshipred" + randNumShip + ".png")
    yellow_color = pygame.image.load("univshipyellow" + randNumShip+  ".png")

    # Load and scale the background image
    univ = pygame.transform.scale(pygame.image.load('background'+randNumbackground+'.png'), (width, height))

    # Set the spaceship dimensions
    univSHIP_width, univSHIP_height = 55, 40

    # Define game parameters
    persecspeed = 60
    new_velocity = 7+2
    firings_new_velocity = 6
    MAX_firingsS = 2
    DEFLECT = 0
    DEFLECT2 = 0

    # Set the font for points and game messages
    points_font = pygame.font.SysFont('comicsans', 45+3)
    good_font = pygame.font.SysFont("comicsans", 93+5)

    # Load sound effects for firing and hitting
    firings_HIT_SOUND = pygame.mixer.Sound("GunHit.wav")
    firings_FIRE_SOUND = pygame.mixer.Sound("GunFire.mp3")

    # Define custom events for yellow and red spaceship firing
    yel_fire = pygame.USEREVENT + 1
    red_fire = pygame.USEREVENT + 2

    # Load and transform the spaceship images for yellow spaceship
    yellow_color_IMAGE = pygame.image.load(os.path.join("univshipyellow" + randNumShip+  ".png"))
    yellow_color = pygame.transform.rotate(pygame.transform.scale(
        yellow_color_IMAGE, (univSHIP_width, univSHIP_height)), 95)

    # Load and transform the spaceship images for red spaceship
    red_color_IMAGE = pygame.image.load(os.path.join("univshipred" + randNumShip + ".png"))
    red_color = pygame.transform.rotate(pygame.transform.scale(
        red_color_IMAGE, (univSHIP_width, univSHIP_height)), 300)
    


    # Load and scale the background image
    univ = pygame.transform.scale(pygame.image.load(os.path.join('background'+randNumbackground+'.png')), (width, height))


        # Initialization function for the game class
    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules
        self.win = pygame.display.set_mode((self.width, self.height))  # Create a game window
        pygame.display.set_caption("univship Battle")  # Set the caption for the game window

    # Function to design the game space
    def designing_space(self, red, yellow, red_firingss, yellow_firingss, red_health, yellow_health):
        self.win.blit(self.univ, (0, 0))  # Draw the background onto the game window
        pygame.draw.rect(self.win, (0, 0, 0), self.lines_gam)  # Draw the center line onto the game window
        # Create health text for both spaceships and draw them onto the game window
        red_health_text = self.points_font.render("Health: " + str(red_health), 1, (212, 212, 212))
        yellow_health_text = self.points_font.render("Health: " + str(yellow_health), 1, (212, 212, 212))
        self.win.blit(red_health_text, (self.width - red_health_text.get_width() - 10, 10))
        self.win.blit(yellow_health_text, (10, 10))
        # Draw the spaceships onto the game window
        self.win.blit(self.yellow_color, (yellow.x, yellow.y))
        self.win.blit(self.red_color, (red.x, red.y))
        # Draw the bullets of both spaceships onto the game window
        for firings in red_firingss:
            pygame.draw.rect(self.win, (212, 0, 0), firings)
        for firings in yellow_firingss:
            pygame.draw.rect(self.win, (212, 212, 0), firings)
        pygame.display.update()  # Update portions of the screen for software displays

    # Function to manage the movements and actions of the yellow spaceship
    def manage_yellow(self, keys_pressed, yellow):
        global DEFLECT2
        # Move the spaceship to the left if 'a' is pressed and it's not at the left boundary
        if keys_pressed[pygame.K_a] and yellow.x - self.new_velocity > 0: # LEFT
            yellow.x -= self.new_velocity
        # Move the spaceship to the right if 'd' is pressed and it's not at the center line
        if keys_pressed[pygame.K_d] and yellow.x + self.new_velocity + yellow.width < self.lines_gam.x: # RIGHT
            yellow.x += self.new_velocity
        # Move the spaceship up if 'w' is pressed and it's not at the top boundary
        if keys_pressed[pygame.K_w] and yellow.y - self.new_velocity > 0: # UP
            yellow.y -= self.new_velocity
        # Move the spaceship down if 's' is pressed and it's not at the bottom boundary
        if keys_pressed[pygame.K_s] and yellow.y + self.new_velocity + yellow.width < self.height - 15: # DOWN
            yellow.y += self.new_velocity
        # Projectile bullets at decline angle if 'x' is pressed
        if keys_pressed[pygame.K_x]: 
            self.DEFLECT+=0.35
        # Projectile bullets at incline angle if 'z' is pressed
        if keys_pressed[pygame.K_z]:  
            self.DEFLECT-=0.35 
  

    # Function to manage the movements and actions of the red spaceship
    def manage_red(self, keys_pressed, red):
        global DEFLECT
        # Move the spaceship to the left if 'LEFT' arrow key is pressed and it's not at the center line
        if keys_pressed[pygame.K_LEFT] and red.x - self.new_velocity > self.lines_gam.x + self.lines_gam.width: # LEFT
            red.x -= self.new_velocity
        # Move the spaceship to the right if 'RIGHT' arrow key is pressed and it's not at the right boundary
        if keys_pressed[pygame.K_RIGHT] and red.x + self.new_velocity + red.width < self.width: # RIGHT
            red.x += self.new_velocity
        # Move the spaceship up if 'UP' arrow key is pressed and it's not at the top boundary
        if keys_pressed[pygame.K_UP] and red.y - self.new_velocity > 0: # UP
            red.x -= self.new_velocity
        # Move the spaceship down if 'DOWN' arrow key is pressed and it's not at the bottom boundary
        if keys_pressed[pygame.K_DOWN] and red.y + self.new_velocity + red.height < self.height - 15:  # DOWN
            red.y += self.new_velocity
        # Projectile bullets at decline angle if 'RSHIFT' is pressed
        if keys_pressed[pygame.K_RSHIFT]:
            self.DEFLECT2+=0.35  
        # Projectile bullets at incline angle if 'SPACE' is pressed
        if keys_pressed[pygame.K_SPACE]:
            self.DEFLECT2-=0.35

    # Function to manage the movements of bullets
    def handle_firingss(self, yellow_firingss, red_firingss, yellow, red):
        # For each bullet of yellow spaceship
        for firings in yellow_firingss:
            # Move the bullet
            firings.x += self.firings_new_velocity
            firings.y += self.DEFLECT
            # If the bullet hits the red spaceship, fire an event and remove the bullet
            if red.colliderect(firings):
                pygame.event.post(pygame.event.Event(self.red_fire))
                yellow_firingss.remove(firings)
            # If the bullet goes out of the game window, remove the bullet
            elif firings.x > self.width:
                yellow_firingss.remove(firings)
        # Do similar thing for each bullet of red spaceship
        for firings in red_firingss:
            firings.x -= self.firings_new_velocity
            firings.y += self.DEFLECT2
            if yellow.colliderect(firings):
                pygame.event.post(pygame.event.Event(self.yel_fire))
                red_firingss.remove(firings)
            elif firings.x < 0:
                red_firingss.remove(firings)

    # Function to display a message in the game window
    def known(self,text):
        draw_text = self.good_font.render(text, 1, self.WHITE)  # Render the text
        self.WIN.blit(draw_text, (self.width/2 - draw_text.get_width() /
                 2, self.height/2 - draw_text.get_height()/2))  # Draw the text onto the game window
        pygame.display.update()  # Update the game window
        pygame.time.delay(5000)  # Delay for 5 seconds

     
    # Function to start the game
    def ready_game(self):
        # Initialize the game objects
        self.red = pygame.Rect(700, 300,  self.univSHIP_width, self.univSHIP_height)  # Define the red spaceship
        self.yellow = pygame.Rect(100, 300, self.univSHIP_width, self.univSHIP_height)  # Define the yellow spaceship

        self.red_firingss = []  # Initialize the list of red's bullets
        self.yellow_firingss = []  # Initialize the list of yellow's bullets
        self.red_health = 10  # Initialize the health of red spaceship
        self.yellow_health = 10  # Initialize the health of yellow spaceship

        clock = pygame.time.Clock()  # Initialize the game clock
        run = True  # Flag to control the game loop
        while run:  # Start the game loop
            clock.tick(self.persecspeed)  # Cap the framerate
            for event in pygame.event.get():  # Handle the game events
                if event.type == pygame.QUIT:  # If QUIT event, exit the game loop
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:  # If a key is pressed
                    # If 'LCTRL' is pressed and the number of yellow's bullets is less than the maximum allowed, create a new bullet
                    if event.key == pygame.K_LCTRL and len(self.yellow_firingss) < self.MAX_firingsS:
                        firings = pygame.Rect(
                            self.yellow.x +  self.yellow.width,  self.yellow.y +  self.yellow.height//2 - 2, 10, 5)
                        self.yellow_firingss.append(firings)
                        self.firings_FIRE_SOUND.play()

                    # Do the similar thing for the red spaceship
                    if event.key == pygame.K_RCTRL and len(self.red_firingss) < self.MAX_firingsS:
                        firings = pygame.Rect(
                            self.red.x, self.red.y + self.red.height//2 - (3+1), 10, 5)
                        self.red_firingss.append(firings)
                        self.firings_FIRE_SOUND.play()

                # If red spaceship is hit, reduce its health and play the hit sound
                if event.type == self.red_fire:
                    self.red_health -= 1
                    self.firings_HIT_SOUND.play()

                # Do the similar thing for the yellow spaceship
                if event.type == self.yel_fire:
                    self.yellow_health -= 1
                    self.firings_HIT_SOUND.play()

            # Check if there is a winner
            winner_text = ""
            if self.red_health <= 0:
                winner_text = "Yellow Wins!"

            if self.yellow_health <= 0:
                winner_text = "Red Wins!"
            
            # If there is a winner, display the winner text and break the game loop
            if winner_text != "":
                self.known(winner_text)
                break

            # Get the keys currently pressed
            keys_pressed = pygame.key.get_pressed()
            # Manage the movements and actions of the spaceships
            self.manage_yellow(keys_pressed, self.yellow)
            self.manage_red(keys_pressed, self.red)

            # Manage the movements of bullets
            self.handle_firingss(self.yellow_firingss, self.red_firingss, self.yellow, self.red)

            # Draw the spaceships, bullets, and health onto the game window
            self.designing_space(self.red, self.yellow, self.red_firingss, self.yellow_firingss,
                        self.red_health, self.yellow_health)

        pygame.quit()
        
if __name__=="__main__":
    game = univshipGame()
    game.ready_game()

