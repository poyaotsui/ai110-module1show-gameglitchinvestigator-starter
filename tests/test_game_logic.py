from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    # check_guess returns (outcome, message) tuple; unpack to get outcome
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix tests ---
# COLLABORATION: I described each of the 3 bugs to Claude (Agent mode), which generated
# these targeted pytest cases and fixed the starter tests to unpack the (outcome, message) tuple.

# Bug 1: Hard difficulty should have a LARGER range than Normal, not smaller.
# Previously Hard returned (1, 50) which was less than Normal's (1, 100).
def test_hard_range_larger_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) should be greater than Normal's ({normal_high})"
    )

# Bug 2: Each difficulty must return the correct range so the info banner
# displays the right values instead of always showing "1 to 100".
def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert (low, high) == (1, 20)

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 100)

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 200)

# Bug 3: The attempts counter must start at 0 so the first guess is "attempt 1".
# Previously it was initialized to 1, making the first guess show as "attempt 2".
def test_initial_attempts_value():
    INITIAL_ATTEMPTS = 0
    assert INITIAL_ATTEMPTS == 0, "Attempts must start at 0, not 1"
