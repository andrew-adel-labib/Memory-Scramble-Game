<div align="center">

<h1>🎮 Memory Scramble</h1>

<p>A professional card-matching puzzle game built with Python & Pygame</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pygame-2.x-green?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pytest-tested-orange?style=for-the-badge&logo=pytest&logoColor=white"/>
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-blue?style=for-the-badge&logo=githubactions&logoColor=white"/>
</p>

<p>
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-gameplay">Gameplay</a> •
  <a href="#-team">Team</a>
</p>

</div>

---

## 📖 Overview

**Memory Scramble** is a card-matching puzzle game where players flip cards attempting to discover matching pairs before the countdown timer expires. The board is configurable, cards are randomized on every session, and the game tracks moves and time to deliver a competitive single-player experience.

Beyond gameplay, this project is a showcase of **professional software engineering practices** — modular architecture, OOP design, centralized logging, custom exception handling, automated testing, CI/CD pipelines, and clean Git collaboration workflows.


---

## ✨ Features

### 🎮 Gameplay

| Feature | Description |
|---|---|
| Dynamic Board | Configurable rows & columns |
| Countdown Timer | Race the clock to find all pairs |
| Randomized Cards | Shuffled on every game session |
| Match Detection | Automatic pair validation |
| Move Counter | Track efficiency across sessions |
| Win / Lose Conditions | Clear end-game feedback screens |
| Responsive UI | Smooth graphical rendering via Pygame |

### 🏗️ Engineering

| Practice | Tool |
|---|---|
| Unit Testing | Pytest |
| Code Linting | Flake8 |
| Code Formatting | Black |
| CI/CD Pipeline | GitHub Actions |
| Dependency Management | UV |
| Logging | Python `logging` module |
| Exception Handling | Custom exception hierarchy |

---

## 🗂️ Project Structure

```
memory-scramble-game/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml        # CI/CD pipeline
│
├── assets/
│   ├── fonts/                   # Poppins, Orbitron
│   └── icons/                   # PNG card icons
│
├── docs/
│   └── screenshots
│
├── logs/
│   └── game.log                 # Runtime logs
│
├── src/
│   ├── main.py                  # Entry point
│   ├── core/                    # Game logic (board, cards, timer)
│   ├── ui/                      # Menus, screens, rendering
│   └── utils/                   # Logger, exceptions, helpers
│
├── tests/                       # Pytest test suite
│
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

---

## 🛠️ Technologies

| Technology | Version | Purpose |
|---|---|---|
| Python | 3.12 | Core language |
| Pygame | Latest | Game rendering & input |
| Pytest | Latest | Unit testing |
| Flake8 | Latest | Linting |
| Black | Latest | Code formatting |
| GitHub Actions | — | CI/CD |
| UV | Latest | Dependency management |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/andrew-adel-labib/Memory-Scramble-Game.git
cd Memory-Scramble-Game
```

### 2. Set Up the Environment

#### Option A — UV *(Recommended)*

```bash
# Install UV: https://github.com/astral-sh/uv
uv sync

# Activate the virtual environment
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

#### Option B — pip

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Game

```bash
python -m src.main
# or
python src/main.py
```

---

## 🧪 Development Commands

```bash
# Run all tests
pytest

# Lint source and tests
flake8 src tests

# Check formatting
black --check src tests

# Auto-format code
black src tests
```

---

## 🎮 Gameplay

### How to Play

1. Launch the game and start a new session
2. Click any card to reveal it
3. Click a second card — if they match, both stay face-up
4. If they don't match, both flip back after a short delay
5. Match all pairs before the countdown timer hits zero to win

### Rules

- Only **two cards** can be revealed at a time
- Unmatched pairs flip back automatically
- The game ends in **defeat** if the timer reaches zero
- The game ends in **victory** when all pairs are matched

---

## 📝 Logging

All runtime events are written to `logs/game.log`:

```
2026-05-16 18:20:11 | INFO  | Game started
2026-05-16 18:20:22 | INFO  | Card selected: position (2, 3)
2026-05-16 18:20:25 | INFO  | Match found: heart.png
2026-05-16 18:21:10 | WARN  | Timer expired — game over
```

---

## ⚠️ Exception Handling

The project uses a **custom exception hierarchy** with centralized handling:

- Asset loading failures are caught and reported gracefully
- Board configuration is validated before game start
- Timer and state errors raise typed exceptions for clean recovery

---

## 🔄 CI/CD Pipeline

Every push triggers the GitHub Actions workflow at `.github/workflows/python-ci.yml`:

```
Install dependencies  →  Flake8 lint  →  Black format check  →  Pytest
```

---

## 🌿 Git Workflow

All members follow this daily workflow:

```bash
git pull origin main
git add .
git commit -m "feat: descriptive message describing the change"
git push origin main
```

> Use meaningful commit prefixes: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`

---

## 👥 Team

| Name | Responsibility |
|---|---|
| **Andrew** | Utilities, Services, CI/CD (`.github/`), `requirements.txt`, `pyproject.toml`, `uv.lock`, test suite |
| **Bassandah** | Core game logic, UI & rendering — board generation, card matching, timer, win/lose conditions, menus, game screens, HUD, hover effects, themes |
---

## 📂 Assets

### Icons
Place `.png` card icons inside `assets/icons/`:
```
apple.png   banana.png   car.png     cat.png    diamond.png
flower.png  heart.png    moon.png    rocket.png  star.png
```

### Fonts
Place font files inside `assets/fonts/`:
```
Poppins-Regular.ttf   Poppins-Bold.ttf   Orbitron-Regular.ttf
```

---

## 🙌 Acknowledgements

- [Python Community](https://www.python.org/)
- [Pygame Developers](https://www.pygame.org/)
- Open-source contributors
