import matplotlib.pyplot as plt

#function for the first type of shuffling
def shuffle1(deck):
    n = len(deck) // 2 #determines the half-index of the deck
    shuffled_deck = [] #creates an empty deck to contain shuffled deck
    for i in range(n): #iterates from 0 to n, or from the beginning of the deck to the halfway point
        shuffled_deck.append(deck[i]) #adds a card from the first half of the deck
        shuffled_deck.append(deck[i + n]) #adds a card from the second half of the deck
    return shuffled_deck

#function for the second type of shuffling
def shuffle2(deck):
    n = len(deck) // 2
    shuffled_deck = []
    for i in range(n):
        shuffled_deck.append(deck[i + n])
        shuffled_deck.append(deck[i])
    return shuffled_deck

#function to calculate the correlation coeffecient
def calculateR(deck):
    n = len(deck)
    sumi = n * (n + 1) // 2 #sums the numbers from 1 to n
    sumsq = n * (n + 1) * (2 * n + 1) // 6 #sums the square of the numbers from 1 to n
    sqsum = sumi * sumi #square of sumi
    sum_product = sum(i * (index + 1) for index, i in enumerate(deck)) #gets index and value of the card, then multiplies the index by the of the value of card, then sums all
    r = (n * sum_product - sqsum) / (n * sumsq - sqsum) #formula for Pearson's correlation coeffecient
    return r

#function to perform the first run of shuffling 
def performFirstRun(num_cards):
    deck = list(range(1, num_cards + 1)) #create a deck of num_cards cards
    r_values = [] #list to store r values after each shuffle

    for i in range(15): #perform 15 shuffles
        deck = shuffle1(deck) #shuffle using first shuffle type
        r = calculateR(deck)
        r_values.append((i + 1, r, deck.copy())) #add the shuffle number, r value, and a copy of the deck to the list

    print(f"1st Run With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}') #print the shuffle number, r value, and deck to the terminal
        print("")

    plt.plot([i[0] for i in r_values], [r[1] for r in r_values], marker='o', label=f'1st Run: {num_cards} Cards') #plot the r values (y) vs shuffle number (x)

    for i, r, order in r_values:
        color = 'blue' if num_cards == 52 else 'orange' #color based on the number of cards
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color) #annotate the points with the r values

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

def main():
    performFirstRun(52)
    performFirstRun(104)
    performSecondRun(52)
    performSecondRun(104)
    
    plt.xlabel('Number of Shuffles')
    plt.ylabel('Value of r')
    plt.title('Correlation Coeffecient over 15 shuffles')
    plt.legend()
    plt.tight_layout()
    plt.show()

main()