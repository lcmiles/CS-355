import random

def simulate_airline_one(num_trials):
    total_arrival_time = 0
    stranded_count = 0
    on_time_count = 0

    for _ in range(num_trials):
        #generate random flight times for each leg based on mean and standard dev
        flight_AB = max(min(random.normalvariate(4*60, 24), 5*60), 3*60)  #flight time AB
        flight_BC = max(min(random.normalvariate(4*60, 24), 5*60), 3*60)  #flight time BC
        flight_CD = max(min(random.normalvariate(3.5*60, 24), 4*60), 3*60)  #flight time CD

        #compute arrival times at B, C, and D
        arrival_B = 8*60 + flight_AB
        arrival_C = arrival_B + flight_BC
        arrival_D = arrival_C + flight_CD

        #check if stranded or not and consider it arrived on time if not
        if arrival_B > 12*60 or arrival_C > 17*60 or arrival_D > 20.5*60: #if a flight is too late to catch a connecting flight
            stranded_count += 1
        else:
            on_time_count += 1
            total_arrival_time += arrival_D

    average_arrival_time = total_arrival_time / on_time_count if on_time_count != 0 else 0 #calculate average arival time if not 0
    probability_on_time = on_time_count / num_trials #calculate probablity of arriving on time
    probability_stranded = stranded_count / num_trials #calculate probability of being stranded

    return average_arrival_time, probability_on_time, probability_stranded

def simulate_airline_two(num_trials):
    total_arrival_time = 0
    stranded_count = 0
    on_time_count = 0

    for _ in range(num_trials):
        #generate random flight times for each leg
        flight_AE = max(min(random.normalvariate(3.5*60, 48), 5*60), 3*60)  # Flight time AE
        flight_EF = max(min(random.normalvariate(4*60, 48), 5*60), 3*60)  # Flight time EF
        flight_FD = max(min(random.normalvariate(3.5*60, 48), 4*60), 3*60)  # Flight time FD

        #compute arrival times at E, F, and D
        arrival_E = 8*60 + flight_AE
        arrival_F = arrival_E + flight_EF
        arrival_D = arrival_F + flight_FD

        #check if stranded or not and consider it arrived on time if not
        if arrival_E > 12*60 or arrival_F > 16.5*60 or arrival_D > 20*60: #if a flight is too late to catch a connecting flight
            stranded_count += 1
        else:
            on_time_count += 1
            total_arrival_time += arrival_D

    average_arrival_time = total_arrival_time / on_time_count if on_time_count != 0 else 0
    probability_on_time = on_time_count / num_trials
    probability_stranded = stranded_count / num_trials

    return average_arrival_time, probability_on_time, probability_stranded

def main():
    num_trials = 10000

    #simulate airline one
    average_arrival_time_one, probability_on_time_one, probability_stranded_one = simulate_airline_one(num_trials)

    #simulate airline two
    average_arrival_time_two, probability_on_time_two, probability_stranded_two = simulate_airline_two(num_trials)

    print("Airline One:")
    print("Average Arrival Time:", average_arrival_time_one)
    print("Probability of Arrival by 21:00:", probability_on_time_one)
    print("Probability of Being Stranded:", probability_stranded_one)

    print("\nAirline Two:")
    print("Average Arrival Time:", average_arrival_time_two)
    print("Probability of Arrival by 20:30:", probability_on_time_two)
    print("Probability of Being Stranded:", probability_stranded_two)

if __name__ == "__main__":
    main()