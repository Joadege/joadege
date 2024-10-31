import random
import time

# Global game data
is_user_logged_in = False
is_game_saved = False
selected_difficulty = None
user_team_name = None
computer_team_name = "Rival College"
user_score, computer_score = 0, 0
current_inning = 1
current_outs = 0

# Possible hit outcomes for player's batting
hit_outcome_types = ["single", "double", "triple", "home run"]

# 1. Start the Game
def start_game():
    """Displays welcome message and initiates the login process."""
    print("Welcome to College Baseball Game!")
    time.sleep(1)
    login()

# 2. Login System
def login():
    """Simulates user login by asking for a username."""
    global is_user_logged_in
    while not is_user_logged_in:
        username = input("Enter Username: ")
        if username:
            print("Login successful!")
            is_user_logged_in = True
            main_menu()
        else:
            print("Invalid input. Try again.")

# 3. Main Menu
def main_menu():
    """Displays the main menu and handles the user's choice for game mode or exit."""
    print("\nMain Menu")
    choice = input("1: Franchise Mode\n2: Exit\nSelect an option: ")
    if choice == '1':
        handle_game_save_option()
    else:
        print("Exiting game.")
        exit()

# 4. Game Save Option
def handle_game_save_option():
    """Handles game loading based on user's choice."""
    global is_game_saved
    if input("Load a saved game? (yes/no): ").lower() == "yes":
        is_game_saved = True
        print("Game loaded.")
    select_difficulty()

# 6. Difficulty Selection
def select_difficulty():
    """Allows user to select game difficulty and moves to team selection."""
    global selected_difficulty
    while not selected_difficulty:
        difficulty = input("Select Difficulty (Easy/Medium/Hard): ")
        if difficulty.lower() in ["easy", "medium", "hard"]:
            selected_difficulty = difficulty.lower()
            choose_team_name()
        else:
            print("Invalid choice. Please select a valid difficulty.")

# 7. Team Selection
def choose_team_name():
    """Prompts user to enter their team name."""
    global user_team_name
    user_team_name = input("Enter your team name: ")
    print(f"You have selected {user_team_name}!")
    display_loading_screen()

# 8. Loading Screen
def display_loading_screen():
    """Displays a loading message before the game begins."""
    print("Loading game...")
    time.sleep(2)
    begin_match()

# 9. Start the Game
def begin_match():
    """Main game loop handling innings, score updates, and end game check."""
    global current_inning, current_outs, user_score, computer_score
    print("\nGame Start!")
    while current_inning <= 9:
        print(f"\nInning {current_inning}:")
        current_outs = 0
        while current_outs < 3:
            player_batting_phase()
            computer_fielding_phase()
            current_outs += 1
        current_inning += 1
        update_scoreboard()
    conclude_game()

# 10. Pitching and Batting Mechanics
def player_batting_phase():
    """Simulates player's batting phase and updates the score based on hit outcome."""
    global user_score
    user_action = input("Press 's' to swing or 'w' to watch: ")
    if user_action == 's':
        contact_result = random.choice(["hit", "miss"])
        if contact_result == "hit":
            hit_result = random.choice(hit_outcome_types)
            print(f"You hit a {hit_result}!")
            calculate_score(hit_result)
        else:
            print("Swing and a miss!")
    else:
        print("Ball!")

def computer_fielding_phase():
    """Placeholder for fielding mechanics when the computer is batting."""
    print("Computer is batting...")

# 11. Scoring Mechanism
def calculate_score(hit_result):
    """Updates player score based on type of hit made."""
    global user_score
    hit_to_score = {"single": 1, "double": 2, "triple": 3, "home run": 4}
    user_score += hit_to_score[hit_result]

# 12. Scoreboard Update
def update_scoreboard():
    """Displays the current scoreboard after each inning."""
    print(f"Scoreboard Update: {user_team_name} {user_score} - {computer_team_name} {computer_score}")

# 13. Game Conclusion
def conclude_game():
    """Displays the final score and announces the winner."""
    print("\nFinal Score:")
    print(f"{user_team_name}: {user_score}")
    print(f"{computer_team_name}: {computer_score}")
    if user_score > computer_score:
        print(f"{user_team_name} wins!")
    elif computer_score > user_score:
        print(f"{computer_team_name} wins!")
    else:
        print("It's a tie!")
    display_post_game_options()

# Post-game options
def display_post_game_options():
    """Handles end-of-game options like saving the game."""
    if input("Would you like to save the game? (yes/no): ").lower() == "yes":
        print("Game saved successfully.")
    print("Returning to Main Menu.")
    main_menu()

# Run the game
start_game()
