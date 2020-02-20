def canFinish(self, numCourses: int, prerequisites) -> bool:
    adjList = [[] for _ in range(numCourses)]
    inDegree = [0 for _ in range(numCourses)]
    # create adjacency list + inDegree List
    for edg in prerequisites:
        adjList[edg[1]] += [edg[0]]
        inDegree[edg[0]] += 1
    # find sources
    sourcesStk = []
    srcCntr = 0
    for i in range(numCourses):
        if inDegree[i] == 0:
            sourcesStk.append(i)
            srcCntr += 1
    # while there are still sources - remove them
    while sourcesStk:
        v = sourcesStk.pop()
        for u in adjList[v]:
            inDegree[u] -= 1
            if inDegree[u] == 0:
                sourcesStk.append(u)
                srcCntr += 1
                adjList[v] = []
    # if there are less than numCourses sources found - there is a cycle
    return srcCntr == numCourses

self = None
numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(self, numCourses, prerequisites))