"""Day 7: The Treachery of Whales.
Part 1: A whale is chasing the ship, and crabs want to form a line (in tiny
submarines), so we decide to help the crabs line up. Find the point which is
closest to all the crabs, then calculate how much fuel is needed to get there.
One horizontal movement takes one unit of fuel.
"""
import statistics

def find_fuel_used(positions):
    """The closest point to all other points is simply the median."""
    closest_pt = statistics.median(positions)
    fuel = sum(abs(pt-closest_pt) for pt in positions)
    return int(fuel)


"""Part 2: Of course, turns out it wasn't that simple. After each step, the
fuel cost increases by 1. For example, 1 step costs 1, the next step costs 2,
the next costs 3, etc.
"""

def find_actual_fuel_used(positions):
    """To find the fuel used between each point, we use the infinite series:
    sum(1 to n) k = n*(n+1)/2.
    We go through all possible points the crabs could be at, and then find the
    minimum 
    """
    all_points = range(min(positions), max(positions)+1)
    fuel = min([sum((abs(pt-guess)*(abs(pt-guess)+1))/2 for pt in positions)
                for guess in all_points])
    return int(fuel)


with open('inputs/input_day_7.txt') as f:
    crab_file = f.read()
    crab_file  = crab_file.split(',')
    positions = [int(x) for x in crab_file]
    print(f'The answer to Part 1 is {find_fuel_used(positions)}.')
    print(f'The answer to Part 2 is {find_actual_fuel_used(positions)}.')