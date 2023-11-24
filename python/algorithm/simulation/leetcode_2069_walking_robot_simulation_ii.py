"""
author: Zhengjian Kang
date: 11/30/2021

残酷群每日一题: 12/01/2021

https://leetcode.com/problems/walking-robot-simulation-ii/

2069. Walking Robot Simulation II

note: simulation: consider i) if meet against the wall ii) compute direction distance iii) duplicate cycles (paths)

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1).
The grid is aligned with the four cardinal directions ("North", "East", "South", and "West").
A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
 

Example 1:
Input
["Robot", "move", "move", "getPos", "getDir", "move", "move", "move", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.move(2);  // It moves two steps East to (2, 0), and faces East.
robot.move(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.move(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.move(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.move(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

 

Constraints:
2 <= width, height <= 100
1 <= num <= 10^5
At most 10^4 calls in total will be made to step, getPos, and getDir.
"""

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dir = [[1,0], [0,1], [-1,0], [0,-1]]
        self.x = 0
        self.y = 0
        self.d = 0
        self.total = self.width*2 + self.height*2 - 4
        

    def step(self, num: int) -> None:
        def at_corner(x, y):
            if x == 0 and y == 0: return True
            if x == 0 and y == self.height-1: return True
            if x == self.width-1 and y == 0: return True
            if x == self.width-1 and y == self.height-1: return True
            return False
        
        while num > 0:
            if self.d == 0: remain = self.width-1-self.x
            elif self.d == 1: remain = self.height-1-self.y
            elif self.d == 2: remain = self.x
            else: remain = self.y
            
            if remain >= num:
                self.x += num * self.dir[self.d][0]
                self.y += num * self.dir[self.d][1]
                num = 0
            else:
                self.x += remain * self.dir[self.d][0]
                self.y += remain * self.dir[self.d][1]
                self.d = (self.d+1) % 4
                num -= remain
                
                num %= self.total
                if num == 0 and at_corner(self.x, self.y):
                    self.d = (self.d-1+4) % 4
                
        
    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        if (self.d==0): return "East"
        elif (self.d==1): return "North"
        elif (self.d==2): return "West"
        else: return "South"   


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
