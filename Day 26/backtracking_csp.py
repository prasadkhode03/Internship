# Pseudocode for Backtracking Search in CSP

# Backtrack(assignment):
#     if assignment is complete:
#         return assignment

#     var ← select an unassigned variable
#     for each value in var.domain:
#         if value is consistent with assignment:
#             add {var = value} to assignment
#             result ← Backtrack(assignment)
#             if result ≠ failure:
#                 return result
#             remove {var = value} from assignment
#     return failure


def backtrack(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment, variables)

    for value in domains[var]:
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value
            result = backtrack(assignment, variables, domains, constraints)
            if result is not None:
                return result
            del assignment[var]  # Backtrack

    return None  # Failure

def select_unassigned_variable(assignment, variables):
    for var in variables:
        if var not in assignment:
            return var

def is_consistent(var, value, assignment, constraints):
    for (v1, v2) in constraints:
        if v1 == var and v2 in assignment:
            if not constraints[(v1, v2)](value, assignment[v2]):
                return False
        elif v2 == var and v1 in assignment:
            if not constraints[(v1, v2)](assignment[v1], value):
                return False
    return True

variables = ['WA', 'NT', 'SA']
domains = {v: ['red', 'green', 'blue'] for v in variables}
constraints = {
    ('WA', 'NT'): lambda x, y: x != y,
    ('WA', 'SA'): lambda x, y: x != y,
    ('NT', 'SA'): lambda x, y: x != y
}

solution = backtrack({}, variables, domains, constraints)
print(solution)
