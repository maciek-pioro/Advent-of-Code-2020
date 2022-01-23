
TURNS = 30000000

# starting_list = [1, 2, 3]
starting_list = [13, 0, 10, 12, 1, 5, 8]
occurrences = {n: (i+1) for i, n in enumerate(starting_list)}
last_number = starting_list[-1]
turn = len(starting_list) + 1
current_number = 0
while turn <= TURNS:
    # print(current_number)
    if occurrences.get(current_number) is None:
        next_number = 0
    else:
        next_number = turn - occurrences[current_number]
    occurrences[current_number] = turn
    last_number, current_number = current_number, next_number
    turn += 1
print(last_number)