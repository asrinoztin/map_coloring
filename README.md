# Introduction
m-Coloring is a problem which is basically in order to determine/show that if we manage to color a graph with at most m colors such that no two adjacent vertices of the given graph are colored with the same color.
There are three common ways to solve that kind of problem. These,

## 1. Naive Appoach
Can be thought as a brute-force way. It is based on the idea that “on worst case scenario it will take m^n tries with m colors and n vertices given”. Thus the time complexity is O(m^n) and space complexity is O(n).

## 2. Backtracking
The main purpose of this algorithm is to reach the goal with learning from repetition and it’s own mistakes. As the name suggests, the algorithm takes a step back to find a solution. At first the algorithm starts with a possible move and then keeps going with another. If it does not satisfy, algorithm goes back and tries another one, until it either finds a solution or appears that there is no solution. Thus the time complexity is O(m^n) and space complexity is O(n). The upperbound time complexity (worst-case scenario) is same with brute-force navive approach since there is a total combination of vertex colors is same as m^n. On the other hand, the average complexity is lower relatively.

## 3. BFS:
The appoarch with BFS is based on the idea that coloring each node from 1 to n travelling with BFS. The algorithm checks all edges of the given node and if the color of the neighbors are same, corrects it and goes on. Time complexity is linear and the space complexity is O(V) since it stores the visited nodes.

# Dependencies
In order to run the functions, you need to install the following modules into your virtual environment
▪ pandas (current latest version: 1.1.4)
▪ plotly (current latest version: 4.13.0)

# Constraint Satisfaction Problems (CSPs)
Task: Color each region
Variables: X = {Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Falkland Islands, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela}
Domains: Di = {blue, red, green, yellow}
Constraints: adjacent regions must have different color

# Logic
To understand the algorithm better, print(information_about_that_step) is used at important breakpoints.

![image](https://user-images.githubusercontent.com/58219688/145998146-5f2ff29f-94c2-44f2-9090-f1d47f811ed6.png)
    
# Result
![image](https://user-images.githubusercontent.com/58219688/145997912-7c15a792-2396-4508-974b-56f949a9362c.png)

