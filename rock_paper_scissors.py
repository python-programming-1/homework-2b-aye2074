while True:
    import random

    r = 'rock'
    p = 'paper'
    s = 'scissors'
    y = 'yes'
    n = 'no'
    sc = 'score'

    beatcomputer = [r, p, s]
    rc = random.choice(beatcomputer)

    print("make a move! (r/s/p)")
    player_move = input()

    def give_me_player_string(player_input):
        if player_move == 'r':
            return 'rock'
        if player_move == 's':
            return 'scissors'
        if player_move == 'p':
            return'paper'

    print("You chose %s and the computer chose %s" %
          (str(give_me_player_string(player_move)), rc))

    x = 0
    y = 0

    if rc == 'rock':
        if give_me_player_string(player_move) == 'scissors':
            print("You Lose!")
            y = y + 1
        elif give_me_player_string(player_move) == 'paper':
            print("You Win!")
            x = x + 1

    if rc == 'paper':
        if give_me_player_string(player_move) == 'scissors':
            print("You win!")
            x = x + 1
        elif give_me_player_string(player_move) == 'rock':
            print("You Lose!")
            y = y + 1

    if rc == 'scissors':
        if give_me_player_string(player_move) == 'rock':
            print("You Win!")
            x = x + 1
        elif give_me_player_string(player_move) == 'paper':
            print("You Lose!")
            y = y + 1

    player_score = input()
    if player_score == 'sc':
        print("Human : %d, Computer : %d" % (x, y))

    print("Do you want to play again? (y/n)")
    player_answer = input()
    if player_answer == 'n':
        print("Thanks bye!")
        break
    if player_answer == 'y':
        continue
