# d: dictionary of immediate neighbor orbits
global d 
d = {}

def input2dict(filename):
    with open(filename) as f:
        for line in f:
            [k,v] = line.strip('\n').split(')')
            if k in d: d[k].append(v)
            else: d[k] = [v]
            if v not in d: d[v] = []

def counter(k):
    return sum([len(d[d[k][i]]) + counter(d[k][i]) for i in range(len(d[k]))])

def insert_indirect_d():
    counter = {}
    for k in d:
        counter[k] = len(d[k]) + counter(k)
    print(sum(counter[i] for i in counter))

input2dict('input6')
insert_indirect_neighbors()
