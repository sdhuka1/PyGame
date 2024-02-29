class GameStats:
    #This tracks statistics for Alien Invasion

    def __init__(self, ai_game):
        #This initializes statistics
        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        #This initializes statistics that can change during the game
        self.ships_left = self.settings.ship_limit