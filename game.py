import pygame, sys
from FacillimumLibrary import Facillimum_Library
import random
from settings import Settings
from marioAnimation import Mario
from coins import Coins
class Main:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Math Game")
        self.FL = Facillimum_Library(self.screen)
        self.settings = Settings()
        self.mario = Mario(self)
        self.coins = Coins(self)
        self.solved = True
        self.background = pygame.image.load('images/mario background image.png')
        self.background = pygame.transform.scale(self.background, (800, 700))
        self.text_box = True
        self.reset = False
        self.get_new_equation = True
        self.game_lost = False
        self.game_won  = False
        
    def play_solved(self):
        pygame.mixer.music.load('sound/11. Coin.mp3')
        pygame.mixer.music.play()

    def play_lose(self):
        pygame.mixer.music.load('sound/17. Lost A Life.mp3')
        pygame.mixer.music.play()

    
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.FL.draw_image(self.background, (0, 100))
       
    def get_equation(self):
        if self.get_new_equation == True:
            self.first_number = random.randint(0, 10)
            self.second_number = random.randint(0, 10)
            self.answer = self.second_number + self.first_number

    def display_equation(self):
        self.FL.draw_words((str(self.first_number) + " + " + str(self.second_number) + " ="), 200, (20, 409), False, "black")

    def keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.reset = True

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
           
    def run_program(self):
        while True:
            # set beginning variables
            self.get_equation()
            
           # check events
            self.check_events()

            # draws the screen
            if self.game_lost == False and self.game_won == False:
                self.update_screen()
                self.mario.blitme()
                self.display_equation()
                self.coins.draw_coins()
                self.coins.blitme()

            # waits for the answer of the equation
            if self.FL.open_text_box(70, (0, 730), (204, 68, 29)) == str(self.answer) and self.text_box == True:
                # equation solved
                self.play_solved()
                self.settings.wins += 1
                self.get_new_equation = True
                self.coins.revealer_rect.x += 75
                self.settings.chances = 5
            else:
                # equation not solved
                if self.game_won == False and self.game_lost == False:
                    self.play_lose()
                    self.settings.chances -= 1
                    self.get_new_equation = False
                

            # game over
            if self.settings.chances < 1:
                self.game_lost = True
                self.text_box = False
                self.FL.draw_words("GAME OVER", 180, (10, 90), False, "red")
                self.FL.draw_words("Press space to play again", 60, (0, 600), False, "black")
                self.FL.text_box = False
                

                # resets the game
                if self.game_lost == True:
                    self.coins.reset_x()
                    self.check_events()
                    if self.reset == True:
                        self.get_new_equation = True
                        self.settings.chances = 5
                        self.text_box = True
                        self.FL.text_box = True
                        self.game_lost = False
                        self.reset = False
                        pygame.mixer.music.stop()

            # game won
            if self.coins.revealer_rect.x > 750:
                self.game_won = True
                self.text_box = False
                self.FL.draw_words("VICTORY!!", 180, (60, 90), False, "green")
                self.FL.draw_words("Press space to play again", 60, (0, 600), False, "black")
                self.FL.text_box = False

                #resets the game
                if self.game_won == True:
                    self.check_events()
                    if self.reset == True:
                        self.get_new_equation = True
                        self.settings.chances = 5
                        self.text_box = True
                        self.FL.text_box = True
                        self.game_won = False
                        self.reset = False
                        self.coins.reset_x()
                        pygame.mixer.music.stop()

            # the same as pygame.display.flip()
            self.FL.update()

            
                
if __name__ == "__main__":
    game = Main()
    game.run_program()
     