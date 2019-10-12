from State import State
from MouseAction import MouseAction

class Waiting(State):
    def run(self):
        print("Waiting: Broadcasting cheese smell")

    def next(self, input):
        if input == MouseAction.appears:
            return Luring()
        return Waiting()

class Luring(State):
    def run(self):
        print("Luring: Presenting Cheese, door open")

    def next(self, input):
        if input == MouseAction.runsAway:
            return Waiting()
        if input == MouseAction.enters:
            return Trapping()
        return Luring()

class Trapping(State):
    def run(self):
        print("Trapping: Closing door")

    def next(self, input):
        if input == MouseAction.escapes:
            return Waiting()
        if input == MouseAction.trapped:
            return Holding()
        return Trapping()

class Holding(State):
    def run(self):
        print("Holding: Mouse caught")

    def next(self, input):
        if input == MouseAction.removed:
            return Waiting()
        return Holding()
