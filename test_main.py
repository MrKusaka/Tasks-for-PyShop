import unittest
from main import get_score


class TestGetScore(unittest.TestCase):

    def test_score(self):
        self.assertEqual(get_score([{'offset': 1, 'score': {'home': 0, 'away': 0}},
                                    {'offset': 3, 'score': {'home': 1, 'away': 1}},
                                    {'offset': 4, 'score': {'home': 1, 'away': 1}},
                                    {'offset': 7, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 9, 'score': {'home': 3, 'away': 2}}], 8), (2, 1))
        self.assertEqual(get_score([{'offset': 1, 'score': {'home': 0, 'away': 0}},
                                    {'offset': 3, 'score': {'home': 1, 'away': 1}},
                                    {'offset': 4, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 7, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 9, 'score': {'home': 3, 'away': 2}}], 4), (2, 1))
        self.assertEqual(get_score([{'offset': 3, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 4, 'score': {'home': 2, 'away': 2}},
                                    {'offset': 7, 'score': {'home': 2, 'away': 2}},
                                    {'offset': 9, 'score': {'home': 3, 'away': 3}}], 2), (2, 1))
        self.assertEqual(get_score([{'offset': 3, 'score': {'home': 0, 'away': 0}},
                                    {'offset': 4, 'score': {'home': 0, 'away': 0}},
                                    {'offset': 7, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 9, 'score': {'home': 3, 'away': 2}}], 20), (3, 2))
        self.assertEqual(get_score([{'offset': 3, 'score': {'home': 0, 'away': 0}},
                                    {'offset': 4, 'score': {'home': 1, 'away': 0}},
                                    {'offset': 6, 'score': {'home': 2, 'away': 1}},
                                    {'offset': 9, 'score': {'home': 3, 'away': 2}}], 5), (1, 0))
        self.assertEqual(get_score([{'offset': 3, 'score': {'home': 0, 'away': 0}}], 22), (0, 0))

