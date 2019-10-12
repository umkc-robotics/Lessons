from MouseAction import MouseAction
from StateMachine import StateMachine
from MouseStates import *

class MouseTrap(StateMachine):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, Waiting())

moves = map(str.strip,
  open("./MouseMoves.txt").readlines())
MouseTrap().runAll(map(MouseAction, moves))