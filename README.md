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
   git clone https://github.com/yourusername/mastermind-game.git
   cd mastermind-game
   ```

2. Create a virtual environment 
   ```
   cd mastermind-game-li/backend
   python3 -m venv venv
   ```

3. Activate virtual environment
   - On macOS/Linux:
   ```
    source venv/bin/activate
   ```
   - On Windows:
   ```
   venv\Scripts\activate
   ```
4. Install backend dependencies
  ```
  pip install -r requirements.txt
  ```

5. Install frontend dependencies
   ```
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
   ` npm start `
  
### Playing the game
1. Option 1: Through the browser
  - After starting the Flask and React development server, open your browser and go to http://localhost:3000 to play the game.
2. Option 2: Postman API Request
  - After starting the Flask server, you can use Postman to send POST request to http://localhost:5000 to interact directly with the backend.Refer to the API section below.  
   
## API Endpoints
### Start a New Game
- URL: `/start`
- Method: POST
- Description: initializes a new game session
- Request Body: None
- Response Example:
  ```
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
  - a string representing the players guess
- Response Example:
  ```
  ```

## Code Structure

### Backend

### Frontend
