
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.players = []
        self.cheese = [random.randInt(0, self.height), random.randInt(0, self.width)]
        # self.cheeses = set([(0,1), (1,2)])
    
    def addAI(self, player):
        self.players.append(player)
        
    def run(self):
        while 1:
            flag = 1
            for player in self.players:
                dist = self.cal_distance(player)
                orig_x, orig_y = player.pos_x, player.pos_y
                if self.timer_to_run(player, TIME_INTERVAL):
                    print()
                if not self.check_valid_move(orig_x, orig_y, player.pos_x, player.pos_y):
                    pass
                # check another check
                if player.pos_x == self.cheese[0] and player.pos_y == self.cheese[1]:
                    self.print()
                    flag = 0
                    break
            if flag == 0:
                break
    
    def find_cheese(self, p_x, p_y):
        return (p_x, p_y) in self.cheeses
    
    def timer_to_run(self, player, time_interval):
        start_time = Timer.cur_time()
        th = ThreadPool.add(player.move())
        while th.running():
            cur_time = Timer.cur_time()
            if cur_time - start_time > time_interval:
                th.terminate()
                return False
                
        return True
              
    def check_valid_move(self, o_x, o_y, p_x, p_y):
        pass
            
    def cal_distance(self, player):
        return abs(player.pos_x - self.cheese[0]) + abs(player.pos_y - self.cheese[1])
          
    def print(self):
        pass
    

class Player:
    def __init__(self, type, x, y, limit_w, limit_h):
        self.pos_x = x
        self.pos_y = y
        self.limit_w = limit_w
        self.limit_h = limit_h
        self.type = type
    
    def move(self, dist):
        pass

class PlayerType:
    RandomMouseMove=0
    SmartMouseMove=1
    DogMove=2
    CatMove=3

class RandomMoveUserAI(Player):
    def __init__(self, x, y, limit_w, limit_h):
        super.__init__(self, PlayerType.RandomMouseMove, x, y, limit_w, limit_h)
    
    def move(self, dist):
        pass

        
class SmartUserAI(Player):
    def __init__(self, x, y, limit_w, limit_h):
        super.__init__(self, x, y, limit_w, limit_h)
    
    def move(self, dist):
        pass


      
        
        
    
