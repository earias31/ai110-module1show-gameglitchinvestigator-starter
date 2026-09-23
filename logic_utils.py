def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 50),
        "Hard": (1, 100),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        value = int(float(raw))
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret): ##Used ai to move this from app.py and still work
    """Compare guess to secret and return a simple outcome string."""
    if guess == secret:
        return "Win"

    try:
        if guess > secret:
            return "Too High"
        return "Too Low"
    except TypeError:
        guess_str = str(guess)
        secret_str = str(secret)
        if guess_str == secret_str:
            return "Win"
        if guess_str > secret_str:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
