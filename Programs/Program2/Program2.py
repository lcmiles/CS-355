import random
import matplotlib.pyplot as plt
import sys

sys.stdout = open('output.txt', 'w') #redirect print outputs to a text file for easier reading of results

#function for the first type of shuffling
def shuffle1(deck):
    n = len(deck) // 2 #determines the half-index of the deck
    shuffled_deck = [] #creates an empty deck to contain shuffled deck
    for i in range(n): #iterates from 0 to n, or from the beginning of the deck to the halfway point
        shuffled_deck.append(deck[i]) #add card from first half of the deck
        shuffled_deck.append(deck[i + n]) #add card from second half of the deck
    return shuffled_deck

#function for the second type of shuffling
def shuffle2(deck):
    n = len(deck) // 2
    shuffled_deck = []
    for i in range(n):
        shuffled_deck.append(deck[i + n])
        shuffled_deck.append(deck[i])
    return shuffled_deck

def shuffle3(deck):
    n = len(deck)
    shuffled_deck = []
    half1 = deck[:n//2]  #split the deck into two halves
    half2 = deck[n//2:]
    
    while half1 and half2:  #while both halves are not empty
        if random.random() < 0.5:  #pick randomly from either half with equal probability
            shuffled_deck.append(half1.pop(0))  #pop and append from the first half
        else:
            shuffled_deck.append(half2.pop(0))  #pop and append from the second half
    
    shuffled_deck.extend(half1 if half1 else half2)  #add the remaining cards from the non-empty half
    
    return shuffled_deck

def shuffle4(deck):
    n = len(deck)
    shuffled_deck = []
    half1 = deck[:n//2]  #split the deck into two halves
    half2 = deck[n//2:]
    
    while half1 and half2:  #while both halves are not empty
        prob_half1 = len(half1) / (len(half1) + len(half2))  #probability to pick from the first half
        if random.random() < prob_half1:  #randomly decide whether to pick from the first half
            shuffled_deck.append(half1.pop(0))  #pop and append from the first half
        else:
            shuffled_deck.append(half2.pop(0))  #pop and append from the second half
    
    shuffled_deck.extend(half1 if half1 else half2)  #add the remaining cards from the non-empty half
    
    return shuffled_deck

#function to calculate the correlation coefficient
def calculateR(deck):
    n = len(deck)
    sumi = n * (n + 1) // 2  #sum of integers from 1 to n
    sumsq = n * (n + 1) * (2 * n + 1) // 6  #sum of squares of integers from 1 to n
    sqsum = sumi * sumi  #square of sum of integers from 1 to n
    sum_product = sum(i * (index + 1) for index, i in enumerate(deck))  #sum of index times card value
    r = (n * sum_product - sqsum) / (n * sumsq - sqsum)  #pearson's correlation coefficient formula
    return r

#function to perform the first run of shuffling 
def performFirstRun(num_cards):
    deck = list(range(1, num_cards + 1))  #create a deck of cards
    r_values = [] #list to store r values after each shuffle

    for i in range(15):  #perform 15 shuffles
        deck = shuffle1(deck)  #shuffle using the first shuffle method
        r = calculateR(deck)  
        r_values.append((i + 1, r, deck.copy()))  #store shuffle number, correlation coefficient, and deck order

    print(f"1st Run With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}')  #print shuffle number, correlation coefficient, and deck order
        print("")

    plt.plot([i[0] for i in r_values], [r[1] for r in r_values], marker='o', label=f'1st Run: {num_cards} Cards')  #plot the r values (y) vs shuffle number (x)

    for i, r, order in r_values:
        color = 'blue' if num_cards == 52 else 'orange'  #color based on the number of cards
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color)  #annotate the points with correlation coefficient

#function to perform the second run of shuffling 
def performSecondRun(num_cards):
    deck = list(range(1, num_cards + 1))
    r_values = []

    for i in range(15):
        deck = shuffle2(deck)
        r = calculateR(deck)
        r_values.append((i + 1, r, deck.copy()))

    print(f"2nd Run With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}')
        print("")
        
    plt.plot([i[0] for i in r_values], [r[1] for r in r_values], marker='o', label=f'2nd Run: {num_cards} Cards')

    for i, r, order in r_values:
        color = 'green' if num_cards == 52 else 'red'
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color)

#function to perform the third run of shuffling 
def performThirdRun(num_cards):
    deck = list(range(1, num_cards + 1))
    r_values = []

    for i in range(15):
        deck = shuffle3(deck)
        r = calculateR(deck)
        r_values.append((i + 1, r, deck.copy()))

    print(f"3rd Run With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}')
        print("")
        
    plt.plot([i[0] for i in r_values], [r[1] for r in r_values], marker='o', label=f'3rd Run: {num_cards} Cards')

    for i, r, order in r_values:
        color = 'purple' if num_cards == 52 else 'brown'
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color)
        
#function to perform the fourth run of shuffling 
def performFourthRun(num_cards):
    deck = list(range(1, num_cards + 1))
    r_values = []

    for i in range(15):
        deck = shuffle4(deck)
        r = calculateR(deck)
        r_values.append((i + 1, r, deck.copy()))

    print(f"4th Run With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}')
        print("")
        
    plt.plot([i[0] for i in r_values], [r[1] for r in r_values], marker='o', label=f'4th Run: {num_cards} Cards')

    for i, r, order in r_values:
        color = 'cyan' if num_cards == 52 else 'pink'
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color)
        
def main():
    performFirstRun(52)
    performFirstRun(104)
    performSecondRun(52)
    performSecondRun(104)
    performThirdRun(52)
    performThirdRun(104)
    performFourthRun(52)
    performFourthRun(104)
    
    plt.xlabel('Number of Shuffles')
    plt.ylabel('Value of r')
    plt.title('Correlation Coefficient over 15 shuffles')
    plt.legend()
    plt.tight_layout()
    plt.show()

main()