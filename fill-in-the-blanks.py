def play_game(difficulty):
    print "You've chosen %s!" %difficulty
    
    remaining_guesses = 5
    print "You will get %s guesses per problem" %remaining_guesses

    ANSWER_LIST = ['one', 'two', 'three', 'four']
    user_answer = ['__1__', '__2__', '__3__', '__4__']

    current_problem_number = 1

    while remaining_guesses > 0 and current_problem_number <=4:
        print "The current paragraph reads as such:\n Let's count! zero, %s, %s, %s, %s, five, six..." %(user_answer[0], user_answer[1], user_answer[2], user_answer[3])
        user_problem_answer = raw_input("What should be substituted in for %s?\n" %user_answer[current_problem_number-1])
        if user_problem_answer == ANSWER_LIST[current_problem_number-1]:
            print "Correct!"
            user_answer[current_problem_number-1] = user_problem_answer
            current_problem_number += 1
        else :
            remaining_guesses -= 1
            print "That isn't the correct answer!  Let's try again; you have %s try(s) left!" % remaining_guesses
    
    
    if current_problem_number == len(ANSWER_LIST) + 1:
        print "You won!"
    else : 
        print "You've failed too many straight guesses!  Game over!"
        

def main():
    while True:
        ChosenDifficulty = raw_input('Select a game difficulty : easy, medium, and hard.\n')
        if ChosenDifficulty in ['easy', 'medium', 'hard']:
            play_game(ChosenDifficulty)
            break
        else:
            print "That's not an option!"


if __name__ == "__main__":
    main()