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

- [x] Describe the game's purpose.
   - This is a number guessing game, where a user has a finite number of guesses to determine the secret number.

- [x] Detail which bugs you found.
   - This game was riddled with bugs. On the logical side, these included faulty difficulty levels, bad hints, and problematic score calculations.
   - On the UI side, bugs included the game not resetting when the difficulty was changed, as well as guess history and attempt counts not being updated after the user made a guess.

- [x] Explain what fixes you applied.
   - I fixed all the above bugs with the help of Claude.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the web app.
2. Open the sidebar.
3. Click on the dropdown menu for difficulty.
4. Change the difficulty to Hard.
5. User enters a guess of 50 → "Too Low".
6. Score updates.
7. User enters a guess of 75 → "Too Low".
8. Score updates.
9. User enters a guess of 90 → "Too Low".
10. Score updates.
11. User enters a guess of 95.
12. User wins the game.
13. Game animation shows and game ends.

## 🧪 Test Results

 pytest .\tests\test_game_logic.py
============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\ryano\Desktop\codepath\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 16 items                                                                                                                                                              

tests\test_game_logic.py ................                                                                                                                                 [100%]

============================================================================== 16 passed in 0.16s ==============================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
