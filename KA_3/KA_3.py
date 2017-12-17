from queue import Queue
import sys

class Task:
    def __init__(self):
        try:
            file = open("in.txt")
        except:
            print("File not found")
            sys.exit()
        data = file.readlines()
        self.n = int(data[0].split()[0])
        self.adj_matrix = []
        self.q = Queue()
        self.flow = []
        for i in range(0, self.n + 1):
            self.flow.append([0]* (self.n + 1))
        self.prev = [0] * (self.n + 1)
        for i in range(1, self.n + 2):
            self.adj_matrix.append(data[i].split())  


    def max_flow(self, start, end, n):
        maxflow = 0
        while(self.bfs(start, end) == 0):
            delta = 1000000
            u = n
            while (self.prev[u] >= 0):
                delta = min(delta, (int(self.adj_matrix[self.prev[u]][u]) - self.flow[self.prev[u]][u]))
                u = self.prev[u]
            u = n
            while (self.prev[u] >= 0):
                self.flow[self.prev[u]][u] += delta
                self.flow[u][self.prev[u]] -= delta
                u = self.prev[u]
            maxflow += delta
        return maxflow

        
    def bfs(self, start, end):
        visited = [0] *  (self.n + 1)
        self.q.put(start)
        visited[start] = 1
        self.prev[start] = -1
        while not self.q.empty():
            u = self.q.get()
            visited[u] = 2
            for v in range (0, self.n + 1):
                if visited[v] == 0 and (int(self.adj_matrix[u][v]) - self.flow[u][v] > 0):
                    self.q.put(v)
                    visited[v] = 1
                    self.prev[v] = u
        if visited[end] == 2:
            return 0
        else:
            return 1
    

if __name__ == '__main__':
    task = Task()
    res_file = open("out.txt", "w+")
    res_file.write(str(task.max_flow(0, task.n, task.n)))
