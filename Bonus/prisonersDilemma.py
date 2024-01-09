import random

rounds = 10                 # number of rounds
options = ['T', 'S']        # options - testify or stay silent
jail_time = [0, 0]          # years in jail


# calc jail time
def calc_jail_time(player, computer):
    if player and computer:
        jail_time[0] += 2
        jail_time[1] += 2
        print("Both players testify. Each gets 2 years in prison.")

    elif player and not computer:
        jail_time[1] += 3
        print("The Player 1 testifies the Computer. Player 1 goes free, the Computer gets 3 years in prison.")

    elif not player and computer:
        jail_time[0] += 3
        print("The Computer betrays Player 1. The Computer goes free, Player 1 gets 3 years in prison.")

    else:
        jail_time[0] += 1
        jail_time[1] += 1
        print("Both players stay silent. Each gets 2 years in prison.")


# Main code
print("Prisoner's Dilemma Game")
print("Enter 'T' to testify or 'S' to Remain Silent.")


while rounds > 0:
    player = input("Choose (T/S): ").upper()
    computer = random.choice(options)

    if player == 'T':
        player_testifies = True
    else:
        player_testifies = False

    if computer == 'T':
        computer_testifies = True
    else:
        computer_testifies = False

    calc_jail_time(player_testifies, computer_testifies)

    rounds = rounds - 1

print(f'The Player get {jail_time[0]} years in jail.')
print(f'The Computer get {jail_time[1]} years in jail.')

# who serves more time and by how much?
# keep track of the picks for each round
# what if tehy enter a different input
