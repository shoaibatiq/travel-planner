class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}
        
    def addVertex(self, vertex):
        if(self.adjacencyList.get(vertex) is None):
            self.adjacencyList[vertex] = []
            
    def addEdge(self, vertex1,vertex2, weight):
        self.adjacencyList[vertex1].append([vertex2,weight])
        self.adjacencyList[vertex2].append([vertex1, weight])

    def Dijkstra(self, start, finish):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        smallest = None
        for vertex in self.adjacencyList:
            if(vertex == start):
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueue(vertex, float('inf'))
            previous[vertex] = None
        
        while(len(nodes.values)):
            smallest = nodes.dequeue().val
            if(smallest == finish):
                while(previous.get(smallest) is not None):
                    path.append(smallest)
                    smallest = previous[smallest]
                
                break
            
            if(smallest or distances[smallest] != float('inf')):
                for nextNode in self.adjacencyList[smallest]:
                    candidate = distances[smallest] + nextNode[1]
                    nextNeighbor = nextNode[0]
                    if(candidate < distances[nextNeighbor]):
                        distances[nextNeighbor] = candidate
                        previous[nextNeighbor] = smallest
                        nodes.enqueue(nextNeighbor, candidate)
                    
                
            
        
        return (path + [smallest]   )[::-1]  

class PriorityQueue:
    def __init__(self):
        self.values = []
        
    def enqueue(self, val, priority):
        newNode =Node(val, priority)
        self.values.append(newNode)
        self.bubbleUp()
    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while(idx > 0):
            parentIdx = (idx - 1)//2
            parent = self.values[parentIdx]
            if(element.priority >= parent.priority): break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx
        
    
    def dequeue(self):
        Min = self.values[0]
        end = self.values.pop()
        if(len(self.values) > 0):
            self.values[0] = end
            self.sinkDown()
        
        return Min
    
    def sinkDown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while(True):
            leftChildIdx = 2 * idx + 1
            rightChildIdx = 2 * idx + 2
            swap = None

            if(leftChildIdx < length):
                leftChild = self.values[leftChildIdx]
                if(leftChild.priority < element.priority):
                    swap = leftChildIdx
                
            
            if(rightChildIdx < length):
                rightChild = self.values[rightChildIdx]
                if(
                    (swap == None and rightChild.priority < element.priority) or
                    (swap != None and rightChild.priority < leftChild.priority)
                ):
                    swap = rightChildIdx
                
            if(swap == None): break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap
        

class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority

if __name__ == '__main__':
    while(True):
        edges = int(input("Enter Number of edges: "))

        results = []
        for i in range(edges):
            src = input(f"Enter Edge_{i+1} source: ")
            dest = input(f"Enter Edge_{i+1} Destination: ")
            w = input(f"Enter Edge_{i+1} weight(distance/cost): ")
            results.append({'source': src + ',' + dest, 'dest': w})

        shrtFrom = input("Enter vertex to find shortest path from: ")
        shrtTo = input("Enter vertex to find shortest path to: ")

        vertexs=[]
        G=WeightedGraph()
        for v in results:
            src, dest = v['source'].split(',')
            src = src.lower()
            dest = dest.lower()
            w = v['dest']
            if src not in vertexs:
                G.addVertex(src)
                vertexs.append(src)
            if dest not in vertexs:
                G.addVertex(dest)
                vertexs.append(dest)
            G.addEdge(src,dest,int(w) )
            
        shrtPath = G.Dijkstra(shrtFrom,shrtTo)
        shrtPath = (" --> ".join(shrtPath)).upper()

        print('\n\n')
        print("Optimal Path:")
        print(shrtPath)

        c = input('Enter "exit" to exit: ')
        if c.lower() == 'exit':
            break

