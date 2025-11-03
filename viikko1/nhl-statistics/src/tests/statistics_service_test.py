from statistics_service import StatisticsService, SortBy
from player import Player
import unittest
from unittest.mock import patch

class PlayerReaderStub():
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
            ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_existing_player_search(self):
        query = "Semenko"
        result = self.stats.search(query)
        self.assertIn(query, result.name)

    def test_nonexistent_player_search(self):
        query = "Hello"
        result = self.stats.search(query)
        self.assertIsNone(result)

    def test_team(self):
        team = self.stats.team("EDM")
        for t in team:
            self.assertIn("EDM", t.team)

    def test_top_points(self):
        top_players = self.stats.top(4, SortBy.POINTS)
        top_points = [p.points for p in top_players]
        top_points_test = sorted(top_points)
        top_points_test.reverse()
        self.assertEqual(top_points, top_points_test)

    def test_top_goals(self):
        top_players = self.stats.top(4, SortBy.GOALS)
        top_goals = [p.goals for p in top_players]
        top_goals_test = sorted(top_goals)
        top_goals_test.reverse()
        self.assertEqual(top_goals, top_goals_test)

    def test_top_assists(self):
        top_players = self.stats.top(4, SortBy.ASSISTS)
        top_assists = [p.assists for p in top_players]
        top_assists_test = sorted(top_assists)
        top_assists_test.reverse()
        self.assertEqual(top_assists, top_assists_test)

