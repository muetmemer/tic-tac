**Project Documentation**

# TicTacToe Game

Welcome to the TicTacToe game! This project is a simple implementation of the classic TicTacToe game in Python. It allows two players to play the game on a 3x3 grid, taking turns to place their markers (X or O) on the board. The game checks for a winner or a tie after each move and provides an option to play again.

## Features

- Two-player gameplay
- Players can choose their markers (X or O)
- The game checks for a win or a tie after each move
- The board is displayed after each move
- Option to play again after a game ends

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/your-username/tictactoe.git
```

**1. Intended Logic and Efficient Code Implementation**
The provided code is a basic implementation of a Tic Tac Toe game in Python. It demonstrates how to structure a game, handle user inputs, and check for winning conditions.

**2. Programming Fundamentals**
The code utilizes several fundamental programming constructs:

**Classes and Objects:** The TicTacToe class encapsulates all game-related functionalities.
**Control Flow:** It uses loops and conditionals to manage the game flow and check for win conditions.
**Functions:** Methods are defined within the class to modularize the game's logic.

**3. Project Logic Plan**
Below is the flowchart that represents the logic of the Tic Tac Toe game:

                +---------------------------------+
                | Start                           |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Initialize game board           |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Players choose markers          |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Display board                   |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Player 1 turn                   |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Player 1 chooses position       |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Place marker and check win/tie  |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Player 2 turn                   |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Player 2 chooses position       |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Place marker and check win/tie  |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | Replay?                         |
                +---------------------------------+
                              |
                              v
                +---------------------------------+
                | End                             |
                +---------------------------------+

**4. Validation and Error Fixes**
4.1 Error-based Fixes
Ensured the clearoutput method clears the screen correctly.
Checked user input validity in player_input and player_choice methods.

**4.2 Manual Testing**
Manual testing was done by running the script and playing the game multiple times to check for bugs and validate the flow.
Used PEP8 validator for code style and adherence to Python standards.

**5. Code Separation**
**Application Code:** The entire TicTacToe class.
External Code: No external libraries or tutorials were used in this implementation.

**7. Implementation Efficiency**
The code efficiently handles game logic, user input, and board state checks.
The win conditions are checked using a simple and readable set of conditions.

**8. Documentation of Libraries and Rationa**le
8.1 Necessary Libraries
No external libraries are required for this basic implementation.
8.2 Project Outcomes
The game correctly initializes, processes user inputs, checks for win conditions, and offers replay functionality.
Screenshots demonstrate a successful run of the game (not included here but should be captured during manual testing).
8.3 Project Rationale
The project aims to provide a simple, interactive command-line Tic Tac Toe game. It is designed to be user-friendly and demonstrate basic programming constructs for educational purposes.

# Deploying to Heroku

This guide will help you deploy your application to Heroku using the Heroku CLI.

## Prerequisites

- Ensure you have the Heroku CLI installed on your machine. You can download it from [here](https://devcenter.heroku.com/articles/heroku-cli).

## Steps to Deploy

1. **Login to Heroku:**

    First, you need to login to your Heroku account. Run the following command in your terminal:

    ```sh
    heroku login
    ```

2. **Create a New Heroku App:**

    Create a new application on Heroku. Replace `your-app-name` with the desired name of your application:

    ```sh
    heroku create your-app-name
    ```

3. **Initialize a Git Repository:**

    Initialize a new Git repository in your project directory:

    ```sh
    git init
    ```

4. **Add Files to Git:**

    Add all your project files to the repository:

    ```sh
    git add .
    ```

5. **Commit Your Changes:**

    Commit the changes with an initial commit message:

    ```sh
    git commit -m "Initial commit"
    ```

6. **Push to Heroku:**

    Push your code to the Heroku remote repository:

    ```sh
    git push heroku master
    ```

7. **Scale Your Application:**

    Scale your application to run a worker. This command scales the application to one worker dyno:

    ```sh
    heroku ps:scale worker=1
    ```

## Conclusion

Following these steps, your application should now be deployed to Heroku and running. You can manage your application from the Heroku dashboard or using additional Heroku CLI commands.
