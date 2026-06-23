from typing import Tuple, Union

# FIX: added type hints.
def get_range_for_difficulty(difficulty: str) -> Tuple[int, int]:
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: rearranged the different ranges for the different difficulty levels.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


# FIX: added type hints.
def parse_guess(raw: str) -> Tuple[bool, Union[int, None], Union[str, None]]:
    """
    Parse user input into an int guess.

    Returns: (ok: bool, 
              guess_int: int | None, 
              error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIX: added type hints.
def check_guess(guess: int, secret: int) -> Tuple[str, str]:
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: removed erroneous string casting.
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


# FIX: added type hints.
def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: made it so the score would only decrease with incorrect guesses
    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5
