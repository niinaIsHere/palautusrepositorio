import requests

class Player:
    def __init__(self, info):
        self.name = info['name']
        self.nationality = info['nationality']
        self.assists = info['assists']
        self.goals = info['goals']
        self.team = info['team']
        self.games = info['games']
        self.points = self.assists + self.goals

    def __str__(self):
        return f"{self.name}, {self.nationality}, {self.assists}, {self.goals}, {self.team}, {self.games}, {self.points}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        return requests.get(self.url).json() # pylint: disable=missing-timeout

class PlayerStats:
    def __init__(self, data=PlayerReader):
        self.data = data
        self.stats = self.data.get_players()

    def get_columns(self):
        cols = list(self.stats[0].keys())
        cols.pop()
        cols.append("points")
        return cols

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []

        for stat in self.stats:
            if stat['nationality'] == nationality:
                player = Player(stat)
                players_by_nationality.append(player)

        return sorted(players_by_nationality, key=lambda x: x.points, reverse=True)
