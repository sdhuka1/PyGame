class GameStats:
    #This tracks statistics for Alien Invasion

    def __init__(self, ai_game):
        #This initializes statistics
        self.settings = ai_game.settings
        self.reset_stats()

        #This starts Alien Invasion in an active state
        #self.game_activate = True

        #This starts the game in an inactive state
        self.game_activate = False

        #The high score should never be reset
        self.high_score = 0
    
    def reset_stats(self):
        #This initializes statistics that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1