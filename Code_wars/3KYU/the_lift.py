"""
Synopsis
A multi-floor building has a Lift in it.

People are queued on different floors waiting for the Lift.

Some people want to go up. Some people want to go down.

The floor they want to go to is represented by a number (i.e. when they enter the Lift this is the button they will press)

BEFORE (people waiting in queues)               AFTER (people at their destinations)
                   +--+                                          +--+
  /----------------|  |----------------\        /----------------|  |----------------\
10|                |  | 1,4,3,2        |      10|             10 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 9|                |  | 1,10,2         |       9|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 8|                |  |                |       8|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 7|                |  | 3,6,4,5,6      |       7|                |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 6|                |  |                |       6|          6,6,6 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 5|                |  |                |       5|            5,5 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 4|                |  | 0,0,0          |       4|          4,4,4 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 3|                |  |                |       3|            3,3 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 2|                |  | 4              |       2|          2,2,2 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 1|                |  | 6,5,2          |       1|            1,1 |  |                |
  |----------------|  |----------------|        |----------------|  |----------------|
 G|                |  |                |       G|          0,0,0 |  |                |
  |====================================|        |====================================|
Rules
Lift Rules
The Lift only goes up or down!
Each floor has both UP and DOWN Lift-call buttons (except top and ground floors which have only DOWN and UP respectively)
The Lift never changes direction until there are no more people wanting to get on/off in the direction it is already travelling
When empty the Lift tries to be smart. For example,
If it was going up then it may continue up to collect the highest floor person wanting to go down
If it was going down then it may continue down to collect the lowest floor person wanting to go up
The Lift has a maximum capacity of people
When called, the Lift will stop at a floor even if it is full, although unless somebody gets off nobody else can get on!
If the lift is empty, and no people are waiting, then it will return to the ground floor
People Rules
People are in "queues" that represent their order of arrival to wait for the Lift
All people can press the UP/DOWN Lift-call buttons
Only people going the same direction as the Lift may enter it
Entry is according to the "queue" order, but those unable to enter do not block those behind them that can
If a person is unable to enter a full Lift, they will press the UP/DOWN Lift-call button again after it has departed without them
Kata Task
Get all the people to the floors they want to go to while obeying the Lift rules and the People rules
Return a list of all floors that the Lift stopped at (in the order visited!)
NOTE: The Lift always starts on the ground floor (and people waiting on the ground floor may enter immediately)

I/O
Input
queues a list of queues of people for all floors of the building.
The height of the building varies
0 = the ground floor
Not all floors have queues
Queue index [0] is the "head" of the queue
Numbers indicate which floor the person wants go to
capacity maximum number of people allowed in the lift
Parameter validation - All input parameters can be assumed OK. No need to check for things like:

People wanting to go to floors that do not exist
People wanting to take the Lift to the floor they are already on
Buildings with < 2 floors
Basements
Output
A list of all floors that the Lift stopped at (in the order visited!)
"""

class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.queues = [list(q) for q in queues]
        self.capacity = capacity
        self.stops = []
        self.lift = []

    def people_waiting(self):
        for floor, queue in enumerate(self.queues):
            if queue:
                for people in queue:
                    if people != floor:
                        return True
        return False

    def operating(self):
        return True if self.people_waiting() or self.lift else False

    def move_lift_up(self):
        stops = []
        for floor, queue in enumerate(self.queues[:]):
            stop = False
            for person in self.lift[:]:
                if person == floor:
                    self.unload_elevator(floor, person)
                    stop = True
            for people in queue[:]:
                if people > floor and people != floor:
                    self.load_elevator(floor, people)
                    stop = True
            if stop and self.stops[-1] != floor:
                self.stops.append(floor)
        return stops

    def move_lift_down(self):
        for floor, queue in reversed(list(enumerate(self.queues[:]))):
            stop = False
            for person in self.lift[:]:
                if person == floor:
                    self.unload_elevator(floor, person)
                    stop = True
            for people in queue[:]:
                if people < floor and people != floor:
                    self.load_elevator(floor, people)
                    stop = True
            if stop and self.stops[-1] != floor:
                self.stops.append(floor)

    def unload_elevator(self, floor, person):
        self.lift.remove(person)
        self.queues[floor].append(person)

    def load_elevator(self, floor, people):
        if self.capacity > len(self.lift):
            self.queues[floor].remove(people)
            self.lift.append(people)

    def theLift(self):
        self.stops.append(0)

        while self.operating():
            self.move_lift_up()
            self.move_lift_down()

        self.stops.append(0) if self.stops[-1] != 0 else None

        return self.stops


tests = [[[[], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
          [0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 3, 2, 1, 0, 1, 0]],
         [((), (), (1, 1), (), (), (), ()), [0, 2, 1, 0]],
         [((), (3,), (4,), (), (5,), (), ()), [0, 1, 2, 3, 4, 5, 0]],
         [((), (0,), (), (), (2,), (3,), ()), [0, 5, 4, 3, 2, 1, 0]]]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    assert lift.theLift() == answer
