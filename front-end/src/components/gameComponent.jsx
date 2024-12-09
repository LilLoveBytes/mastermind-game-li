import React, { useState } from "react";
import axios from "axios";

const GameComponent = () => {
	const [guess, setGuess] = useState("");
	const [feedback, setFeedback] = useState("");
	const [history, setHistory] = useState("");
	const [gameStarted, setGameStarted] = useState(false);

	const startGame = async () => {
		try {
			const url = "http://localhost:3000/start";
			await axios.post(url);
			setGameStarted(true);
			setGuess("");
			console.log("Game started", gameStarted);
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
			console.log("guess", guess);
			setFeedback(result.feedback);
			console.log("feedback", result.feedback);
			setHistory("history", result.history);
			console.log("history", result.history);
			setGuess("");
		} catch (error) {
			console.log("Error submitting guess", guess, "error:", error);
		}
	};

	return (
		<div id="game-container">
			<h1> Hello, there! Welcome to Mastermind!</h1>
			<p> Are you a mastermind? Try to guess the secret code! </p>
			<button id="start-game" onClick={startGame}>
				{" "}
				Start A New Game{" "}
			</button>
			{/* display only after starting new game*/}
			{gameStarted && (
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
      </div>
)};
export default GameComponent;
