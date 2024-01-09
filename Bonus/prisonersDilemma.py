import random

rounds = 10                 # number of rounds
options = ['S', 'T']        # options
jail_time = [0, 0]          # years in jail


# calc jail time
def calc_jail_time(player, computer):
    if player and computer:
        jail_time[0] += 2
        jail_time[1] += 2
        print("Both players cooperate. Each gets 2 years in prison.")

    elif player and not computer:
        jail_time[1] += 5
        print("The Player 1 betrays the Computer. Player 1 goes free, the Computer gets 5 years in prison.")

    elif not player and computer:
        jail_time[0] += 5
        print("The Computer betrays Player 1. The Computer goes free, Player 1 gets 5 years in prison.")

    else:
        jail_time[0] += 4
        jail_time[1] += 4
        print("Both players betray each other. Each gets 4 years in prison.")


# Main code
print("Prisoner's Dilemma Game")
print("Enter 'S' to Snitch or 'Q' to Remain Quiet.")


while rounds > 0:
    player = input("Choose (S/Q): ").upper()
    computer = random.choice(options)

    if player == 'S':
        player_cooperate = True
    else:
        player_cooperate = False

    if computer == 'S':
        computer_cooperate = True
    else:
        computer_cooperate = False

    calc_jail_time(player_cooperate, computer_cooperate)

    rounds = rounds - 1

print(f'The Player get {jail_time[0]} years in jail.')
print(f'The Computer get {jail_time[1]} years in jail.')

# who serves more time and by how much?
# keep track of the picks for each round
