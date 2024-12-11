import React, { useState } from "react";
import axios from "axios";

const GameComponent = () => {
	const [guess, setGuess] = useState("");
	const [feedback, setFeedback] = useState("");
	const [attemptHistory, setAttemptHistory] = useState("");
	const [guessHistory, setGuessHistory] = useState([]);
	const [gameStarted, setGameStarted] = useState(false);
	const [historyVisible, setHistoryVisible] = useState(false);
	const [numberOfAttempts, setNumberOfAttempts] = useState(0);
	const MAX_ATTEMPTS = 10;

	const startGame = async () => {
		try {
			const url = "http://localhost:3000/start";
			await axios.post(url);
			setGameStarted(true);
      setNumberOfAttempts(0);
      setFeedback("");
			setGuess("");
      setAttemptHistory("");
      setGuessHistory([]);
      setHistoryVisible(false);
		} catch (error) {
			console.log("Error starting game", error);
      
		}
	};

	const submitGuess = async (e) => {
		e.preventDefault();
		try {
			const url = "http://localhost:3000/guess";
			const response = await axios.post(url, { guess });
			const result = response.data;
			setFeedback(result.feedback);
			setAttemptHistory(result.history.message);
			setGuessHistory(result.history.guesses);
			setNumberOfAttempts(numberOfAttempts + 1);
			setGuess("");
		} catch (error) {
			console.log("Error submitting guess", guess, "error:", error);
		}
	};

	const toggleShowHistory = () => {
		setHistoryVisible(!historyVisible);
	};

	return (
		<div id="game-container">
			<h1> Hello, there! Welcome to Mastermind!</h1>
			<p> Are you a mastermind? Try to guess the secret code! </p>
			<button id="start-game" onClick={startGame}>
				{" "}
				Start A New Game{" "}
			</button>
			{gameStarted && numberOfAttempts < MAX_ATTEMPTS && (
				<form id="guess-form" onSubmit={submitGuess}>
					<input
						type="text"
						id="guess-input"
						maxLength={4}
						value={guess}
						onChange={(e) => setGuess(e.target.value)}
					/>
					<button type="submit"> Submit Guess </button>
				</form>
			)}
			<p> {feedback} </p>
			<p> {attemptHistory} </p>
			{gameStarted && guessHistory.length >= 1 && (
				<>
					<button id="guess-history" onClick={toggleShowHistory}>
						{historyVisible ? "Hide Guess History" : "Show Guess History"}
					</button>
					{historyVisible && <p>{guessHistory.join(", ")}</p>}
				</>
			)}
		</div>
	);
};
export default GameComponent;
