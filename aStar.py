from math import fabs, sqrt, floor
from reaper import *
import heapq


class State:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.actions = [self.go, self.turnleft, self.turnright]
        self.parent = None
        self.direction = direction
        self.cost = 0

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.direction == other.direction:
            return True
        else:
            return False

    def go(self,reap):
        if self.direction == 1:
            new = State(self.x + 1, self.y, self.direction)
            new.parent = self
            reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
            new.cost = self.cost + reap.whereAmI()
            return new
        if self.direction == 2:
            new = State(self.x, self.y + 1, self.direction)
            new.parent = self
            reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
            new.cost = self.cost + reap.whereAmI()
            return new
        if self.direction == 3:
            new = State(self.x - 1, self.y, self.direction)
            new.parent = self
            reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
            new.cost = self.cost + reap.whereAmI()
            return new
        if self.direction == 4:
            new = State(self.x, self.y - 1, self.direction)
            new.parent = self

            reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
            new.cost = self.cost + reap.whereAmI()
            return new

    def turnleft(self, reap):
        new = State(self.x, self.y, self.direction)
        new.parent = self
        new.direction = self.direction - 1
        if new.direction == 0:
            new.direction = 4
        new.cost = self.cost + 1
        return new

    def turnright(self, reap):
        new = State(self.x, self.y, self.direction)
        new.parent = self
        new.direction = self.direction + 1
        if new.direction == 5:
            new.direction = 1
        new.cost = self.cost + 1
        return new


    def go_right(self, reap):
        new = State(self.x+1, self.y)
        new.parent = self
        reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
        new.cost = self.cost + reap.whereAmI()
        return new

    def go_up(self, reap):
        new = State(self.x, self.y-1)
        new.parent = self
        reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
        new.cost = self.cost + reap.whereAmI()
        return new

    def go_left(self,reap):
        new = State(self.x-1, self.y)
        new.parent = self
        reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
        new.cost = self.cost + reap.whereAmI()
        return new

    def go_down(self,reap):
        new = State(self.x, self.y+1)
        new.parent = self
        reap.pos = (new.x * TILESIZE, new.y * TILESIZE)
        new.cost = self.cost + reap.whereAmI()

        return new

    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

    def distance(self, goal):
        distance_x = fabs(goal.x - self.x)
        distance_y = fabs(goal.y - self.y)
        return floor(sqrt(distance_x*distance_x + distance_y*distance_y)) + self.cost

    def __del__(self):
        pass

    def __lt__(self, other):
        return (self.cost + self.distance(endtarget)) < (other.cost + other.distance(endtarget))


endtarget = State(2,2,1)


def smallestState(heap):
    return heap.cost + heap.distance(endtarget)


def Astar(game,startx, starty, endx, endy, direction):

    heap = []

    reap = ScoutReaper(game, endx, endy)

    endx = endx - game.camera.x
    endy = endy - game.camera.y
    start = State(int(startx//TILESIZE), int(starty//TILESIZE), direction)
    end = State (int(endx//TILESIZE), int(endy//TILESIZE), 1)
    endtarget = end
    reap.pos.x = startx
    reap.pos.y = starty


    heapq.heappush(heap, start)
    explored = []
    pos = start
    count = 0

    while(True):

        if len(heap) == 0:
            print("JESTEM POJEBANY")
            return False

        pos = heapq.heappop(heap)

        if pos.x == end.x and pos.y == end.y:
            break

        if pos in explored:
            for i in range (len(explored)):
                if pos == explored[i]:
                    if pos.cost < explored[i].cost:
                        explored[i] = pos

        if pos not in explored:
            explored.append(pos)
        else:
            continue
        reap.pos = vec(pos.x*TILESIZE, pos.y*TILESIZE)
        for action in pos.actions:
            newstate = action(reap)
            if (newstate.distance(end) > 10000):
                continue
            heapq.heappush(heap, newstate)

    outputtab = []

    while pos.parent is not None:
        outputtab.append(pos)
        pos = pos.parent

    return outputtab