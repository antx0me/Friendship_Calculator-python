import random

def calculate_friendship_score(your_name, friend_name):
    # Generate a random friendship score between 0 and 100
    friendship_score = random.randint(0, 100)
    return friendship_score

def main():
    print("Welcome to the Friendship Calculator!")
    your_name = input("Enter your name: ")
    friend_name = input("Enter your friend's name: ")

    friendship_score = calculate_friendship_score(your_name, friend_name)

    print(f"Your friendship score with {friend_name} is: {friendship_score}%")

    if friendship_score >= 70:
        print("You are great friends!")
    else:
        print("You might need to work on your friendship!")

if __name__ == "__main__":
    main()
