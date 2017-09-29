
EASY_LEVEL = 'easy'
MEDIUM_LEVEL = 'medium'
HARD_LEVEL = 'hard'
DIFFICULTY_LEVELS = [EASY_LEVEL, MEDIUM_LEVEL, HARD_LEVEL]
MAX_NUMBER_OF_GUESSES = 5


def get_question_prompt(difficulty):
    """
    Input: difficulty level - easy, medium, hard
    Output: question prompt for difficulty level
    Behavior: returns question prompt
    """
    beginning = "The current paragraph reads as such:\n"
    if difficulty == EASY_LEVEL:
        return  beginning + "Let's count! zero, %s, %s, %s, %s, five, six..."
    elif difficulty == MEDIUM_LEVEL:
        return beginning + "Let's count backward! six, five, %s, %s, %s, %s, zero"
    elif difficulty == HARD_LEVEL:
        return beginning + "Let's count odd numbers! zero, %s, two, %s, four, %s, six, %s, eight..."
    else:
        raise "Invalid difficulty", difficulty

def get_answer_list(difficulty):
    """
    Input: difficulty level - easy, medium, hard
    Output: list of answers for problems
    Behavior: return list of answers for problems
    """
    if difficulty == EASY_LEVEL:
        return ['one', 'two', 'three', 'four']
    elif difficulty == MEDIUM_LEVEL:
        return ['four', 'three', 'two', 'one']
    elif difficulty == HARD_LEVEL:
        return ['one', 'three', 'five', 'seven']
    else :
        raise "Invalid difficulty", difficulty

def after_game_result(num_user_guesses):
    """
    Input: number of user guesses
    Output: no output - only print statement
    Behavior: user gets notified win or lose dependng on number of user guesses meeting MAX NUMBER OF GUESSES
    """
    if num_user_guesses >= MAX_NUMBER_OF_GUESSES:
        print "You've failed too many straight guesses!  Game over!"
    else:
        print "you won!"

def game_start_notification(difficulty):
    """
    Input: difficulty level - easy, medium, hard
    Output: no output - only print statement
    Behavior: user gets notified which difficulty and how many guesses user gets
    """
    print "You've chosen %s!" %difficulty
    print "You will get %s guesses per problem" %MAX_NUMBER_OF_GUESSES


def play_game(difficulty):
    """
    Input: difficulty level - easy, medium, hard
    Output: no output
    Behavior: plays game by guessing answers
    """
    assert(difficulty in DIFFICULTY_LEVELS), "function precondition not satisfied for difficulty level"
    game_start_notification(difficulty)
    num_of_guesses_tried = 0

    ANSWER_LIST = get_answer_list(difficulty)
    user_answer = ['__1__', '__2__', '__3__', '__4__']
    Question_Prompt = get_question_prompt(difficulty)

    current_problem_number = 1

    while num_of_guesses_tried < MAX_NUMBER_OF_GUESSES and current_problem_number <= len(ANSWER_LIST):
        print Question_Prompt %(user_answer[0], user_answer[1], user_answer[2], user_answer[3])
        user_problem_answer = raw_input("What should be substituted in for %s?\n" %user_answer[current_problem_number-1])
        if user_problem_answer == ANSWER_LIST[current_problem_number-1]:
            print "Correct!"
            user_answer[current_problem_number-1] = user_problem_answer
            current_problem_number += 1
        else :
            num_of_guesses_tried += 1
            print "That isn't the correct answer!  Let's try again; you have %s try(s) left!" %(MAX_NUMBER_OF_GUESSES-num_of_guesses_tried)
    
    after_game_result(num_of_guesses_tried)        

def main():
    """
    Input: no input
    Output: no output
    Behavior: the function takes user chosen difficulty input (easy, medium, hard) and then play game with that difficulty.
            If user input doesn't select difficulty, ask user for difficulty input again.
    """
    while True:
        UserChosenDifficulty = raw_input('Select a game difficulty : easy, medium, and hard.\n')
        if UserChosenDifficulty in DIFFICULTY_LEVELS:
            play_game(UserChosenDifficulty)
            break # once you play game, it is over
        else:
            print "That's not an option!"


if __name__ == "__main__":
    main()