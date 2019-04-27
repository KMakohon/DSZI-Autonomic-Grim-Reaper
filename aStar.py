from math import fabs, sqrt

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
