'''
    __name__ = 'die10k.players.py'
    __author__ = 'kyle roux'
    __author_email__ = 'jstacoder@gmail.com'
    __package__ = 'die10k'
    __description__ = 'Player class definition'
    __date__ = '05-25-2013, Sat, 2:06 AM'
'''
from dice import Roll, Die
from abc import abstractmethod

class Player(object):
    ''' a Player keeps track of individual player stats,
        such as (but not limited to) 

        scores
        rolls(for dice) or hands(for cards)
        name (the most important)
        id numbers (self or computer assigned)
        play status(am i playing?)
    '''
    _playerCount = 0 # keeps running count of players in game

    def __init__(self, name=None, score=0):
        Player._playerCount += 1
        self.id = Player._playerCount
        if name is None:
            self.name = 'Player{}'.format(self.id)
        else:
            self.name = name
        self.score = score
        self.isPlaying = False

    def __str__(self):
        return '{0} : player {1} <score:{2}>'.format(self.name,self.id,self.score)
        
    def __repr__(self):
        return self.name

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score
        return 0

    def get_name(self):
        return self.name

    def __add__(self, other):
        self.add_score(other)
    
    @abstractmethod
    def start_playing(self):
        pass

class DicePlayer(Player):
    ''' like a player but with dice specific stats for dice games'''
    def __init__(self, name, score):
        super(DicePlayer, self).__init__(name, score)
        self.diceRolling = 6
        self.diceHeld = 0
        self.isRolling = False
        self.heldDice = False

    def check_if_held_Dice(self):
        return self.heldDice

    def set_rolling(self):
        '''turn rolling on or off (either or)'''
        if self.isRolling:
            self.isRolling = False
        else:
            self.isRolling = True

    def check_if_rolling(self):
        return self.isRolling

    def roll(self, numberOfDies=6):
        if not self.diceRolling:
            rollNum = numberOfDies
        else:
            rollNum = self.diceRolling
        aRoll = ''
        for die in range(rollNum):
            aRoll = str(Die()) + ' ' + aRoll
        self.currentRoll = aRoll[:]

    def start_playing(self):    
        '''
        setup dice game related variables
        '''
        self.roundScore = 0
        self.rollScore = 0
        self.diceRolling = 6
        self.diceHeld = 0
        self.currentRoll = ''

    def update_roll_num(self):
        if self.diceRolling == 0:
            self.diceRolling = 6
        else:
            self.diceRolling = self.diceRolling - self.diceHeld

    def roll_again(self):
        self.roll(self.diceRolling)
