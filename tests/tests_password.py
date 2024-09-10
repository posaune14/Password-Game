from game.main import Passwords
from game.main import Game
import pytest

def test_check_password():
    password = Passwords()
    assert password.check_password("password") == True
    assert password.check_password("123") == False
    
def test_import_random_pattern():
    password = Passwords()
    assert password.import_random_pattern() != None 
    assert password.pattern != "[a-z]"
    
def test_generate_password():
    game = Game()
    password = Passwords()
    pattern = password.pattern
    game.generate_password()
    assert password.pattern == pattern
    
'''def test_ask_password(monkeypatch):
    game = Game() 
    #setattr replaces an object (in this case input) with the value 123
    monkeypatch.setattr('builtins.input', lambda _: '123')
    assert game.ask_password() != None'''

'''def test_start_game(monkeypatch):
    game = Game()
    game.mode = 'testing'
    monkeypatch.setattr('builtins.input', lambda _: 'a')
    password = Passwords()
    password.pattern = "[a-zA-Z]"
    #change pattern to a specified pattern so the monkeypatch input works
    game.start_game()
    assert len(game.completed_patterns)>0
    assert game.password.pattern != '[a-zA-Z]'
    assert game.print_password() == game.password.pattern
    #after a sucess, check if the pattern is in the list
    
#def test_print_password():
    password = Passwords()
    game = Game()
    game.mode = 'testing'
    password.pattern 
    game.start_game()'''

#pytest tests/tests_password.py --import-mode=append 
#run statement