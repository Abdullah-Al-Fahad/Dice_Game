# Non-Transitive Dice Game

This repository contains a Python implementation of a generalized non-transitive dice game. The game allows users to specify custom dice configurations and play against the computer in a provably fair manner. The game supports any number of dice (greater than 2) and ensures that the random number generation is fair and verifiable using HMAC (Hash-based Message Authentication Code).

---

## Features

- **Custom Dice Configuration**: Users can specify any number of dice with custom values via command-line arguments.
- **Provably Fair Random Number Generation**: The game uses cryptographically secure random number generation and HMAC to ensure fairness.
- **Interactive CLI**: The game provides an interactive command-line interface for users to select dice and make throws.
- **Probability Table**: The game displays a probability table showing the winning probabilities for each pair of dice.
- **Error Handling**: The game provides clear error messages for invalid inputs and configurations.

---

## Requirements

- Python 3.7 or higher
- `prettytable` library (for displaying probability tables)
- `colorama` library (for colored console output)

You can install the required libraries using:

```bash
pip install prettytable colorama
```

## How to Run

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the game using the following command:

```bash
python main.py <dice1> <dice2> <dice3> ...
```

## Game Rules

1. **Dice Configuration**:
   - Each die is represented by a comma-separated list of integers (e.g., `2,2,4,4,9,9`).
   - You can specify any number of dice (greater than 2) with custom values.

2. **Fair Random Generation**:
   - The game uses HMAC (Hash-based Message Authentication Code) to ensure that the random number generation is fair and verifiable.
   - Both the user and the computer contribute to the random number generation process.

3. **Gameplay**:
   - The game determines who makes the first move using a fair random selection (0 or 1).
   - Players take turns selecting dice and making throws.
   - The player with the higher throw wins the round.
   - If both players roll the same value, it’s a tie.

4. **Modulo Function**:
   - The modulo operation (`mod`) is used to ensure that the random number generated falls within the valid range of the dice.
   - For example, if a die has 6 faces, the result of the random number generation is calculated as `(user_number + computer_number) mod 6`.
   - This ensures that the result is always a valid index for the dice values (0 to 5 for a 6-faced die).

5. **Probability Table**:
   - The game provides a table showing the probability of winning for each pair of dice.
   - This helps the user make informed decisions when selecting dice.

6. **Fairness**:
   - The computer cannot cheat, as the random number generation is provably fair.
   - The user can verify the fairness by checking the HMAC and the secret key provided by the computer.

7. **Winning**:
   - The player with the higher throw wins the round.
  
## Acknowledgments

- This project was developed as part of **Task #3** of the internship program at **Intransition**.
- Special thanks to Intransition for providing the opportunity to work on this challenging and educational task, which helped deepen my understanding of fair random number generation, HMAC, and object-oriented programming.
