import random

def game():
    print("You are playing the game...")

    # Generate a random score
    score = random.randint(1, 100)

    # Fetch the high score
    try:
        with open("high_score.txt", "r") as f:
            highscore = f.read().strip()
            if highscore:
                highscore = int(highscore)
            else:
                highscore = 0
    except FileNotFoundError:
        # If the file does not exist, initialize highscore to 0
        highscore = 0

    print(f"Your score: {score}")

    # Update the high score if the current score is higher
    if score > highscore:
        print("New high score!")
        with open("high_score.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"High score remains: {highscore}")

    return score

# Run the game function
game()