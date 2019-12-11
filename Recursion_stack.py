class Node(object):

    R = None #initialize result

    @staticmethod
    def pop_compute(V):

        return Node.R*V

    def __init__(self,V):
        self.V = V
        if Node.R == None:
            Node.R = 1

    def __repr__(self):

        return str(self.V)

class Stack(object):

    def __init__(self):

        self.stack = []

    def push(self,node):

        self.stack.append(node)

    def pop(self):

        
        node = self.stack[-1]
        #print ("popped "+str(node))
        Node.R = node.pop_compute(node.V)
        self.stack.pop()

    def empty(self):

        if not self.stack:
            return True

def factorial(N):

    visited = []
    st = Stack()
    st.push(Node(N))
    while not st.empty():
        top = st.stack[-1]
        #print (top)
        #print (top.V)
        #input()
        if (top.V == 1) or (str(top) in visited):
            st.pop()
            #print (Node.R)
        else:
            visited.append(str(top))
            child = Node(top.V-1)
            st.push(child)

    return (Node.R)

print (factorial(5))
        
