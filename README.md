# Introduction

The goal of the project is to use a backtracking search algorithm to color the map of the continent of South America. The main goal is to color the countries so that two adjacent countries shouldn't share the same color. To do this, we can only use a maximum of four different colors (blue, green, red, and yellow). The m-coloring problem, the backtracking algorithm, the benefits of include the neighbors as a dictionary in the code, and the code explanation will all be covered in this project report.

# M-coloring Problem

One of the graph coloring problems is the m-coloring problem. The challenge is to use m colors at maximum to evenly distribute the vertices of a network so that no two neighboring vertices share the same color. Since the m-coloring problem is a NP-complete problem, no algorithm with polynomial time complexity can solve it for all kinds of inputs.

# Backtracking Algorithm

Backtracking is a generic algorithmic method that involves examining all possible combinations in order to find a solution to a problem. The backtracking algorithm tries to put together a solution and discards the incomplete ones as soon as it sees they can't be finished to a valid one as expected.

# Constraint Satisfaction Problems

Task: Color each country
Variables: {Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Falkland Islands, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela}
Fields: {blue, red, green, yellow}
Restrictions: Adjacent countries must be in different colors

# Output
