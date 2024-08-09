class Solution:
    def canReachCorner(
        self,
        xCorner: int,
        yCorner: int,
        circles: list[list[int]],
    ) -> bool:
        # Idea: equivalent condition - look at all the circles as a graph
        # edge = the circles overlap or touch
        # check if there is a connected component that creosses two  oposite walls of the rectengles  return False (or if it crosses the up-right ir down-left wall pairs)

        # create adjacency list
        n = len(circles)
        adj = [[] for _ in range(n)]
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                x1, y1, r1 = circles[i1]
                x2, y2, r2 = circles[i2]
                d_sqr = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if (r1 + r2) ** 2 >= d_sqr:
                    print("i1", i1, "i2", i2)
                    adj[i1].append(i2)
                    adj[i2].append(i1)
        print("adj: ", adj)

        def dfs(i: int) -> tuple[int]:
            nonlocal visited, adj, circles
            visited.add(i)
            x, y, r = circles[i]
            min_x = x - r
            max_x = x + r
            min_y = y - r
            max_y = y + r
            for j in adj[i]:
                if j not in visited:
                    jmin_x, jmax_x, jmin_y, jmax_y = dfs(j)
                    min_x = min(min_x, jmin_x)
                    max_x = max(max_x, jmax_x)
                    min_y = min(min_y, jmin_y)
                    max_y = max(max_y, jmax_y)
            return min_x, max_x, min_y, max_y

        # go over the connected components:
        visited = set()
        for i in range(n):
            # Get the bounding box coords of the connected component:
            min_x, max_x, min_y, max_y = dfs(i)
            print(f" min_x {min_x}, max_x {max_x}, min_y {min_y}, max_y {max_y}")
            # crosses the left and right walls:
            if (max_x >= xCorner) and (min_x < 0) and (min_y < yCorner) and (max_y > 0):
                print(" crosses the left and right walls:")
                return False
            # crosses the up and down walls:
            if (max_y >= yCorner) and (min_y < 0) and (min_x < xCorner) and (max_x > 0):
                print(" crosses the up and down walls")
                return False
            # crosses the upper and right walls:
            if (min_x < xCorner <= max_x) and (min_y < yCorner <= max_y):
                print(" crosses the upper and right walls")
                return False
            # crosses the down and left walls:
            if (min_x < 0 <= max_x) and (min_y < 0 <= max_y):
                print("crosses the down and left walls")
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    circles = [[2, 1000, 997], [1000, 2, 997]]
    xCorner = 3  # noqa: N816
    yCorner = 3  # noqa: N816
    # plot the circles:
    from matplotlib import pyplot as plt  # noqa: I001
    import numpy as np
    plt.figure()
    for circle in circles:
        x,y, r = circle
        plt.scatter([x], [y])
        # draw the circle:
        t = np.linspace(-np.pi*r/180., 360.*np.pi/180., 50000)
        plt.scatter([x+r*np.cos(t), x-r*np.cos(t)], [y+r*np.sin(t), y-r*np.sin(t)], zorder=2, s=0.1)
    # plot the rectangle:
    plt.plot([0., xCorner], [0., 0.], color="black", linewidth=2)
    plt.plot([0., 0.], [0., yCorner], color="black" , linewidth=2)
    plt.plot([0., xCorner], [yCorner, yCorner], color="black", linewidth=2)
    plt.plot([xCorner, xCorner], [0., yCorner], color="black" , linewidth=2)
    plt.show()
        
        
    print(sol.canReachCorner(xCorner, yCorner, circles))
