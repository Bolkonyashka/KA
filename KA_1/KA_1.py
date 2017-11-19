import sys

import math


def data_analyzer():
    try:
        file = open("in.txt")
    except:
        print("File not found")
        sys.exit()
    data = file.readlines()
    adj_matrix = []
    for i in range(1, len(data)):
        adj_matrix.append(data[i].split())   
    res = jar_pri_dij(adj_matrix)
    adj_lists = []
    for i in range(0, len(adj_matrix) + 1):
        adj_lists.append([])
    res_weight = 0
    for e in res:
        res_weight += int(adj_matrix[e[0]-1][e[1]-1])
        adj_lists[e[0]].append(e[1])
        adj_lists[e[1]].append(e[0])
    res_file = open("out.txt", "w+")
    for lst in adj_lists[1:]:
        lst.sort()
        for v in lst:
            res_file.write(str(v) + ' ')
        res_file.write('0\n')
    res_file.write(str(res_weight))
    res_file.close()


def jar_pri_dij(matr):
    res = []
    nodes = [i for i in range(1,len(matr) + 1)]
    d = []
    p = []
    for i in range(0, len(nodes) + 1):
        d.append(1000000)
        p.append(-1)
    d[4] = 0
    to_visit = [i for i in range(1,len(matr) + 1)]
    v = min_v(to_visit, d)
    to_visit.remove(v)
    while len(to_visit) != 0:
        for i in range(0, len(matr)):
            if int(matr[v-1][i]) != 32767:
                if i+1 in to_visit and int(matr[v-1][i]) < d[i+1]:
                    d[i+1] = int(matr[v-1][i])
                    p[i+1] = v
        v = min_v(to_visit, d)
        to_visit.remove(v)
        res.append((p[v], v))
    return res


def min_v(to_visit, d):
    min = 32767
    res = -1
    for v in to_visit:
        if d[v] < min:
            min = d[v]
            res = v
    return res


if __name__ == '__main__':
    data_analyzer()
