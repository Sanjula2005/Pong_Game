
# Pong Game 🏓

Welcome to **Pong Game** — a digital recreation of the classic arcade game where two players control paddles and try to bounce a ball past each other to score points! This version is built using Python and the Turtle graphics library, offering a nostalgic yet competitive experience. Play against your friends and see who can score the most points!

---

## Features ✨

- **Classic Gameplay**: Play the classic Pong game with two paddles and a bouncing ball. The objective is to prevent the ball from passing your paddle while trying to score by sending it past your opponent.
- **Two Player Mode**: Control your paddle using keyboard inputs. Player 1 controls the left paddle using the "Q" (up) and "A" (down) keys, while Player 2 controls the right paddle using the "Up" and "Down" arrow keys.
- **Score Tracking**: Points are tracked for both players, and the scoreboard is updated in real-time.
- **Ball Speed Increase**: The ball’s speed gradually increases as the game progresses, adding to the challenge!
- **Responsive Controls**: The paddles move smoothly with the keyboard controls for quick and accurate play.

---

## How to Play 🎮

### Gameplay:
- **Objective**: Prevent the ball from passing your paddle while trying to get the ball past your opponent’s paddle.
- **Ball Movement**: The ball bounces off the top and bottom walls, as well as the paddles. If it hits either paddle, it changes direction.
- **Score**: Each time the ball passes a paddle, the opponent scores 1 point.
  
### Controls:
- **Player 1 (Left Paddle)**:
  - **Q**: Move up
  - **A**: Move down
- **Player 2 (Right Paddle)**:
  - **Up Arrow**: Move up
  - **Down Arrow**: Move down

### Scoring:
- When the ball passes the **left paddle**, Player 2 gets a point.
- When the ball passes the **right paddle**, Player 1 gets a point.
- The score is displayed at the top of the screen.

---

## Setup and Installation ⚙️

### Requirements:
- Python 
- Turtle graphics library 

### Running the Game:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Sanjula2005/Pong_Game.git
   cd Pong_Game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

Once the game starts, control your paddle using the keys provided and compete to score points!

---

## Code Structure 🧑‍💻

This project is divided into multiple files to keep the code organized:

### `main.py`:
- The main script that manages the game loop, paddle movement, ball behavior, and score updates.

### `ball.py`:
- Contains the `Ball` class, responsible for handling the ball’s movement, bouncing off walls and paddles, and resetting the ball after scoring.

### `paddle.py`:
- Contains the `Paddle` class, which defines how the paddles behave, including their movement (up and down).

### `scoreboard.py`:
- Contains the `Scoreboard` class to keep track of and display the scores for both players.

---

## Gameplay Walkthrough 🏁

- **Starting the Game**: Upon starting, the game opens a window with the paddles and ball displayed on a black background.
- **Ball Movement**: The ball bounces back and forth across the screen, bouncing off the paddles and top/bottom walls.
- **Scoring**: If the ball passes a paddle, the opponent scores a point, and the ball resets to the center.
- **Winning**: The game continues indefinitely, with no set limit. Players can track their scores in real-time and aim to get the highest score.

---

