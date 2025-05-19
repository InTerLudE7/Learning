# A small python code to compute the probability of the joker-bomb appears in the a Dou-Di-Zhu game.
# idea: "https://www.bilibili.com/video/BV1PtVHzDETT"



from math import factorial
def nAr(n,r):
    if r < 0 or r > n:
        return 0
    return factorial(n)/factorial(n-r)


if __name__ == "__main__":
    print("Castlu Method:")
    print("\n Calculating the probability of persence of Joker-Pair appears in Player's hand.")
    print("\n Scenario 1: The joker pair is in DiZhu's hand..")
    
    P_A1 = nAr(20,2)/nAr(54,2)
    print("The Prob of Scenario 1: {}".format(P_A1))

    print("\n Scenario 2: The joker pair is in Peasant's hand..")
    P_A2 = 2*nAr(17,2)/nAr(54,2)

    print("The Prob of Scenario 2: {}".format(P_A2))

    print("The Prob of All three Scenarios: {}.".format(P_A1+P_A2))
# Check by Simulation:

import random
import argparse

def simulate_joker_probability(n_simulations=100000):
    count_same_player = 0

    for _ in range(n_simulations):
        deck = list(range(54))  # 0~51 are genearl cards，52 and 53 are Joker.
        random.shuffle(deck)

        # everybody get the 17 card. iteratively.
        hands = [deck[i*17:(i+1)*17] for i in range(3)]
        remaining = deck[51:]

        # Give the last 3 card to a random player.
        receiver = random.randint(0, 2)
        hands[receiver].extend(remaining)

        # Check Joker Pair in Hand
        for hand in hands:
            if 52 in hand and 53 in hand:
                count_same_player += 1
                break

    probability = count_same_player / n_simulations
    print(f"Estimated probability that both Jokers are in the same hand: {probability:.6f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate probability of both Jokers in one hand.")
    parser.add_argument("n_simulations", type=int, help="Number of simulations to run")
    args = parser.parse_args()
    simulate_joker_probability(args.n_simulations)

