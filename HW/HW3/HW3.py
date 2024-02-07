import itertools
import random

def isFullHouse(hand): #function used to check if a hand is a full house
    values = [card[0] for card in hand] #define the values for each card in the hand
    value_counts = {value:values.count(value) for value in set(values)} #count the occurences of each value
    return sorted(value_counts.values()) == [2,3] #if there are 2 unique counts of card values, one with 2 and the other with 3, then return the boolean

def countFullHouseHands(num_trials):
    deck = list(itertools.product(['2','3','4','5','6','7','8','9','10','J','Q','K','A'],['H','D','C','S'])) #generate a list representing a deck of 52 cards
    fh_count  = 0 #initialize a count for the hands containing a full house
    for _ in range(num_trials): #loop for the number of trials
        shuffled_deck = deck[:] #create duplicate deck to shuffle
        random.shuffle(shuffled_deck) #shuffle the deck
        hand = shuffled_deck[:5] #select 5 cards from the deck
        if isFullHouse(hand): #if the hand is a full house
            fh_count += 1 #increment full house count
    return fh_count / num_trials #calculate and return probability

num_trials = 1000000
probability = countFullHouseHands(num_trials)
print("Probability of getting a full house in a 5-card poker hand after", num_trials, "trials:", probability)