import re
import random
import time
import string
import sys
import json

from termcolor import cprint, colored

#game: user has to create a password which follows certain parameters, after each password is created parameters become more restrictive
#using regular expressions to create parameters for password

#start: 
#computer prints the regex expression to the console
#computer asks for a password
#user inputs a password
#computer checks if password follows pattern. if it does, state sucess and ask for new password with different pattern. if not, state wrong and ask for new password with the same pattern
#user input password
#computer continues to restrict answers and user inputs new passwords

class Game:
    #create a test configuration for game
    def __init__(self) -> None:
        self.username = None
        self.mode = 'production'
        self.completed_patterns = []
        #completed_patterns has to be initialized before generate_password because generate password uses it
        self.generate_password()
        #self.password.pattern = Passwords().import_random_pattern()
    #game class should have a list of completed patterns to know when to end 
    def load_progress(self):
        question = colored('Enter username to load progress, otherwise, click enter: ', 'dark_grey')
        username = input(question).strip()
        if bool(username) == True:
            #end removes whitespace after ., and flush parameter makes all print statements with end parameter run instantenously using sys library
            cprint('Loading progress', 'dark_grey', end='', flush=True)
            for i in range(5):
                time.sleep(1)
                cprint('.', 'dark_grey', end='', flush=True)
            print('')
            with open('game/saves.txt', 'r') as file:
                line = file.readline()
                while line:
                    if line.startswith(username):
                        line = line.split('::')
                        self.username = line[0]
                        completed_patterns = line[1].replace("\\\\", "\\").strip()
                        self.completed_patterns = completed_patterns[1:-1].split(', ')
                        #removes first and last character from string
                        #split creates list
                        cprint('Username: '+ username, 'cyan')
                        cprint('Completed Patterns: '+str(completed_patterns), 'green')
                        for i in range(len(self.completed_patterns)):
                            self.completed_patterns[i] = self.completed_patterns[i].strip("'")
                        break
                    line = file.readline()
    def tutorial(self):
        if len(self.completed_patterns)>0:
            self.start_game()
        else:
            #loading tutorial text 
            cprint('Loading tutorial', 'dark_grey', end='', flush=True)
            for i in range(3):
                time.sleep(1)
                cprint('.', 'dark_grey', end='', flush=True)
            print('')
            cprint('Hello. Welcome to the tutorial for the password game. Your goal is to write passwords which satisfy the regex patterns.', 'white', 'on_light_yellow')
            self.password.pattern = '[a-z]'
            while True:
                cprint("Pattern: ", 'magenta')
                cprint(self.password.pattern, 'yellow')
                question = colored('Input Password: ', 'cyan')
                password = input(question).strip()  
                if re.match(self.password.pattern, password):
                    cprint("Correct", 'green')
                    break
                else:
                    cprint("Type anything using only letters. For example: 'apple' ")
            while True:
                print('')
                cprint('Write skip to receive a new pattern. Type Skip:', 'dark_grey')
                cprint("Pattern: ", 'magenta')
                cprint(self.password.pattern, 'yellow')
                password = input(question).strip()
                if password == 'Skip' or password == 'skip':
                    cprint('Good job, that is how you skip patterns.', 'green')
                    break
                else:
                    cprint('Try typing skip or Skip', 'dark_grey')
            self.password.pattern = '[0-9]'
            while True:
                print('')
                cprint('Write quit to exit the game. Type Quit:', 'dark_grey')
                cprint("Pattern: ", 'magenta')
                cprint(self.password.pattern, 'yellow')
                password = input(question).strip()
                if password == 'Quit' or password == 'quit':
                    cprint('Good job, that is how you quit the game.', 'green')
                    break
                else:
                    cprint('Try typing quit or Quit', 'dark_grey')
            print('')
            ready = colored('Are you ready to start the game?', 'white', 'on_light_yellow')
            yes = colored(' Yes ' , 'green')
            no = colored('  No  ', 'red')
            answer = input(ready+yes+no)
            print(' ')
            if answer == 'Yes' or answer == 'Y' or answer == 'yes' or answer == 'y':
                cprint('Loading game', 'dark_grey', end='', flush=True)
                for i in range(4):
                    time.sleep(1)
                    cprint('.', 'dark_grey', end='', flush=True)
                print('')
                self.start_game()
            else:
                sys.exit('Come back when you are ready.')
    def print_password(self):
        if self.mode == 'testing':
            return self.password.pattern
        else:
            cprint("Pattern: ", 'magenta')
            cprint(self.password.pattern, 'yellow')
    def quit(self):
        print(self.completed_patterns)
        save = input("Would you like to save/overwrite progress? Type yes or y: ")
        if save == 'Yes' or save == 'yes' or save == 'y' or save == 'Y':
            if bool(self.username) is not True:
                username = input('Enter a username: ')
                #write new username to file
                self.username=username
                with open('game/saves.txt', 'w') as file:
                    file.write(self.username+'::'+str(self.completed_patterns) + '\n')
            else:
                with open('game/saves.txt', 'r') as file:
                    lines = file.readlines()
                for i in range(len(lines)):
                    if lines[i].strip().split('::')[0] == self.username:
                        lines[i] = self.username+'::'+str(self.completed_patterns) + '\n'
                        break
                with open('game/saves.txt', 'w') as file:
                    file.writelines(lines)
        sys.exit('Thank you for playing.')
    def start_game(self):
        self.generate_password()
        #test while loop
        while len(self.completed_patterns)<10:
            self.print_password()
            guess=self.ask_password().strip()
            if guess == 'skip' or guess == 'Skip':
                self.generate_password()
                print('')
            elif guess == 'quit' or guess == 'Quit':
                self.quit()
            else:
                correct=self.password.check_password(guess)
                if correct:
                    cprint("Correct", 'green')
                    self.completed_patterns.append(self.password.pattern)
                    x=len(self.completed_patterns)
                    cprint("You have completed "+str(x)+" passwords.", 'dark_grey')
                    print('')
                    #if password correct, generate new password object with different pattern
                    if x != 10:
                        self.generate_password()
                    #test append function works 
                    if self.mode == 'testing':
                        self.generate_password()
                        break
                else:
                    #else go back to start of the loop
                    cprint("Incorrect", 'red')
                    print('')
        cprint("Game Completed.", 'green')
    def generate_password(self):
        self.password = Passwords()
        self.password.pattern = self.password.import_random_pattern()
        while self.password.pattern in self.completed_patterns:
            self.password.import_random_pattern()
    def ask_password(self):
        question = colored('Input Password: ', 'cyan')
        password = input(question)           
        return password
#create a class for passwords
#create a game class
class Passwords:
    def __init__(self) -> None: # -> None means the class will not return anything
        self.pattern = '[a-z]'
    def check_password(self, password):
        #print('checking password...')
        #print(self.pattern)
        #print(password)
        if re.match(self.pattern, password):
            return True
        else:
            return False
    def import_random_pattern(self):
        with open('game/regex_patterns.txt', 'r') as file:
            lines = file.readlines()
            self.pattern = str(random.choice(lines).strip())
            return self.pattern      

password = Passwords()
game = Game()
game.load_progress()
game.tutorial()
        
# Game class
# Starts the game
# Grabs a regex password auto and saves it into vaiable self.pattern
# Asks the user to type the password until they run out of lives
# Everytime the user asks if the returned value of check password is true generate a new regex pattern