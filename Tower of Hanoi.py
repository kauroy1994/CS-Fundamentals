from copy import deepcopy
class Block(object):

    Actions = []

    def __init__(self,number,beg,aux,end):
        
        self.number = number
        self.executed = False
        self.beg = beg
        self.aux = aux
        self.end = end

    def __repr__(self):

        return (str(self.executed)+', ('+str(self.number)+','+self.beg+','+self.aux+','+self.end+').')
    
def Tower_of_Hanoi(n_blocks):

    start_state = Block(n_blocks,'A','B','C')
    c = 0 #number of states visited counter
    stack = [start_state]
    while stack:
        
        top = stack[-1]
        c += 1
        '''
        if not top.executed:
            print (top)
            input()
        '''
        if top.executed:
            c -= 1
            stack.pop()
        if top.number == 1:
            Block.Actions.append(str(top.beg+'-->'+top.end))
            stack.pop()
        elif not top.executed:
            top.executed = True
            c1 = Block(top.number-1,top.beg,top.end,top.aux)
            c2 = Block(1,top.beg,top.aux,top.end)
            c3 = Block(top.number-1,top.aux,top.beg,top.end)
            stack.append(c3)
            stack.append(c2)
            stack.append(c1)
    print (c)
    return (Block.Actions)

if __name__ == '__main__':
    actions = Tower_of_Hanoi(4)
    for action in actions:
        print (action)
