import random

winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

file_name = "rating.txt"


def read_ratings():
    my_file = open(file_name, mode="r")
    rating_dict = dict()

    for line in my_file:
        current_line = line.strip("\n").split(" ")
        rating_dict[current_line[0]] = current_line[1]

    my_file.close()
    return rating_dict


def get_username():
    print("Enter your name: ", end="")
    return input()


def get_rating(a_ratings, a_username):
    rating = 0
    for key, value in a_ratings.items():
        if key == a_username:
            rating = int(value)
    return rating


# Program entry
score_dict = read_ratings()
user_name = get_username()
user_score = get_rating(score_dict, user_name)
print("Hello, " + user_name)

# Input: Choose options or input empty space to go with default
rules_input = input()
if rules_input == "":
    rules_input = "rock,paper,scissors"
options = rules_input.split(",")
print("Okay, let's start")

# Game Loop
while True:
    user_move = input().lower()
    comp_move = random.choice(options)

    if user_move == "!rating":
        print(f"Your rating: {user_score}")
        continue

    if user_move == "!exit":
        print("Bye!")
        break

    if user_move not in options:
        print("Invalid input")
        continue

    if user_move == comp_move:
        user_score += 50
        print(f"There is a draw ({comp_move})")
    elif comp_move in winning_cases[user_move]:
        user_score += 100
        print(f"Well done. The computer chose {comp_move} and failed")
    else:
        print(f"Sorry, but the computer chose {comp_move}")
