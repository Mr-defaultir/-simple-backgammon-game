import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, spaces):
    player += spaces
    if player > 100:
        player = 100
    elif player == 100:
        print("Congratulations! You Won!")
        return 0
    return player

def main():
    player1 = 0
    player2 = 0
    turn = 1
    
    while True:
        input("Press Enter to roll the dice")
        spaces = roll_dice()
        
        if turn == 1:
            player1 = move_player(player1, spaces)
            print("Player 1 moved to space", player1)
            if player1 == 0:
                break
            if spaces != 6:
                turn = 2
        else:
            player2 = move_player(player2, spaces)
            print("Player 2 moved to space", player2)
            if player2 == 0:
                break
            if spaces != 6:
                turn = 1

if name == "__main__":
    main()
