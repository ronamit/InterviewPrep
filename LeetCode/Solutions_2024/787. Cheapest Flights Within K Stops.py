import math


class Solution:

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Use Bellman-Ford algorithm O(k * |E|)

        # init an array of the min price to reach each city from src
        min_prices = [math.inf] * n
        min_prices[src] = 0

        for _ in range(k + 1):
            # create a copy of the min_prices array
            min_prices_copy = min_prices.copy()
            for flight in flights:
                f, t, p = flight  # from, to, price
                # check if the shortest path to city t is improved by going through city f
                min_prices[t] = min(min_prices[t], min_prices_copy[f] + p)

        price_to_dest = min_prices[dst]
        return price_to_dest if price_to_dest < math.inf else -1


if __name__ == "__main__":
    n = 5
    flights = [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]]
    src = 0
    dst = 2
    k = 2
    print(Solution().findCheapestPrice(n, flights, src, dst, k))

    # def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    #     #  complexity: O(n^k)

    #     # create adjacency list (outgoing edges)
    #     adj = [[] for _ in range(n)]
    #     for flight in flights:
    #         f, t, p = flight
    #         adj[f].append((t, p))  # (to, price)

    #     flights_dict = {(f, t): p for f, t, p in flights}

    #     @cache
    #     def get_min_price(from_city, to_city, n_stops):
    #         if from_city == to_city:
    #             return 0
    #         # first check direct flight
    #         min_price = flights_dict.get((from_city, to_city), math.inf)
    #         # if we can do more stops, check all possible flights with stop at 3rd city
    #         if n_stops > 0:
    #             for next_city, price in adj[from_city]:
    #                 min_price = min(min_price, price + get_min_price(next_city, to_city, n_stops - 1))
    #         return min_price

    #     min_price =  get_min_price(from_city=src, to_city=dst, n_stops=k)
    #     return min_price if min_price < math.inf else -1
