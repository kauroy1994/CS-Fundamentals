from copy import deepcopy
class Queen(object):

    def __init__(self,number):

        self.number = number
        self.placed = False
        self.x = False
        self.y = False

    def place(self,board,pos):

        self.x = pos[0]
        self.y = pos[1]
        self.placed = True
        board[self.x][self.y] = 1

    def can_attack_pos(self,pos):

        if not self.placed:
            return False
        if self.x == pos[0]:
            return True
        elif self.y == pos[1]:
            return True
        elif abs(self.x - pos[0]) == abs(self.y-pos[1]):
            return True
        return False
        
    def can_attack(self,queen):

        if not self.placed:
            return False
        if self.x == queen.x:
            return True
        elif self.y == queen.y:
            return True
        elif abs(self.x - queen.x) == abs(self.y-queen.y):
            return True
        return False
        
class State(object):


    def __init__(self,board_dim, n_queens):
        
        self.grid = [[0 for i in range(board_dim)] for j in range(board_dim)]
        self.grid_dim = board_dim
        self.queens = [Queen(i) for i in range(n_queens)]

    def all_placed(self):

        for queen in self.queens:
            if not queen.placed:
                return False
        return True

    def oq_can_attack(self,pos):

        for oq in self.queens:
            if oq.placed and oq.can_attack_pos(pos):
                return True

    def get_child(self,visited,method = "Brute"):

        placed_xs = []
        placed_ys = []

        for queen in self.queens:
            if queen.placed:
                placed_xs.append(queen.x)
                placed_ys.append(queen.y)

        for queen in self.queens:
            if not queen.placed:
                for i in range(self.grid_dim):
                    for j in range(self.grid_dim):
                       if (i not in placed_xs) and (j not in placed_ys) and (not self.oq_can_attack((i,j))): #change last condition for brute force           
                           queen.place(self.grid, (i,j))
                           if str(self) not in visited:
                               return self
        return False

    def is_solution(self):

        n_queens = len(self.queens)
        for i in range(n_queens):
            for j in range(i+1,n_queens):
                if self.queens[i].can_attack(self.queens[j]):
                    return False
        return True
                
    def __repr__(self):
        rep = ""
        for queen in self.queens:
            rep += "queen"+str(queen.number)+":"+str((queen.x,queen.y))+"\n"
        return rep

def Algorithm():

    visited = []
    solution = False
    start_state = State(6,5)
    expansion_stack = [start_state]
    while expansion_stack:
        top_state = deepcopy(expansion_stack[-1])
        visited.append(str(top_state))
        #print (top_state)
        #input()
        if top_state.all_placed():
            if top_state.is_solution():
                solution = top_state
                break
        child = top_state.get_child(visited)
        if child:
            expansion_stack.append(child)
        else:
            expansion_stack.pop()
    print ("number of states visited: ",len(visited))
    return solution

if __name__ == '__main__':
    
    solution = Algorithm()
    print (solution)
