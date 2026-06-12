import random

print("=" * 45)
print("      WELCOME TO THE CYBER ARENA")
print("        ROCK ~ PAPER ~ SCISSORS")
print("=" * 45)

user_id = input("Enter your Gaming ID: ")
computer_id = "CyberBot-3000"

choices = ["rock", "paper", "scissors"]

play_again = "yes"

while play_again == "yes":

    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:

        print(f"\nScore -> {user_id}: {user_score} | {computer_id}: {computer_score}")

        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"{user_id} chose: {user_choice}")
        print(f"{computer_id} chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a Tie!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print(f"{user_id} wins this round!")
            user_score += 1

        else:
            print(f"{computer_id} wins this round!")
            computer_score += 1

    print("\n===== FINAL RESULT =====")

    if user_score > computer_score:
        print(f"🏆 Congratulations {user_id}! You won the match!")
    else:
        print(f"🤖 {computer_id} won the match!")

    play_again = input("\nPlay again? (yes/no): ").lower()

print(f"\nThanks for playing, {user_id}!")