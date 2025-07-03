
## 🏏 Handcricket Game (Python CLI Version)

A terminal-based handcricket game where you play against the computer.  
Built using Python OOP principles, featuring basic game mechanics and an anti-cheat system.


---

## 🗂️ Project Structure

```
Project/
├── GameScores/              # Folder where match histories are saved
├── init.py              # Placeholder/init file (not used actively)
├── main.py                  # Game entry point
├── game\_engine.py           # Toss logic and innings mechanics
├── player\_and\_computer.py   # Input logic for player and computer
├── helping\_tools.py         # Game utilities and cheat-detection
```

---

## ⚙️ Requirements

- Python **3.6+**
- Cross-platform (Tested on **Linux**, works on **Windows** too)

---

## ▶️ How to Play

```bash
python3 main.py   # On Linux/Mac
python main.py    # On Windows
```

1. Choose **Odd or Even** for the toss
2. Enter a number between **0–10**
3. Win/lose the toss and proceed with **Batting** or **Bowling**
4. First Innings:
   * If batting: score as much as possible
   * If bowling: try to get the computer out early
5. Second Innings:
   * If batting: beat the target to win
   * If bowling: prevent the computer from chasing your score

---

## 🚨 Anti-Cheat System

If you spam the same number while bowling, the computer will **adapt** and change its input to prevent trap-outs.

---

## 📝 Game History

* After each match, a file is saved inside `GameScores/`
* Format: `<NAME>_<TIMESTAMP>.txt`

---

## 🌟 Features

* Modular code (multiple organized files)
* Clear CLI prompts
* Anti-spam cheat system
* Match replay loop
* Match logs with timestamps
* Readable and maintainable code

---

## 🔍 What You’ll find

This project is great for beginner-to-intermediate learners to understand:

* Python OOP (classes, methods, object interaction)
* Modular code structuring
* User input and game flow
* File handling in Python
* Clean terminal-based UX

---

## 🚧 Future Improvements

* Player login/profile system
* GUI version using **Tkinter** or **Pygame**
* Save scores in `.csv` or `.json` for easier tracking

---

## 👨‍💻 Author

Made with passion by **Thiruvenkatachari**
Feel free to **fork**, **play**, and **contribute**!
