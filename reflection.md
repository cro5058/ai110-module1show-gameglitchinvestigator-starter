# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - The hints were indeed backwards -- for example, when the 
    correct answer was 89 and I guessed 99, it told me to go higher,
    and when the correct answer was 89 and I guessed 17, it told me to go lower.
  - The secret was getting converted to a string on even-numbered guess attempts.
  - The attempt counting logic was not quite right -- 
    the attempt log was always one attempt behind in logging what I typed.
  - The easy, medium, and hard levels were wrong -- 
    easy should have a range of 1 to 20, medium from 1 to 50, and hard from 1 to 100.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 18 (secret was 16) | "Go Lower" hint | "Go Higher" hint | none |
| Guess of 18 (secret was 21) | "Go Higher" hint | "Go Lower" hint | none |
| Guess of 15 (1 attempt used) | Attempts remaining: 7 | Attempts remaining: 6 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - In this project, I used Claude exclusively.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude suggested a way of resetting the game when the user changed the difficulty, 
  which worked correctly and stood up to testing. 
  - I tested the new difficulty changing feature by clicking "new game" in two cases: 
  one where I had already made a guess, and another where I had not yet made any guesses. 
  I repeated these cases with all three levels of difficulty. 
  Additionally, I checked to see if the game recognized my chosen difficulty level, 
  and whether it reset the history, attempt number, and secret number variables 
  upon choosing the new difficulty.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - To fix a bug where the site did not display an updated history and attempt count after a user made and submitted a guess, Claude incorrectly suggested grouping the guess text box and "submit guess" button into a "form" element. I was suspicious of this suggestion from the beginning because it fundamentally changed the site's user interface, but the suggestion ultimately proved to be incorrect when the same issue persisted despite the button and text box being grouped into a form.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decided if a bug was really fixed mainly by playtesting various scenarios
  on the actual website and seeing if the site behaved as I expected it to. 
  This was especially relevant to UI-based bugs, which are difficult to test purely in code.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One test I ran was to check the outcome of various guesses -- 
  for example, if a guess of 85 with a correct answer of 50 would give an outcome of "too high".

- Did AI help you design or understand any tests? How?
  - I used AI to design the tests in logic_utils.py. The logical functions were relatively easy and formulaic
  to test in code, whereas testing UI-based elements required me to personally use the website and ensure
  it behaved as I expected.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns cause the web app to be reloaded.
  - Session state is a set of variables that the web app must keep track of to ensure the information and appearance of the app are always up to date as the user uses it.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - In future projects, I would like to continue the practice of adding FIXME comments to code that needs to be edited, and FIX comments where it has been fixed. 

- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time, I would try to make my prompts simpler and clearer.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - This project made me trust AI-generated code more. I was able to see AI as a partner more than I have on previous projects.
