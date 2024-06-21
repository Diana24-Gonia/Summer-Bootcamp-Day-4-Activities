import random  # Importing the random module to use its choice function

# Player 1 input
P1 = input("P1, Enter your choice (kulob/hayang): ").strip().lower()
#This is where the user input his /her choice in lowercase.

# Validate Player 1 input
while P1 not in ["kulob", "hayang"]: 
    # If the input is not 'kulob' or 'hayang',input again your choice
    print("Invalid choice. Please enter 'kulob' or 'hayang'.")
    P1 = input("P1, Enter your choice (kulob/hayang): ").strip().lower()
    # input again until you get your kind of choice

# Computer choices
choices = ["kulob", "hayang"]  # Lists of choices kulob or hayang
C2 = random.choice(choices)  # Choose either kulob or hayang 
C3 = random.choice(choices)  # Choose randomly if its either kulob or hayang

# Display choices
print(f"P1 choose: {P1}")  # Print P1 choice
print(f"Computer 2 chose: {C2}")  # Print C2 choice
print(f"Computer 3 chose: {C3}")  # Print C3 choice

# Determine the winner
kulob_count = [P1, C2, C3].count("kulob")
# Counting on how many times kulob choose
hayang_count = [P1, C2, C3].count("hayang")
# counting on how many times hayang choose

# This is where the winner wins based on the counts 
if kulob_count > hayang_count:
    print("Kulob wins!")  # More kulob means kulob wins 
elif hayang_count > kulob_count:
    print("Hayang wins!")  # More hayang means hayang wins
else:
    print("It's a tie!")  # kung kulob or hayang its a tie
