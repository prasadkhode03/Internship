# Pseudocode for Forward Checking in CSP

# Backtrack(assignment):
#     if assignment is complete:
#         return assignment

#     var ← select an unassigned variable
#     for each value in domain[var]:
#         if value is consistent with assignment:
#             assignment[var] = value
#             inferences = forward_check(var, value, assignment)
#             if inferences ≠ failure:
#                 result ← Backtrack(assignment)
#                 if result ≠ failure:
#                     return result
#             undo inferences
#             remove var from assignment
#     return failure


def not_equal(x, y):
    return x != y

def backtrack(assignment, variables, domains, constraints):
    if len(assignment) == len(variables):
        return assignment

    var = select_unassigned_variable(assignment, variables)

    for value in domains[var]:
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value

            # Make a copy of domains to track changes
            local_domains = {v: list(domains[v]) for v in variables}
            inferences = forward_check(var, value, assignment, local_domains, constraints)

            if inferences is not None:
                result = backtrack(assignment, variables, local_domains, constraints)
                if result is not None:
                    return result

            del assignment[var]  # Backtrack

    return None

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

def forward_check(var, value, assignment, domains, constraints):
    inferences = {}

    for (v1, v2) in constraints:
        neighbor = None
        if v1 == var:
            neighbor = v2
        elif v2 == var:
            neighbor = v1

        if neighbor and neighbor not in assignment:
            to_remove = []
            for val in domains[neighbor]:
                if not constraints[(v1, v2)](value if var == v1 else val, val if var == v1 else value):
                    to_remove.append(val)

            if to_remove:
                for val in to_remove:
                    domains[neighbor].remove(val)
                inferences[neighbor] = to_remove

            if not domains[neighbor]:  # Domain wiped out
                return None

    return inferences

# Define variables and domains
variables = ['WA', 'NT', 'SA']
domains = {v: ['red', 'green', 'blue'] for v in variables}

# Define constraints using named functions instead of lambdas
constraints = {
    ('WA', 'NT'): not_equal,
    ('WA', 'SA'): not_equal,
    ('NT', 'SA'): not_equal
}

# Solve CSP
solution = backtrack({}, variables, domains, constraints)
print(solution)


