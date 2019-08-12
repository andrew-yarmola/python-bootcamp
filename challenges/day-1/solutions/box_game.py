import random

def individual_strategy(boxes_list, num_tries, num_to_find) :
    """ Implements the cycle strategy for a player to
    look for their number (num_to_find) in a list (boxes_list) with
    a limited number of tries (num_tries). The function
    returns True if the number is found, False otherwise.
    The algorithm treats boxes[i] as a permtuation and
    looks through the cycle containing i = person. """
    count = 0
    idx = num_to_find
    while count < num_tries :
        curr = boxes_list[idx]
        if curr == num_to_find :
            return True
        idx = curr
        count += 1
    return False

def play_box_game(num_ppl, num_tries, strategy, num_runs = 1) :
    """ A tool to simulate many random rounds of the box game.
    
    Parameters
    ----------
    num_ppl : int, required
        number of contestants.
    num_tries : int, required
        number of tries each contestant has to find their box.
    strategy : function(boxes, num_tries, person), required
        a strategy function to be used for each contestant.
    num_runs : int, optional
        number of times to play the game. Defaults to 1.

    Returns    
    ----------
    rate of victory with given strategy function """

    boxes = list(range(num_ppl))
    game_results = []
    while len(game_results) < num_runs + 1 :
        result = True
        # Shuffle the boxes once per game
        random.shuffle(boxes)
        for person in range(num_ppl) :
            result = result and strategy(boxes,num_tries,person)
            if result is False : # We have lost !!!
                break 
        game_results.append(result)
    return sum(game_results)/len(game_results)
