# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game purpose:**
A number-guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. The difficulty setting controls the number range and attempt limit — Easy (1–20, 6 attempts), Normal (1–100, 8 attempts), Hard (1–200, 5 attempts). After each guess the game gives a "Too High" or "Too Low" hint and tracks a score.

**Bugs found:**
1. **Hard difficulty had a smaller range than Normal** — `get_range_for_difficulty("Hard")` returned `(1, 50)` instead of a range larger than Normal's `(1, 100)`.
2. **Info banner always showed "1 to 100"** — the `st.info()` f-string used hardcoded string literals instead of the `low` and `high` variables already computed from the selected difficulty.
3. **Attempts counter started at 1** — `st.session_state.attempts` was initialized to `1`, so the first guess was displayed as "attempt 2" instead of "attempt 1".

**Fixes applied:**
- Changed Hard difficulty range to `(1, 200)` in `get_range_for_difficulty()` in both `app.py` and `logic_utils.py`.
- Replaced hardcoded `"1 and 100"` with `{low}` and `{high}` in the `st.info()` banner, and also fixed the "New Game" button to use `random.randint(low, high)`.
- Changed `st.session_state.attempts` initialization from `1` to `0`.
- Refactored `get_range_for_difficulty` and `check_guess` into `logic_utils.py` so pytest can import them without triggering Streamlit.
- Fixed the 3 starter tests to unpack the `(outcome, message)` tuple returned by `check_guess`.
- Added 4 new targeted pytest cases covering each bug fix (7 tests total, all passing).

## 📸 Demo

**Pytest results (all 7 tests passing):**
```
tests/test_game_logic.py::test_winning_guess         PASSED
tests/test_game_logic.py::test_guess_too_high        PASSED
tests/test_game_logic.py::test_guess_too_low         PASSED
tests/test_game_logic.py::test_hard_range_larger_than_normal  PASSED
tests/test_game_logic.py::test_easy_range            PASSED
tests/test_game_logic.py::test_normal_range          PASSED
tests/test_game_logic.py::test_hard_range            PASSED
tests/test_game_logic.py::test_initial_attempts_value PASSED

8 passed in 0.XXs
```
> To add a screenshot: run `python -m pytest tests/test_game_logic.py -v` in your terminal, take a screenshot, and replace this block with `![pytest results](screenshot.png)`.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
