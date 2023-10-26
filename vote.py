 # Dictionary to store roll numbers and their vote status
voted_users = {}

# Dictionary to store candidate names and their vote counts
candidates = {
    "Doremon": 0,
    "Shinchan": 0,
    "Oggy": 0,
}

# Admin's password
admin_password = "gps@578"

# Function to vote
def vote():
    roll_number = input("Enter your roll number: ")

    if roll_number in voted_users:
        print("You have already voted.")
    else:
        print("Candidates:")
        for candidate in candidates.keys():
            print(candidate)

        user_choice = input("Enter the name of the candidate you want to vote for: ")

        if user_choice in candidates:
            candidates[user_choice] += 1
            voted_users[roll_number] = True
            print("Thank you for voting for", user_choice)
        else:
            print("Invalid candidate name. Please try again.")

# Function to display the count to the admin
def display_count(password):
    if password == admin_password:
        print("Vote Count:")
        for candidate, count in candidates.items():
            print(candidate, ":", count)
    else:
        print("Admin password is incorrect. Access denied.")

# Main program loop
print("hi")
while True:
    print("\nOnline Voting System")
    print("1. Vote")
    print("2. Display Vote Count (Admin Only)")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vote()
    elif choice == "2":
        password = input("Enter admin password: ")
        display_count(password)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")