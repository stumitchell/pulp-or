#!/usr/bin/env python
# @(#) $Jeannot: test2.py,v 1.16 2004/03/20 17:06:54 js Exp $

# This example is a PuLP rendition of the todd.mod problem included in the GLPK
# 4.4 distribution. It's a hard knapsack problem.

# Import PuLP modeler functions
from pulp import *

# Import math functions
import math

# A new LP problem
prob = LpProblem("test2", LpMaximize)

# Parameters
# Size of the problem
n = 15
k = math.floor(math.log(n) / math.log(2))

# A vector of n binary variables
x = LpVariable.matrix("x", list(range(n)), lowBound=0, upBound=1, cat=LpInteger)

# A vector of weights
a = [pow(2, k + n + 1) + pow(2, k + n + 1 - j) + 1 for j in range(1, n + 1)]
# The maximum weight
b = 0.5 * math.floor(sum(a))

# The total weight
weight = lpDot(a, x)

# Objective
prob += weight
# Constraint
prob += weight <= b

# Resolution
prob.solve()

# Print the status of the solved LP
print("Status:", LpStatus[prob.status])

# Print the value of the variables at the optimum
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(prob.objective))
