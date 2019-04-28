from math import fabs, sqrt
from reaper import *


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

class PriorityQueue:

    def __init__(self, goal):
        self.obj_list = []
        self.priority_list = []

        #self.explored = []
        self.goal = goal

#    def ifexplored(self, value):
 #       for exp in self.explored:
  #          if exp.x == value.x and exp.y == value.y:
   #             return True
    #    return False


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

    def find(self, finder):
        for i in range (len(self.obj_list)):
            if finder == self.obj_list[i]:
                return i
        return -1

#start = State(1,2)
#end = State(15,15)



def Astar(game,startx, starty, endx, endy):
    reap = ScoutReaper(game, startx, starty)
    endx = endx - game.camera.x
    endy = endy - game.camera.y
    start = State(int(startx//TILESIZE), int(starty//TILESIZE))
    end = State (int(endx//TILESIZE), int(endy//TILESIZE))

    print(end)

    Queue = PriorityQueue(end)
    Queue.push(start,start.distance(end))
    explored = []
    pos = start
    count = 0

   # while(True):
    #    reap.pos = (endx, endy)
     #   print(reap.pos)
      #  reap.whereAmI()


    while(True):
        #print("Rozmiar Queue: ", len(Queue.obj_list))
        #count+=1
        #print(Queue.obj_list[i])
        if len(Queue.obj_list) < 1:
            return -1

        pos = Queue.pop()

        if pos == end:
            break

        if pos in explored:
            for i in range (len(explored)):
                if pos == explored[i]:
                    if pos.cost < explored[i].cost:
                        explored[i] = pos

        if pos not in explored:
            #print("dodaje")
            explored.append(pos)
        else:
            continue
        #print(reap.pos)
        reap.pos = vec(pos.x*TILESIZE, pos.y*TILESIZE)
        #print(reap.whereAmI())
        #print(pos)
        for action in pos.actions:
            newstate = action(reap)
            #print(newState)
            print(newstate, " o koszcie:", newstate.distance(end))
            Queue.push(newstate, newstate.distance(end))
            #if pos not in Queue.obj_list and pos not in explored:
            #    Queue.push(newstate, newstate.distance(end))
            #else:
             #   oldprior = Queue.priority_list[Queue.find(newstate)]
              #  if oldprior > pos.distance(end):
               #     Queue.priority_list[Queue.find(newstate)] = pos.distance()
                #    Queue.obj_list[Queue.find(newstate)] = pos




            #Queue.push(newstate, newstate.distance(end))
            #print("Akcja: ", action, " Koszt obecny: ", newstate.cost)
    del reap
    outputtab = []


    while pos.parent is not None:
        outputtab.append(pos)
        pos = pos.parent
    return outputtab

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
