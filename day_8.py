"""Day 8: Seven Segment Search.
Okay, this one is long. We need to decode the seven-segment display of the
submaine. 1, 4, 7 and 8 have a unique number of segments that are used
(2, 4, 3 and 7).
Determine the number of times 1, 4, 7 and 8 appear in the four digit output
value.
"""

def get_value_count(signal):
    signal = [s.split(' | ') for s in signal]
    signal = [[x[0].split(), x[1].split()] for x in signal] 
    lengths = [len(item) for sublist in signal for item in sublist[1]]
    values = [2, 4, 3, 7]
    count = len([x for x in lengths if x in values])
    return count

"""Part 2: Using deduction, solve the pattern and find the four numbers in each
entry. Sum these numbers and report the value.
"""

def get_sum_of_outputs(signal):
    """To solve this, we need to get the input patterns with lengths 2 and 4
    and use these to determine which numbers correspond to outputs of lengths
    5 and 6.
    If outputs with length 5 have 2 elements in common with patterns of length
    2, the number is 3. If 2 in common with patterns of length 4, the number
    is 2. Otherwise, number is 5. For outputs of length 6, 1 element in
    common with patterns of length 2 is 6, 4 with patterns of length 4 is 9
    and otherwise 0.
    """
    final_numbers = []
    for sig in signal:
        pattern, output = sig.strip().split('|')
        output = output.split()
        decode = {len(p):set(p) for p in pattern.split() if len(p) in (2,4)}
        decoded_num = ''
        for num in output:
            if len(num)==2:
                decoded_num += '1'
            elif len(num)==3:
                decoded_num += '7'
            elif len(num)==4:
                decoded_num += '4'
            elif len(num)==7:
                decoded_num += '8'
            elif len(num)==5:
                if len(set(num) & decode[2])==2:
                    decoded_num += '3'
                elif len(set(num) & decode[4])==2:
                    decoded_num += '2'
                else:
                    decoded_num += '5'
            elif len(num)==6:
                if len(set(num) & decode[2])==1:
                    decoded_num += '6'
                elif len(set(num) & decode[4])==4:
                    decoded_num += '9'
                else:
                    decoded_num += '0'
        final_numbers.append(int(decoded_num))
    return sum(final_numbers)


with open('inputs/input_day_8.txt') as f:
    signal_file = f.read()
    signal = signal_file.splitlines()
    print(f'The answer to Part 1 is {get_value_count(signal)}.')
    print(f'The answer to Part 2 is {get_sum_of_outputs(signal)}.')