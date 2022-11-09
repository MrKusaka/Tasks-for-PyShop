from pprint import pprint
import random
import math


TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps: list[dict, ], offset: int) -> (int, int):
    """
    Takes list of game's stamps and time offset for which returns the scores for the home and away teams
    :param game_stamps: time and score of games
    :param offset: game time
    The dictionaries in the list should be sorted in ascending offset.
    The data passed to the function must be exactly the same as in the annotation.
    """
    # if the specified offset is not in game_stamps, then the nearest smallest element is taken
    while len(game_stamps) > 1:
        middle_stamp_id = len(game_stamps) // 2
        middle_stamp = game_stamps[middle_stamp_id]
        if middle_stamp['offset'] > offset:
            game_stamps = game_stamps[:middle_stamp_id]
        else:
            game_stamps = game_stamps[middle_stamp_id:]
    return game_stamps[0]["score"]["home"], game_stamps[0]["score"]["away"]
