def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n*c_lib
    adjencyList = [[] for _ in range(n)]
    for link in cities:
        adjencyList[link[0]-1].append(link[1]-1)
        adjencyList[link[1]-1].append(link[0]-1)

    minCost = 0
    # Run DFS to find DFS forest
    visited = [False for _ in range(n)]
    for s in range(n):
        if visited[s]:
            continue
        # found a new connected componenet - build  libary
        print('Build lib {}'.format(s+1))
        minCost += c_lib
        stk = [s] # source of DFS tree
        while stk:
            p = stk.pop()
            visited[p] = True
            for child in adjencyList[p]:
                if not visited[child]:
                    # found a new edge in DFS tree
                    print('Build road {}->{}'.format(p+1, child+1))
                    visited[child] = True
                    minCost += c_road
                    stk.append(child)
    print(minCost)
    return minCost

n = 3
c_lib = 2
c_road = 1
cities = [[1,2], [3,1], [2,3]]
roadsAndLibraries(n, c_lib, c_road, cities)