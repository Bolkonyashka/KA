import sys

import math


def data_analyzer():
    try:
        file = open("in.txt")
    except:
        print("File not found")
        sys.exit()
    data = file.readlines()
    k = int(data[0].split()[0])
    l = int(data[0].split()[1])
    adj_matrix = []
    for i in range(1, k + 1):
        adj_matrix.append(data[i].split())  
    kuhn(adj_matrix, k, l)

def kuhn(matr, k, l):
    match = []
    used = []
    for i in range(l + 1):
        match.append(-1)
    for i in range(1, k + 1):
        used = []
        for j in range(k + 1):
            used.append(False)
        res = dfs(i, used, match, matr)
        if not res:
            res_file = open("out.txt", "w+")
            res_file.write('N\n')
            res_file.write(str(i))
            exit(0)
    output = [None for i in range(k + 1)]
    for i in range(l + 1):
        if match[i] != -1:
            output[match[i]] = i
    res_file = open("out.txt", "w+")
    res_file.write('Y\n')
    for i in range(1, k + 1):
        if match[i] != -1:
            res_file.write(str(output[i]) + ' ')


def dfs(v, used, match, matr):
    if used[v]:
        return False
    used[v] = True
    for i in range(len(matr)):
        if int(matr[v-1][i]) == 1:
            if match[i+1] == -1 or dfs(match[i+1], used, match, matr):
                match[i+1] = v
                return True
    return False



if __name__ == '__main__':
    data_analyzer()
