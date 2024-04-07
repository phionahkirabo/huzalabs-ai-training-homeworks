import random

def roll_dice():
    return random.randint(1, 6)

def play_turn(player):
    score = 0
    print(f"It's {player}'s turn.")
    while True:
        roll = roll_dice()
        print(f"{player} rolled: {roll}")
        if roll == 1:
            print(f"{player} got a Pig! No points earned this turn.")
            return 0
        score += roll
        print(f"{player}'s current score this turn: {score}")
        choice = input("Do you want to roll again? (yes/no): ")
        if choice.lower() != 'yes':
            return score

def play_game():
    players = ['Player 1', 'Player 2']
    scores = {'Player 1': 0, 'Player 2': 0}
    turn = 0

    while all(score < 100 for score in scores.values()):
        player = players[turn % 2]
        turn_score = play_turn(player)
        scores[player] += turn_score
        print(f"{player}'s total score: {scores[player]}")
        if turn_score != 0:
            print(f"{player} ends their turn with {scores[player]} points.")
        turn += 1

    winner = max(scores, key=scores.get)
    print(f"Congratulations, {winner} wins with {scores[winner]} points!")


play_game()
