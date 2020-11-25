########################################################
#
# CMPSC 441: Homework 2
#
########################################################


student_name = 'Roger Yu'
student_email = 'rpy5032'




########################################################
# Import
########################################################


from hw2_utils import *
from collections import deque

# Add your imports here if used







##########################################################
# 1. Uninformed Any-Path Search Algorithms
##########################################################


def depth_first_search(problem):
    
    node = Node(problem.init_state)
    frontier = deque([node])         # stack: append/pop
    explored = [problem.init_state]  # used as "visited"
    while len(frontier) != 0:
        n = frontier.pop()
        if problem.goal_test(n.state):
            return n
        for i in n.expand(problem):
            if i.state not in explored and i not in frontier:
                frontier.append(i)
                explored.append(i.state)
    return Node(None)

    
def breadth_first_search(problem):
    
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: append/popleft
    explored = [problem.init_state]  # used as "visited"         
    while len(frontier) != 0:
        n = frontier.popleft()
        if problem.goal_test(n.state):
            return n
        for i in n.expand(problem):
            if i.state not in explored and i not in frontier:
                frontier.append(i)
                explored.append(i.state)
    return Node(None)





##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    
    def __init__(self, n):
        x = (-1,) * n
        self.init_state = x;

    
    def actions(self, state):
        x = list(range(len(state)))
        y = 0
        while state[y] != -1:
            y+=1
        for i in list(range(len(state))):
            if state[i] != -1:
                if (state[i] in x):
                    x.remove(state[i])
                if (state[i] + (y - i)) in x:
                    x.remove(state[i] + (y - i))
                if (state[i] - (y - i)) in x:
                    x.remove(state[i] - (y - i))
        return x;

    def result(self, state, action):
        x = list(state)
        y = 0
        while x[y] != -1:
            y+=1
        x[y] = action
        return tuple(x)
    
                        
    def goal_test(self, state):
        n = NQueensProblem(len(state))
        s = [-1] * len(state)
        for i in range(len(state)):
            if state[i] in n.actions(tuple(s)):
                s[i] = state[i]
            else:
                return False
        return True


        


##########################################################
# 3. Farmer's Problem
##########################################################


class FarmerProblem(Problem):
    
    def __init__(self, init_state, goal_state):
        super().__init__(init_state, goal_state)

    
    def actions(self, state):
        actions = ['F', 'FG', 'FC', 'FX']
        f = FarmerProblem((True, True, True, True), (False, False, False, False))
        for i in ['F', 'FG', 'FC', 'FX']:
            x = f.result(state, i)
            if (x[0] != x[1] and x[1] == x[2]) or (x[0] != x[2] and x[2] == x[3]):
                actions.remove(i)
        return actions

    
    def result(self, state, action):
        x = list(state)
        if action == 'F':
            x[0] = not x[0]
        elif action == 'FG':
            x[0] = not x[0]
            x[1] = not x[1]
        elif action == 'FC':
            x[0] = not x[0]
            x[2] = not x[2]
        elif action == 'FX':
            x[0] = not x[0]
            x[3] = not x[3]
        return tuple(x)
            
    
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False





##########################################################
# 4. Graph Problem
##########################################################


class GraphProblem(Problem):
    
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

    
    def actions(self, state):
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        return action

    
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        return False

