import random  # We need this to generate random numbers for the lottery results

# Initialize counters for wins, partial wins, and losses
total_daug, total_hapit_ra, total_pilde = 0, 0, 0

# We'll play the game for 3 rounds
for round_number in range(1, 4):
    print(f"Round {round_number}")  # Inform the player which round it is
    
    # Get the player's bet and convert it to a list of integers
    patad = list(map(int, input("Enter your Bet (space-separated numbers): ").split()))
    
    # Generate the lottery result by picking 3 unique random numbers between 2 and 4
    resulta = random.sample(range(2, 5), 3)
    print(f"Lottery resulta: {' '.join(map(str, resulta))}")  # Show the lottery result
    
    # Determine if the player won, nearly won, or lost
    if patad == resulta:
        outcome, daug, hapit_ra, pilde = "Daug ka!", 1, 0, 0  # Exact match
    elif sorted(patad) == sorted(resulta):
        outcome, daug, hapit_ra, pilde = "Hapit ra madaug!", 0, 1, 0  # Same numbers, different order
    else:
        outcome, daug, hapit_ra, pilde = "Luoya pilde man!", 0, 0, 1  # No match
    
    # Update the win/lose counters
    total_daug += daug
    total_hapit_ra += hapit_ra
    total_pilde += pilde
    
    # Inform the player of the outcome
    print(outcome, "\n")

# Display the final results
print("Game Over!")
print(f"Total Daug: {total_daug}\nTotal Hapit_ra: {total_hapit_ra}\nTotal Pilde: {total_pilde}")
