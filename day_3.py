"""Day 3: Binary Diagnostic.
Part 1: Find the power consumption using the diagnostic report. Use the
diagnostic report to generate two new binary numbers: the gamma rate and
epsilon rate. The power consumption is found by multiplying these numbers.
The gamma rate is given by the most common bit in each column (starting
with column 0), and the epsilon rate is given by the least common bit in each
column.
"""
from collections import Counter

def get_power_consumption(diag_report):
    def get_element(cols, most_or_least):
        if most_or_least=='most':
            i = 0
        elif most_or_least=='least':
            i = 1
        else:
            raise ValueError("most_or_least must be 'most' or 'least'.")
        el = int(''.join(Counter(x).most_common()[i][0] for x in cols), 2)
        return el
    # Make sure length of all rows is the same
    iter_diag = iter(diag_report)
    len_elements = len(next(iter_diag))
    if not all(len(l)==len_elements for l in iter_diag):
        raise ValueError('Elements of diag_report not the same length.')
    # Transform data into columns
    diag_cols = []
    for i in range(len(diag_report[0])):
        diag_cols.append(''.join(x[i] for x in diag_report))
    gamma = get_element(diag_cols, 'most')
    epsilon = get_element(diag_cols, 'least')
    return gamma*epsilon

"""Part 2: Next, you need to verify the life support rating, which can be
determined multiplying the oxygen generator rating by the CO2 scrubber rating.
These values can be found in the diagnostics report.
Start with the full list of binary numbers from your diagnostic report and
consider just the first bit of those numbers. Then:
    - Keep only the numbers selected by the bit criteria for the type of
    rating value for which you are searching. Discard numbers that don't
    match the bit criteria.
    - If only one number left, stop; this is the rating value for which you
    are searching.
    - Otherwise, repeat the process considering the next bit to the right.
The bit criteria depends on which type of rating value you want to find:
    - To find the oxygen generator rating, determine the most common value
    (0 or 1) in the current bit position. If 0 and 1 are equally common, keep
    values with a 1 in the position being considered.
    - To find the CO2 scrubber rating, determing the least common value (0 or
    1) in the current bit position. If 0 and 1 are equally common, keep
    values with a 0 in the position being considered.
"""

def get_life_support_rating(diag_report):
    # Make sure length of all rows is the same
    iter_diag = iter(diag_report)
    len_elements = len(next(iter_diag))
    if not all(len(l)==len_elements for l in iter_diag):
        raise ValueError('Elements of diag_report not the same length.')

    def get_rating(diag_report, o2_or_co2):
        if o2_or_co2=='O2':
            common_num = 1
            common_index = 0
        elif o2_or_co2=='CO2':
            common_num = 0
            common_index = 1
        for i in range(len(diag_report[0])):
            if len(diag_report)==1:
                return diag_report
            diag_col = ''.join(x[i] for x in diag_report)
            ranked = Counter(str(diag_col)).most_common()
            if ranked[0][1]==ranked[1][1]:
                common = common_num
            else:
                common = Counter(str(diag_col)).most_common()[common_index][0]
            diag_report = [item for item in diag_report if item[i]==str(common)]
        return diag_report
    
    oxygen = int(get_rating(diag_report, 'O2')[0], 2)
    carbon_dioxide = int(get_rating(diag_report, 'CO2')[0], 2)
    life_support_rating = oxygen*carbon_dioxide
    return life_support_rating
    
with open('inputs/input_day_3.txt') as f:
    diag_file = f.read()
    diag_report = diag_file.splitlines()
    print(f"The answer to Part 1 is: {get_power_consumption(diag_report)}.")
    print(f"The answer to Part 2 is: {get_life_support_rating(diag_report)}.")
