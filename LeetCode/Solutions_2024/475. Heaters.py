class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        n_heaters = len(heaters)
        i_heater = 0
        d = 0
        for house_pos in houses:
            # check if we should move to next heater
            while (
                i_heater < n_heaters - 1
                and abs(house_pos - heaters[i_heater + 1]) <=  abs(house_pos - heaters[i_heater])
            ):
                i_heater += 1
            d = max(d, abs(house_pos - heaters[i_heater]))
        return d
