# Pong Game

A simple 2D Pong game built from scratch using Python and Pygame. Instead of following step-by-step tutorials, this was made by adapting an existing skeleton, mapping out a custom roadmap, and using documentation to figure out the syntax and fix bugs.

## How It Works

- **The Code:** Written to be short, efficient, and readable without unnecessary clutter.
- **The Controls:** Standard movement logic keeping track of coordinates on the Cartesian plane.
- **The Enemy AI:** A straightforward opponent paddle that just tracks the ball's Y-coordinate to move up and down. It works perfectly for basic tracking and hitting the ball back.
- **Hardware Friendly:** Lightweight script optimized to run fast and smooth on low-spec or older computers.

## Game Structure

The engine follows a standard sequential setup:

1. **Initialize:** Sets up the Pygame window, caption, and initial positions.
2. **Game Loop:** 
   - Checks for player keyboard inputs.
   - Updates the ball's movement and handles basic wall/paddle collisions using bounding boxes.
   - Moves the enemy paddle up and down based on where the ball is.
   - Clears and updates the screen.
3. **States:** Logic switches based on whether you are on the start screen, playing the game, or looking at a game over screen.

## Built With

- **Python**
- **Pygame** (Using the documentation manual for reference)

## Downloads & Releases

If you just want to play the game without installing Python or setting up an environment, you can download the standalone executable directly from the **[Releases](https://github.com)** section.

- **Filename:** `pong.game.exe`

## Running from Source

### Prerequisites

Make sure you have Pygame installed:

```bash
pip install pygame
```

### Running the Game

Run the script directly from your terminal:

```bash
python "Src/pong game.py"
```

## Building the Executable Manually

If you want to compile the source code into your own standalone executable using the included configuration file, make sure you have `pyinstaller` installed:

```bash
pip install pyinstaller
```

Then run the compiler from the root directory pointing to your spec file:

```bash
pyinstaller "Src/pong game.spec"
```

## Project Files

Inside the `Src/` directory:
- `pong game.py` — The entire game source code (handles window creation, loop logic, and mechanics).
- `pong game.spec` — Config file used for compiling the project into a standalone executable.
- `gitignore` — Cleans up unnecessary temporary build or cache files from getting tracked.
