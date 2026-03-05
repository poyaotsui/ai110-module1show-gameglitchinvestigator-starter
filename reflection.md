# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1.Hard difficulty has a larger range than Normal 
2.The info banner always says "1 to 100" regardless of difficulty
3. Attempts counter starts at 1, so the first guess is already "attempt 2"
---

## 2. How did you use AI as a teammate?

I used Claude (Claude Code / Agent mode) as my primary AI tool on this project. I described bugs in plain English and Claude read the source files, proposed fixes, and wrote the code changes directly.

**Correct AI suggestion — Fix 2 (info banner hardcoded range):**
When I told Claude that the info banner always showed "1 to 100" regardless of difficulty, it correctly identified that the f-string on line 113 of `app.py` used hardcoded string literals `"1 and 100"` instead of the already-computed variables `low` and `high`. Claude replaced the literals with `{low}` and `{high}`, and I verified the fix by changing the difficulty dropdown to Hard and confirming the banner updated to "Guess a number between 1 and 200."

**Incorrect / misleading AI suggestion — starter test assertions:**
When Claude first wrote the bug-fix tests, it initially kept the same assertion style as the starter tests (`assert result == "Win"`). This was misleading because `check_guess` actually returns a tuple `("Win", "message")`, so those assertions would always fail. Claude only caught this after pytest ran and reported the failures. I verified the root cause by reading the `check_guess` return statements in `app.py`, then Claude corrected all three starter tests to unpack the tuple with `outcome, _ = check_guess(...)`.

---

## 3. Debugging and testing your fixes

I decided a bug was truly fixed when both a manual game run and a passing pytest test confirmed the correct behavior — one check alone wasn't enough.

**pytest run:** After implementing all three fixes and refactoring `check_guess` and `get_range_for_difficulty` into `logic_utils.py`, I ran `python -m pytest tests/test_game_logic.py -v`. All 7 tests passed: the 3 original starter tests (after fixing the tuple-unpacking issue) and the 4 new bug-fix tests targeting the Hard range, per-difficulty ranges, and the initial attempts value.

**Manual game run:** I launched the app with `streamlit run app.py`, switched to Hard difficulty, and confirmed the sidebar showed "Range: 1 to 200", the info banner matched, and the first guess was labeled "Attempt 1 of 5" — not "Attempt 2". This cross-checked the pytest results against real runtime behavior.

Claude helped design the tests by generating one test per bug (e.g. `test_hard_range_larger_than_normal` compares Hard's upper bound directly against Normal's) and explaining why `get_range_for_difficulty` needed to live in `logic_utils.py` so tests could import it without importing Streamlit.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
