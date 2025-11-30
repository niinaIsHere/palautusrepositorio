class TennisGame:
    MIN_POINTS_TO_WIN = 4
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE = 1
    WIN = 2

    SCORE_NAMES = {
        0: 'Love',
        1: 'Fifteen',
        2: 'Thirty',
        3: 'Forty'
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def tie(self):
        return self.player1_score == self.player2_score
    
    def tie_score(self):
        points = self.player1_score
        if points > self.THIRTY:
            return 'Deuce'
        return self.SCORE_NAMES[points] + '-All'

    def possible_win(self):
        return self.player1_score >= self.MIN_POINTS_TO_WIN or self.player2_score >= self.MIN_POINTS_TO_WIN

    def difference(self):
        return self.player1_score - self.player2_score

    def possible_win_score(self):
        difference = self.difference()
        if difference == self.ADVANTAGE:
            return "Advantage " + self.player1_name
        elif difference == -self.ADVANTAGE:
            return "Advantage " + self.player2_name
        elif difference >= self.WIN:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name
    
    def construct_score(self):
        return self.SCORE_NAMES[self.player1_score] + '-' + self.SCORE_NAMES[self.player2_score]
        
    def get_score(self):
        if self.tie():
            return self.tie_score()
        elif self.possible_win():
            return self.possible_win_score()
        else:
            return self.construct_score()
