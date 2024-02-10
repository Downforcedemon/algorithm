import random
import math

def rule1(x,n,upright):
    return((x + ((-1)**upright) * n)%n**2)

def rule2(x,n,upleft):
    return((x + ((-1)**upleft))%n**2)

def rule3(x,n,upleft):
    return((x + ((-1)**upleft * (-n + 1)))%n**2)



def fillsquare(square, entry_i, entry_j, howfull, n):
    while sum(math.isnan(i) for row in square for i in row) > howfull:
        where_we_can_go = []

        # Check for possible directions we can go and add them to the list
        if entry_i < (n - 1) and entry_j < (n - 1):
            where_we_can_go.append('down_right')
        if entry_i < (n - 1) and entry_j > 0:
            where_we_can_go.append('down_left')
        if entry_i > 0 and entry_j < (n - 1):
            where_we_can_go.append('up_right')
        if entry_i > 0 and entry_j > 0:
            where_we_can_go.append('up_left')

        # Randomly choose a direction to go
        where_to_go = random.choice(where_we_can_go)

        # Move to the new cell according to the chosen direction and apply the rule
        if where_to_go == 'up_right':
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_left':
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, False)
        elif where_to_go == 'up_left' and (entry_i + entry_j) != n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_right' and (entry_i + entry_j) != (n-2):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, False)
        elif where_to_go == 'up_left' and (entry_i + entry_j) == n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, True)
        elif where_to_go == 'down_right' and (entry_i + entry_j) == (n-2):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, False)

        # Update the current position
        entry_i, entry_j = new_entry_i, new_entry_j
