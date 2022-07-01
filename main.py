import numpy as np
import random
import time

def read_input():
    # Read input file
    with open("input.txt") as file:
        lines = file.readlines()

    # Convert to integers
    sim_data = []
    for line in lines:
        timestep = []
        for entry in line.strip("\n").split(";"):
            # convert binary string to int
            timestep += [int(entry, 2)]

        sim_data += [timestep]

    # Or a dirty oneliner
    # sim_data = [[int(entry,2) for entry in line.strip("\n").split(";")] for line in lines]

    sim_data = np.array(sim_data)
    # print(sim_data)
    return sim_data

def IFF(step):
    # Count number of odd occurences
    number_of_odd = sum(step%2)
    number_of_even = len(step) - number_of_odd

    return number_of_odd>number_of_even

def shoot_missile():

    PK = random.random()     # generate Kill Probability

    if PK<0.8:
        return True
    elif PK==0.8:
        print("Attention: undetermined probability")

    return False


def simulate(sim_data, show_log=True):
    logs = ""
    for i,step in enumerate(sim_data):

        log = f"t={i+1} s  "

        # Determine if Friend or Foe
        foe = IFF(step)

        # Check if Friend or Foe
        if foe:
            log += "Foe detected! Missile was fired"
            if shoot_missile():
                log += " and hit confirmed"
            else:
                log += " but missed"

        # Friend
        else:
            log += "Friend detected. No action undertaken."

        # Real time simulation
        time.sleep(1)
        if show_log:
            print(log)

        logs += log + "\n"

    return logs


# Run code
data = read_input()
simulate(data)



