# Mastermind Game

Welcome to the Mastermind Game! This project is a web-based implementation of the classic code-breaking game, Mastermind.

## Table of Contents

- [Mastermind Game](#mastermind-game)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Running the Backend Server](#running-the-backend-server)
    - [Running the Frontend](#running-the-frontend)
    - [Playing the game](#playing-the-game)
  - [API Endpoints](#api-endpoints)
    - [Start a New Game](#start-a-new-game)
    - [Submit a Guess](#submit-a-guess)
  - [Backend Tests](#backend-tests)
    - [Running Backend Tests](#running-backend-tests)
  - [Code Structure](#code-structure)
    - [Backend](#backend)
    - [Frontend](#frontend)
  - [Future Work](#future-work)
    - [Implement difficulty levels](#implement-difficulty-levels)

## Introduction

Mastermind is a player-versus-computer game where the player has ten tries to guess the four-digit secret code created by the computer. This project provides a web interface for playing the game, with a backend server to handle game logic.

## Features

- Start a new game
- Submit guesses and receive feedback
- Track the number of attempts and guess history
- Display feedback and guess history to the player
- Ends the game after max number of attempts made

## Technologies Used

- **Frontend**: React.js
- **Backend**: Flask (Python)
- **HTTP Client**: Axios
- **Styling**: CSS

## Setup

### Prerequisites

- Node.js and npm
- Python and pip

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/LilLoveBytes/mastermind-game-li.git
   cd mastermind-game-li
   ```

2. Create a virtual environment

   ```sh
   cd mastermind-game-li/backend
   python3 -m venv venv
   ```

3. Activate virtual environment

   - On macOS/Linux:

   ```sh
    source venv/bin/activate
   ```

   - On Windows:

   ```sh
   venv\Scripts\activate
   ```

4. Install backend dependencies

   ```sh
   pip install -r requirements.txt
   ```

5. Install frontend dependencies
   ```sh
   cd ../frontend
   npm install
   ```

## Usage

### Running the Backend Server

1. Navigate to the backend directory:
   `cd ../backend`
2. Set debug mode to off:
   `export FLASK_DEBUG=0`
3. Start the Flask server:
   `flask run`

### Running the Frontend

1. Navigate to the frontend directory:
   ` cd ../frontend`
2. Start the React development server:
   `npm start`

### Playing the game

1. Option 1: Through the browser

- After starting the Flask server and the React development server, open your browser and go to http://localhost:3000 to play the game utilizing a simple UI on the webpage.

2. Option 2: Postman API Request

- After starting the Flask server, you can use Postman to send POST requests to http://localhost:5000 to interact directly with the backend. Refer to the API section below.

## API Endpoints

### Start a New Game

- URL: `/start`
- Method: POST
- Description: initializes a new game session
- Request Body: None
- Response Example:

  ```
  {
    "message": "New game started",
    "secret_combo": [
        0,
        1,
        4,
        3
    ]
  }
  ```

### Submit a Guess

- URL: `/guess`
- Method: POST
- Description: submits a guess and returns feedback
- Request Body:
  ```
  {
    "guess": "1234"
  }
  ```
  - "guess": a string representing the players guess
- Response Example:

  ```
  {
    "feedback": "Your guess [1237] has 2 correct numbers, with 0 in the correct position.",
    "history": {
        "guesses": [
            "7556",
            "1234",
            "1237"
        ],
        "message": "You've made 3 guess(es) so far and have 7 attempt(s) remaining."
    },
    "message": "Guess submitted"
  }
  ```

## Backend Tests

The backend tests are written using the `unittest` module in Python. These tests ensure that the game logic and API endpoints work as expected.

### Running Backend Tests

To run the backend test, navigate to the `backend` directory and use the following command:

```sh
PYTHONPATH=backend python -m unittest discover -s backend/app/tests
```

This command sets the `PYTHONPATH` to include the `backend` directory and runs the tests using the `unittest` discovery mechanism.

## Code Structure

### Backend

The backend of this project is build using Flask, a lightweight framework in Python. The backend handles the game logic and API endpoints.

- **backend/**
  - **app/**
    - **models/**
      - `gameController.py`: Contains the game logic and functions for handling game state, guesses, and feedback.
    - **routes/**
      - `gameRoutes.py`: Defines the Flask routes for starting a new game and submitting a guess
    - `__init__.py`: Initializes Flask application, sets up configurations, and registers blueprints.
    - `requirements.txt`: Lists the Python dependencies required for the backend.

### Frontend

The frontend of this project is built using React.js. It provides the user interface for interacting with this game.

- **frontend/**
  - **public/**
  - **src/**
    - **components/**
      - `GameComponent.jsx`: Handles the game interface, including button to start a game, form for submiting guesses, and button to display feedback.
    - `App.js`: Sets up the main structure of the application.
    - `index.js`: Entry point for the React application
    - `package.json`: Lists the JavaScript dependencies and scripts for the frontend.

## Future Work

### Implement difficulty levels

I plan to enhance this game by adding difficulity levels. The current configuration will be considered the "Normal" level. In the "Hard" level, players will attempt to guess a six-digit number in five or fewer attempts. Players will be able to select their difficulty level at the start of a new game.
