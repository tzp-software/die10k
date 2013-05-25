'''
    dieGame.py
'''
from players import DicePlayer as Player

def ask_str(STR=None):
    if STR is None:
        q = 'what is your favorite color?'
    else:
        q = STR
    return raw_input(q)

def get_players():
    '''returns tuple of Player objects'''
    players = []
    add = True
    PNAME = 'Please enter a name for a new player: '
    ADD_PLAYER = 'Would you like to add another player?\n(yes or no):'
    while add:
        name = ask_str(PNAME)
        tmp = Player(name, 0)
        players.append(tmp)
        if not ask_bool(ADD_PLAYER):
            add = False
    return players


def play_game(players):
    start_roll(players[0])
    if not ask_bool(PICKUP):
        change_player()
        
    else:
        if pickedUpNum == 6:
            roll_again() # set pickedUpNum to 0
        else:
            update_roll_num()
            if not ask_bool(ROLL_AGAIN):
                change_player()
            else:
                roll_again()

def ask_bool(question=None):
    if question is None:
        msg = 'Would you like to continue?\n(yes / no): '
    else:
        msg = question
    print msg,
    return raw_input().lower().startswith('y')

def change_player():
    global players
    global playa
    players[playa].stop_playing()
    if playa == len(players):
        playa = 0
    else:
        playa += 1

def start_roll(player):
    player.start_playing()
    player.roll()

def update_roll_num(player):
    player.update_roll_num()


def roll_again(player):
    player.roll_again()

if __name__ == "__main__":
    play_game(get_players())
