"""
Tests covering the bug fixes made to logic_utils.py.

Run with: pytest test_game_logic.py
"""

import logic_utils


# --- get_range_for_difficulty: difficulty ranges (commit 17888b4) ---

def test_easy_range():
    assert logic_utils.get_range_for_difficulty("Easy") == (1, 20)


def test_normal_range():
    assert logic_utils.get_range_for_difficulty("Normal") == (1, 50)


def test_hard_range():
    assert logic_utils.get_range_for_difficulty("Hard") == (1, 100)


def test_unknown_difficulty_defaults_to_normal():
    assert logic_utils.get_range_for_difficulty("???") == (1, 50)


# --- parse_guess: only count attempts that are numbers (commit 566ff56) ---

def test_parse_valid_integer():
    assert logic_utils.parse_guess("42") == (True, 42, None)


def test_parse_float_truncates_to_int():
    ok, value, err = logic_utils.parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None


def test_parse_non_number_rejected():
    ok, value, err = logic_utils.parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_empty_string_rejected():
    ok, value, err = logic_utils.parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_none_rejected():
    ok, value, err = logic_utils.parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


# --- check_guess: simplified comparison without string casting (commit 7c8c34b) ---

def test_check_guess_win():
    outcome, _ = logic_utils.check_guess(50, 50)
    assert outcome == "Win"


def test_check_guess_too_high():
    outcome, _ = logic_utils.check_guess(80, 50)
    assert outcome == "Too High"


def test_check_guess_too_low():
    outcome, _ = logic_utils.check_guess(20, 50)
    assert outcome == "Too Low"


# --- update_score: score must not increase on a wrong guess (commit 060253e) ---

def test_score_does_not_increase_when_too_high():
    assert logic_utils.update_score(100, "Too High", 0) == 95


def test_score_does_not_increase_when_too_low():
    assert logic_utils.update_score(100, "Too Low", 0) == 95


def test_score_increases_on_win():
    # First attempt (attempt_number=0): 100 - 10*1 = 90 points awarded.
    assert logic_utils.update_score(0, "Win", 0) == 90


def test_win_score_floored_at_ten():
    # Many attempts should never award fewer than 10 points.
    assert logic_utils.update_score(0, "Win", 50) == 10
