
num_of_people = 23

def people_to_probability(num_of_people):
    probability_not_share = 1
    for person in range(0, num_of_people):
        probability_not_share = probability_not_share*((366-person)/366)
    probability_share = 1 - probability_not_share
    return probability_share
    

def probability_to_people(probability):
    for group in range(2, 100):
        test_probability = people_to_probability(group)
        if 100*test_probability >= probability:
            return group
        

if __name__ == "__main__":

    people_in_room = int(input("How many people are in this room?\n:"))   
    print(f"The probability that there are people who share the same birthday in a room of {people_in_room} people is {100*people_to_probability(people_in_room):.2f}%")

    desired_probability = float(input("What is your desired probability to have a shared birthday?\n:"))
    print(f"In order to have a probability of at least {desired_probability}%, there must be {probability_to_people(desired_probability)} people in the room.")