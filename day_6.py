"""Day 6: Lantern Fish.
Part 1: You want to model the growth rate of the lantern fish population.
After 7 days, a lantern fish will spawn a new lantern fish. Lantern fishes
will have different numbers of days before they are due to spawn, so we can
keep track of the fish by giving them a number corresponding to their days
left to respawn. A newly spawned fish, however, will take 2 more days before
it can respawn, i.e. 8 days.
Given an initial starting configuration of lantern fish, find how many there
would be after 80 days.
"""

lantern_fish_init = [3,4,3,1,2]

def find_fish_population(lantern_fish_pop):
    for day in range(80):
        for fish in lantern_fish_pop:
            if fish==0:
                lantern_fish_pop.append(9)
        lantern_fish_pop = [fish-1 if fish>0 else 6 for fish in lantern_fish_pop]
    return len(lantern_fish_pop)

"""Part 2: How about after 256 days?
"""

def find_big_fish_population(lantern_fish_pop):
    """Well, this exponential problem needs more than a simple for loop.
    We'll pick the easiest solution: keep track of the number of fish
    with each number of days left (days = 0 to 8).
    """
    # Create dictionary
    counters = dict.fromkeys([f'{i} days' for i in range(0,9)], 0)
    # Get initial fish counts at each day
    for i in range(0,9):
        counters[f"{i} days"] += len([x for x in lantern_fish_pop if x==i])
    # Cycle through all 256 days
    for i in range(256):
        num_0 = counters['0 days']
        counters['0 days'] = counters['1 days']
        counters['1 days'] = counters['2 days']
        counters['2 days'] = counters['3 days']
        counters['3 days'] = counters['4 days']
        counters['4 days'] = counters['5 days']
        counters['5 days'] = counters['6 days']
        counters['6 days'] = counters['7 days']+num_0
        counters['7 days'] = counters['8 days']
        counters['8 days'] = num_0
    return sum(counters.values())

with open('inputs/input_day_6.txt') as f:
    fish_file = f.read()
    fish_file  = fish_file.split(',')
    lantern_fish = [int(x) for x in fish_file]
    print(f'The answer to Part 1 is: {find_fish_population(lantern_fish)}.')
    print(f'The answer to Part 2 is: {find_big_fish_population(lantern_fish)}.')