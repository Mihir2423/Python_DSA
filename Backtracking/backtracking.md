# Backtracking

-> Backtracking is an algorithmic - technique
-> Solving problems recursively
-> Try to build the solution increamentally
-> Remove those solutions that fail to satisfy the constraints of the problem


# Pseudo Code to get out of a maze

junction -> where we take decision

function backtrack(junction):
    if isExit:
        return True
    for each direction of junction:
        if backtrack(next-junction):
            return True
    return False