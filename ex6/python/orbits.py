# d: dictionary of immediate neighbor orbits
global d, counter 
d = {}

def input2dict(filename):
    with open(filename) as f:
        for line in f:
            [k,v] = line.strip('\n').split(')')
            if k in d: d[k].append(v)
            else: d[k] = [v]
            if v not in d: d[v] = []

def count_indirect_neighbors(k):
    return sum([len(d[d[k][i]]) + count_indirect_neighbors(d[k][i]) for i in range(len(d[k]))])

def insert_indirect_neighbors():
    counter = {}
    for k in d:
        counter[k] = len(d[k]) + count_indirect_neighbors(k)
    print(sum(counter[i] for i in counter))

input2dict('input6')
insert_indirect_neighbors()
