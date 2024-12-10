import requests
from flask import json, make_response, jsonify, request

MAX_ATTEMPTS = 10


def generate_secret_combo():
    try:
        url = "https://www.random.org/integers/"
        params = {
            "num": 4,
            "min": 0,
            "max": 7,
            "col": 1,
            "base": 10,
            "format": "plain",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # checks the response code and raises exception if error

        # strips whitespace and splits by newline
        secret_combo = response.text.strip().split("\n")
        # each element placed in list as integer
        secret_combo = [int(num) for num in secret_combo]

        return secret_combo

    except requests.exceptions.RequestException as e:
        raise Exception("Failed to generate secret combo")


def start_game():
    try:
        secret_combo = generate_secret_combo()
        game_state = {
            "secret_combo": secret_combo,
            "attempts": 0,
            "guesses": []
        }

        print("secret combo:", secret_combo)

        response = make_response(
            jsonify({"message": "New game started", "secret_combo": secret_combo}), 200)
        response.set_cookie("game_state", json.dumps(game_state))

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def submit_guess():
    try:
        game_state_cookie = request.cookies.get("game_state")

        if not game_state_cookie:
            return start_game()

        guess = request.json.get('guess')
        guess_array = [int(num) for num in guess]

        if not guess or len(guess_array) != 4:
            raise Exception("Guess must be exactly 4 numbers long")

        game_state = json.loads(game_state_cookie)
        game_state["attempts"] += 1
        game_state["guesses"].append(guess)

        if game_state["attempts"] >= MAX_ATTEMPTS:
            raise Exception("You've made 10 incorrect guess. Game over!")

        feedback = give_feedback(
            guess, guess_array, game_state["secret_combo"])
        history = get_history(game_state)
        response = make_response(jsonify(
            {"message": "Guess submitted", "history": history, "feedback": feedback}), 200)

        response.set_cookie("game_state", json.dumps(game_state))

        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_history(game_state):
    try:
        attempts = game_state["attempts"]
        guesses = game_state["guesses"]
        attempts_left = MAX_ATTEMPTS - attempts

        return ({
            "message": f"You've made {attempts} guess(es) so far and have {attempts_left} attempt(s) remaining.",
            "guesses": guesses
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def give_feedback(guess, guess_array, secret_combo):
    try:
        correctNumbers = 0
        exactMatches = 0
        secret_combo_count = {}

        # frequency of each number in the secret combo
        for num in secret_combo:
            if num in secret_combo_count:
                secret_combo_count[num] += 1
            else:
                secret_combo_count[num] = 1

        # check for exact matches
        for i in range(len(guess_array)):
            if guess_array[i] == secret_combo[i]:
                exactMatches += 1

        # check for correct numbers (any position)
        for i in range(len(guess_array)):
            if guess_array[i] in secret_combo_count.keys() and secret_combo_count[guess_array[i]] > 0:
                correctNumbers += 1
                secret_combo_count[guess_array[i]] -= 1

        if exactMatches == 4:
            return "You've guessed the correct combination!"
        else:
            return f"Your guess [{guess}] has {correctNumbers} correct numbers, with {exactMatches} in the correct position."

    except Exception as e:
        return ({"error": str(e)})
