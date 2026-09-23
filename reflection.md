# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Easy to understand. Not much to say.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were wrong. It would display go higher at 99, and go lower at 100
  New game doesnt work.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|selected hard | range 1-100 | 1-20 |none |
| new game| data is reset and a new game starts| nothing |none |
| submit guess| guess will submit| nothing happens | none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used the chat section and copilot. Copilot was mainly for debugging vscode. The chat section helped with all the other stuff.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Changing the display range of 1-100 to actually follow the difficulty. Before it displayed a static 1-100 range. Now it actually says 1 - whatever difficulty sets.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
The ai wanted to overcomplicate the logic, i had to tell it to keep the logic file and not make a new one. Beyond that it tries ti import other utils. I had to restate my prompt a few times.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I checked the code myself. After that I ran it and checked it again.
- Describe at least one test you ran (manual or using pytest)  
I repeatidly tested the hints. If the number was 43 id check 42 and 44 to see the go higher and lower tests.
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
Not really, I ran the tests myself. If the ai meeses up a test it can still return true due to faulty code. It's like asking the theif to double check if the diamon was stolen without verifying it yourself.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Its neat. It gives a nice way to view your code thats not in a terminal. I'd tell a friend that the set up is wonky but its worth it in the end.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I want to resue looking at the code first. I can understand what ai is doing if i at least know the code before asking it to change things.
- What is one thing you would do differently next time you work with AI on a coding task?
Be more specific. Sometimes i was too vauge and it messed up a decent bit.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I don't really like it. The ai has it uses, which im all for. Like a knife, it depends on the what the person using it does that makes it safe or unsafe. However, I can't ignore the costs on the enviornment and the impact data centers have on the surrounding community.
