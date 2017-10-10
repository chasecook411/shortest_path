import itertools

'''

Find the shortest path over a series of nodes. 
d(u,v) = distance from u to v, which needs to be predefined in a dict
for some series of nodes p0, p1, p2, .. pN

'''

# returns the distance from two nodes
# from the dictionary where defined
# their distances. 
def dist(u,v,d):
    if u != v:
        return d[u][v]

# Our dictionary is full of duplicates.
# We need to get the distinct indicies, 
# so we have just ['p0', 'p1', 'p2' ..]

# Note! In expected output, the second 
# foreach loop should not be necessary.
def distinct_indicies(dictionary):
    cache = []

    # for each location in sub1
    # add it to our list if its not already
    for place_one in dictionary:
        if place_one not in cache:
            cache.append(place_one)

        # for each location is sub2
        # add it to our list if its not already
        # **it should've been caught in sub1 if 
        # its valid input. **
        for place_two in dictionary[place_one]:
            if place_two not in cache:
                cache.append(place_two)
    return cache

# returns all permutations for a distinct
# iterable of indices
# example:
# [p0, p1, p2]
# [p0, p2, p1]
# [p1, p2, p0]
# ...

# takes a list of indices l
def perm(l):
    return itertools.permutations(l)

# now we want to get the total distance
# traveled for each permutation.
# for v in a set of V vertices,
# we need to check from v_sub_(i) to v_sub_(i+1)

# receives a tuple p, and the dictionary d
def total_dist(p, d):
    # keep track of our total and
    # our i+1 index. 
    total = 0
    j = 1
    for i in range(len(p) - 1):
        # find the distance between vertice i and i+1
        total += dist(p[i], p[j], d)
        j+=1
    return total


# Now we need to find minimum total distance 
# for each path possible. 
def shortest_path(d):
    min = float('inf')
    for p in perm(distinct_indicies(d)):
        temp = total_dist(p, d)

        # if we find a distance shorter than min
        # let's replace it. 
        if temp < min:
            print("Got a minimum!", temp)
            # print out our list for confirmation
            print(p)
            min = temp 
    return min


def main():
    dictionary = {}

    # fill up our dictionary with
    # some valid input, ie. distances
    # from one place to another. 

    # the optimal path for this set of input
    # is ('p2', 'p4', 'p3', 'p0', 'p1')
    # try changing any i/i+1 index to get a 
    # different output. ex. p0 to p1 = 100 
    # and p1 to p0 = 100

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