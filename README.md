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
  - [Code Structure](#code-structure)
    - [Backend](#backend)
    - [Frontend](#frontend)

## Introduction

Mastermind is a player vs. computer game where the player tries to guess the secret code created by the computer within a certain number of attempts. This project provides a web interface for playing the game, with a backend server to handle game logic.

## Features

- Start a new game
- Submit guesses and receive feedback
- Track the number of attempts and guess history
- Display feedback and guess history to the player

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
   git clone[https://github.com/yourusername/mastermind-game.git](https://github.com/LilLoveBytes/mastermind-game-li.git)
   cd mastermind-game
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
   ` cd ../backend`
2. Start the Flask server with debug mode off:
   ` export FLASK_DEBUG=0`
   ` flask run`

### Running the Frontend

1. Navigate to the frontend directory:
   ` cd ../frontend`
2. Start the React development server:
   `npm start`

### Playing the game

1. Option 1: Through the browser

- After starting the Flask and React development server, open your browser and go to http://localhost:3000 to play the game utilizing a simple UI on the webpage.

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
    "feedback": "Your guess [7556] has 0 correct numbers, with 0 in the correct position.",
    "history": {
        "guesses": [
            "7556"
        ],
        "message": "You've made 1 guess(es) so far and have 9 attempt(s) remaining."
    },
    "message": "Guess submitted"
  }
  ```

## Code Structure

### Backend

The backend of this project is build using Flask, a lightweight framework in Python. The backend handles the game logic and API endpoints.

- **backend/**
  - **app/**
    - **models/**
      - `gameController.py`: Contains the game logic and functions for handling game state, guesses, and feedback.
    - **routes/**
      - `gameRoutes.py`: Defines teh Flask routes for starting a new game and submitting a guess
    - `__init__.py`: Initializes Flask application, set ups configurations, and registers blueprints.
    - `requirements.txt`: Lists the dependencies required for the backend.

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
