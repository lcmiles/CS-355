import matplotlib.pyplot as plt

def shuffle(deck):
    n = len(deck) // 2
    shuffled_deck = []
    for i in range(n):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[i + n])
    return shuffled_deck

def calculate_r(deck):
    n = len(deck)
    sumi = n * (n + 1) // 2
    sumsq = n * (n + 1) * (2 * n + 1) // 6
    sqsum = sumi * sumi
    sum_product = sum(i * (index + 1) for index, i in enumerate(deck))
    r = (n * sum_product - sqsum) / (n * sumsq - sqsum)    
    return r

def perform_experiment(num_cards):
    deck = list(range(1, num_cards + 1))
    r_values = []

    for i in range(15):
        deck = shuffle(deck)
        r = calculate_r(deck)
        r_values.append((i + 1, r, deck.copy()))

    print(f"With {num_cards} Cards")
    print("")

    for i, r, order in r_values:
        print(f'Shuffle {i}: r = {r:.4f}, order = {order}')
        print("")

    for i, r, order in r_values:
        color = 'blue' if num_cards == 52 else 'orange'
        plt.annotate(f'{r:.4f}', (i, r), xytext=(5, 5), textcoords='offset points', fontsize=8, color=color)

    plt.plot([r[0] for r in r_values], [r[1] for r in r_values], marker='o', label=f'{num_cards} Cards')

def main():
    perform_experiment(52)
    perform_experiment(104)

    plt.xlabel('Number of Shuffles')
    plt.ylabel('Value of r')
    plt.title('Value of r over 15 shuffles')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
