import itertools

'''

Find the shortest path over a series of nodes. 
d(u,v) = distance from u to v, which needs to be predefined in a dict
for some series of nodes p0, p1, p2, .. pN

'''

def dist(u,v,d):
    if u != v:
        return d[u][v]

def distinct_indicies(dictionary):
    cache = []
    for place_one in dictionary:
        if place_one not in cache:
            cache.append(place_one)
        for place_two in dictionary[place_one]:
            if place_two not in cache:
                cache.append(place_two)
    return cache
            
def perm(l):
    return itertools.permutations(l)

def total_dist(p, d):
    total = 0
    j = 1
    for i in range(len(p) - 1):
        total += dist(p[i], p[j], d)
        j+=1
    return total

def shortest_path(d):
    cache = {}
    min = float('inf')
    for p in perm(distinct_indicies(d)):
        temp = total_dist(p, d)
        if temp < min:
            min = temp 
    return min


def main():
    dictionary = {}

    dictionary['p0'] = {}
    dictionary['p0']['p1'] = 5
    dictionary['p0']['p2'] = 7
    dictionary['p0']['p3'] = 2
    dictionary['p0']['p4'] = 10

    dictionary['p1'] = {}
    dictionary['p1']['p0'] = 5
    dictionary['p1']['p2'] = 23
    dictionary['p1']['p3'] = 32
    dictionary['p1']['p4'] = 20

    dictionary['p2'] = {}
    dictionary['p2']['p0'] = 7
    dictionary['p2']['p1'] = 23
    dictionary['p2']['p3'] = 45 
    dictionary['p2']['p4'] = 16

    dictionary['p3'] = {}
    dictionary['p3']['p0'] = 2
    dictionary['p3']['p1'] = 32
    dictionary['p3']['p2'] = 45 
    dictionary['p3']['p4'] = 18

    dictionary['p4'] = {}
    dictionary['p4']['p0'] = 10
    dictionary['p4']['p1'] = 20
    dictionary['p4']['p2'] = 16 
    dictionary['p4']['p3'] = 18

    print(shortest_path(dictionary))

main()