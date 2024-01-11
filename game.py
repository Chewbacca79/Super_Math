import pygame, sys
from FacillimumLibrary import Facillimum_Library
import random
from settings import Settings
from marioAnimation import Mario
from coins import Coins
from button import Button

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
        self.button = Button(self)
        self.solved = True
        self.playing = False
        self.solvable = True
        self.game_won = False
        self.game_lost = False
        self.background = pygame.image.load('images/mario background image.png')
        self.background = pygame.transform.scale(self.background, (800, 700))
        self.game_on = True
        self.game_reset = False
        
    def play_solved(self):
        pygame.mixer.music.load('sound/11. Coin.mp3')
        pygame.mixer.music.play()

    def play_lose(self):
        pygame.mixer.music.load('sound/17. Lost A Life.mp3')
        pygame.mixer.music.play()

    def play_game_over(self):
        pygame.mixer.music.load('sound/18. Game Over.mp3')
        pygame.mixer.music.play()

    def play_win(self):
        pygame.mixer.music.load('sound/SE Game SEction Clear Fanfare.mp3')
        pygame.mixer.music.play()
   
    def update_screen(self):
        if self.game_won == False:
            self.screen.fill(self.settings.bg_color)
            self.FL.draw_image(self.background, (0, 100))
       
    def get_equation(self):
        self.first_number = random.randint(0, 10)
        self.second_number = random.randint(0, 10)
        self.answer = self.second_number + self.first_number

    def display_equation(self):
        self.FL.draw_words((str(self.first_number) + " + " + str(self.second_number) + " ="), 200, (20, 409), False, "black")

    def keydown_events(self, event):
        if event.key == pygame.K_SPACE:
            self.playing = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            

    def run_program(self):
        while self.game_on:
                self.update_screen()
                if self.game_won == False:
                    self.FL.draw_words("Press space to start", 80, (125, 400), False, "black")
               
                if self.playing == True and self.solved == True and self.game_won == False and self.game_lost == False:
                    
                    self.update_screen()
                    self.solved = False
                    self.get_equation()
                    self.display_equation()
                    self.coins.draw_coins()
                    self.mario.blitme()
                    self.coins.blitme()
                    if self.FL.open_text_box(60, (0, 740), (204, 68, 29)) == str(self.answer) and self.solvable == True:
                        self.solved = True
                        self.play_solved()
                        self.settings.chances = 5
                        self.coins.move_right = True
                        self.coins.reveal_coins()
                        self.settings.wins += 1
                        if self.settings.wins == 11:
                            self.FL.draw_words("VICTORY!!", 200, (40, 60), True, "green")
                            self.play_win()
                            self.game_won = True
                            self.solvable = False 
                    else:
                        self.settings.chances = self.settings.chances - 1
                        self.play_lose()
                        while self.solved == False:
                            if self.FL.open_text_box(60, (0, 740), (204, 68, 29)) == str(self.answer) and self.solvable == True:
                                self.solved = True
                                self.play_solved()
                                self.settings.chances = 5
                                self.coins.move_right = True
                                self.coins.reveal_coins()
                                self.settings.wins += 1
                                if self.settings.wins == 11:
                                    self.FL.draw_words("VICTORY!!", 200, (40, 60), True, "green")
                                    self.play_win()
                                    self.game_won = True
                                    self.solvable = False
                            else:
                                self.settings.chances = self.settings.chances - 1
                                self.play_lose()
                                if self.settings.chances < 1:
                                    self.FL.draw_words("GAME OVER", 180, (10, 60), True, "red")
                                    self.play_game_over()
                                    self.game_lost = True
                                    self.solvable = False
                                    
                self.FL.update()
                self.check_events()
                

if __name__ == "__main__":
    game = Main()
    game.run_program()
     