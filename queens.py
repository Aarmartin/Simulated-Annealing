import time
import random
import numpy as np
import math

class Board(object):
    """An N-queens candidate solution ."""

    def __init__(self,N):
        """A random N-queens instance"""
        self.queens = dict()
        for col in range(N):
            row = random.choice(range(N))
            self.queens[col] = row

    def copy(self,board):
        """Copy a board (prevent aliasing)"""
        self.queens = board.queens.copy()
        
    def actions(self):
        """Return a list of possible actions given the current placements."""
        # YOU FILL THIS IN
        L = list()

        for col in self.queens:
            for space in range(len(self.queens)):
                if(self.queens[col] != space):
                    L.append([col, space])
        return L
            

    def neighbor(self, action):
        """Return a Board instance like this one but with one action made."""
        # YOU FILL THIS IN

        x = Board(8)
        x.copy(self)
        x.queens[action[0]] = action[1]

        return x

    def cost(self):
        """Compute the cost of this solution."""
        # YOU FILL THIS IN
        cost = 0
        for i in range(len(self.queens)):
            for j in range(i+1, len(self.queens)):
                if(self.queens[i] == self.queens[j]):
                    cost += 1
                if(abs(i - j) == abs(self.queens[i] - self.queens[j])):
                    cost += 1
        return cost


cooling_schedule = {'none': lambda T0,t: T0,
                    'linear': lambda T0,t: T0/(1+t),
                    'logarithmic': lambda T0,t: T0/math.log(1+t)}


def simulated_annealing(env):

    ## set start temperature
    starttemp = int(env.starttemp.get())

    ## set temperature schedule
    temp = cooling_schedule[env.coolmode.get()]

    ## set search cutoff
    maxsteps = int(env.maxsteps.get())
    
    ## Initial random board
    x = Board(8);
    T0 = starttemp
    steps = 1
    env.solved = False
    while x.cost() > 0 and steps < maxsteps and env.alive and env.running:

        ## YOU FILL IN HERE
        y = x.neighbor(random.choice(x.actions()))

        if(y.cost() < x.cost()):
            x = y
        else:
            c = y.cost() - x.cost()
            p = math.e**((-c)/temp(T0, steps))
            if(p > random.random()):
               x = y

        if (steps % 100 == 0):
            env.display(x)
            env.message('SIMULATED ANNEALING\nstep {}\ntemperature: {:.5e}\ncost: {}'.format(steps,temp(T0,steps),x.cost()))
            time.sleep(0.1)
        steps = steps+1

    env.display(x);
    env.message('SIMULATED ANNEALING\nstep {}\ntemperature: {:.5e}\ncost: {}'.format(steps,temp(T0,steps),x.cost()))
    if x.cost() == 0: env.solved = True
    return steps

