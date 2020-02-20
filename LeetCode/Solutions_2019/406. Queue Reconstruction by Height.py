class Solution:
    def reconstructQueue(self, people):

        outOrder = []
        n = len(people)
        people_orig = [p.copy() for p in people]
        if n == 0:
            return []
        for k in range(n):
            # the person that should be in front = k==0 and with minimal h
            front_i = None
            front_h = None
            for i in range(n):
                if people[i] is not None and people[i][1] == 0:
                    if front_h is None or people[i][0] < front_h:
                        front_h = people[i][0]
                        front_i = i
            # add to list
            outOrder += [front_i]
            # 'delete' from people
            people[front_i] = None
            # update pepole list
            for i in range(n):
                if people[i] is not None and people[i][0] <= front_h:
                    people[i][1] -= 1
        return [people_orig[i] for i in outOrder]

sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))

#
# class Solution:
#     def reconstructQueue(self, people):
#
#         outOrder = []
#         n = len(people)
#         if n == 0:
#             return []
#         arr = [[people[i][0], people[i][1], i] for i in range(n)]
#         for k in range(n):
#             # the person that should be in front = k==0 and with minimal h
#             front_i_orig = None
#             front_i = None
#             front_h = None
#             for i in range(len(arr)):
#                 if  arr[i][1] == 0:
#                     if front_h is None or arr[i][0] < front_h:
#                         front_h = arr[i][0]
#                         front_i = i
#                         front_i_orig = arr[i][2]
#             # add to list
#             outOrder += [front_i_orig]
#             # 'delete' from people
#             del arr[front_i]
#             # update pepole list
#             for i in range(len(arr)):
#                 if arr[i][0] <= front_h:
#                     arr[i][1] -= 1
#
#         return [people[i] for i in outOrder]
#
# sol = Solution()
# people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# print(sol.reconstructQueue(people))
#
#
#
