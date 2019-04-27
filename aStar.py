from pyswip import Prolog
#import pygame as pg
from math import fabs, sqrt
'''

prolog = Prolog()
prolog.consult("aStar.pl")

explored = []
actions = ["Up", "Down", "Wight", "Left", "Go"]
fringe = []
#vec = pg.math.Vector2
#Istate = vec(1, 1) * 64
#GoalTest = vec(4, 4) *64

#prolog.query()


def graphsearch(Fringe, Explored):
    return prolog.query("fringe_add(Fringe, [], Fringe)")


print(prolog.query("initial(State)"))
print(prolog.query("fringe_new(node(nil, nil-State)-0, Fringe)"))
print(prolog.query("fringe_add(1,1,Fringe)"))
k = prolog.query("fringe_select(Fringe,1,1)")

prolog.query("fringe_add()")
'''


class State:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actions = [self.go_right, self.go_up, self.go_down, self.go_left]
        self.parent = None
        self.cost = 0

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def go_right(self):
        new = State(self.x+1, self.y)
        new.parent = self
        new.cost = self.cost + 1
        if new.x == 2 and new.y == 2:
            new.cost += 10
        return new

    def go_up(self):
        new = State(self.x, self.y-1)
        new.parent = self
        new.cost = self.cost + 1
        return new

    def go_left(self):
        new = State(self.x-1, self.y)
        new.parent = self
        new.cost = self.cost + 1
        return new

    def go_down(self):
        new = State(self.x, self.y+1)
        new.parent = self
        new.cost = self.cost + 1
        return new


    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

    def distance(self, goal):
        distance_x = fabs(goal.x - self.x)
        distance_y = fabs(goal.y - self.y)
        return sqrt(distance_x*distance_x + distance_y*distance_y) + self.cost

    def __del__(self):
        pass

class PriorityQueue:

    def __init__(self, goal):
        self.obj_list = []
        self.priority_list = []
        self.explored = []
        self.goal = goal

    def ifexplored(self, value):
        for exp in self.explored:
            if exp.x == value.x and exp.y == value.y:
                return True
        return False

    def push(self, value, priority):
        #print(len(self.explored))
        self.obj_list.append(value)
        self.priority_list.append(priority)

    def pop(self):
        if len(self.obj_list) == 0:
            return -1
        #print(max(self.priority_list))
        #return "chomik"
        tmp = self.priority_list.index(min(self.priority_list))
        #print("TMP", tmp)
        output = self.obj_list[tmp]
        #print("OUTPUT", output)
        self.obj_list.remove(self.obj_list[tmp])
        self.priority_list.remove(self.priority_list[tmp])
        return output

start = State(1,2)
end = State(15,15)
Queue = PriorityQueue(end)
Queue.push(start,start.distance(end))
explored = []
pos = start
count = 0

while(not(pos.x == end.x and pos.y == end.y)):
    count+=1
    #print(Queue.obj_list[i])
    pos = Queue.pop()
    if pos not in explored:
        print("dodaje")
        explored.append(pos)
    else:
        continue
    #print(pos)
    for action in pos.actions:
        newState = action()
        #print(newState)
        Queue.push(newState, newState.distance(end))


while pos.parent is not None:
    print(pos)
    pos = pos.parent

print(count)
'''
k = PriorityQueue()
a = State(2,2)
b = State(2,4)
c = State(5,5)
goal = State(10,10)


k.push(a,a.distance(goal))
k.push(b,b.distance(goal))
k.push(c,c.distance(goal))

print(k.pop())
print(k.pop())
print(k.pop())
print(k.pop())
'''





#print(graphsearch(fringe, explored))
#print("Chomik")

'''
def succ(x, fringe):
    pass

def priority (x):
    return 10
#tutaj trzeba wypisac kost zależny od grida

def reconstruct_path(endpos, elem):
    print("rekonstrukcja")
#tutaj powinien pojawić sie ciąg akcji zbudowny z patern i action


class stan:
    def __init__ (self, parent, action, p, posX, posY):
        self.parent = parent
        self.action = action
        self.p = p
        self.posX = posX
        self.posY = posY

def graphsearch(startpos, endpos):
    startpos = startpos
    endpos = endpos
    fringe = []
    hq.heapify(fringe)
    explored = []
    hq.heappush(fringe, startpos)

    while fringe is not None:
        elem = hq.heappop(fringe)
        if elem is endpos:
            return reconstruct_path(endpos, elem)
        explored.append(elem)

    for (akcja, stan) in succ(elem, fringe):
        p = priority(stan)
        if (not stan in fringe) and (not stan in explored):
            hq.heappush(fringe,stan(elem, akcja, p))
        elif stan in fringe and stan.p > p:
            stan.p = p

    return 0
'''
