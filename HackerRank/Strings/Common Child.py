
def commonChild(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    row = [0 for _ in range(1+n2)]
    for i1 in range(1, n1+1):
        prev_row = row.copy()
        row[0] = 0
        for i2 in range(1, n2+1):
            if s1[i1-1] == s2[i2-1]:
                row[i2] = 1 + prev_row[i2-1]
            else:
                row[i2] = max(prev_row[i2], row[i2-1])
    return max(row)




# s1 = 'OUDFRMYMAW'
# s2 = 'AWHYFCCMQX'
# s1 = 'ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP'
# s2 = 'FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX'
s1 = 'SHINCHAN'
s2 = 'NOHARAAA'


print(commonChild(s1, s2))


# def commonChild(s1, s2):
#     if s1 == "" or s2 == "":
#         return 0
#     if s1[-1] == s2[-1]:
#         return 1+commonChild(s1[:-1], s2[:-1])
#     a1 = commonChild(s1, s2[:-1])
#     a2 = commonChild(s1[:-1], s2)
#     return max(a1,a2)




#
# # Complete the commonChild function below.
# def commonChild(s1, s2):
#
#     def commonRec(s1, s2):
#         if s1 == "" or s2 == "":
#             return ""
#         p = s2.find(s1[0])
#         if p == -1:
#             # s1[0] doensn't apear in s2
#             return commonRec(s1[1:], s2)
#         else:
#               # s1[0] apear in s2 at index p - either take it or not
#             comm_take = s1[0] + commonRec(s1[1:], s2[p+1:])
#             comm_no_take = commonRec(s1[1:], s2)
#             if len(comm_take) > len(comm_no_take):
#                 return comm_take
#             else:
#                 return comm_no_take
#     print(commonRec(s1, s2))
#     return len(commonRec(s1, s2))


from copy import  deepcopy
# Complete the commonChild function below.
# def commonChild(s1, s2):
#     s2_dict = {}
#     for i, c in enumerate(s2):
#         if c not in s2_dict:
#             s2_dict[c] = [i]
#         else:
#             s2_dict[c].append(i)
#
#     def commonRec(s1, s2_dict, start2=0):
#         if s1 == "":
#             return ""
#         c = s1[0]
#         if c not in s2_dict:
#             p = -1
#         else:
#             p = -1
#             ind = 0
#             nc = len(s2_dict[c])
#             while ind < nc and s2_dict[c][ind] < start2:
#                 ind += 1
#             if ind < nc:
#                 p = s2_dict[c][ind]
#         if p == -1:
#             # s1[0] doensn't apear in s2
#             return commonRec(s1[1:], s2_dict, start2=start2)
#         else:
#               # s1[0] apear in s2 at index p - either take it or not
#             comm_no_take = commonRec(s1[1:], s2_dict, start2=start2)
#             # remove index p from s2_dict:
#
#             comm_take = c + commonRec(s1[1:], s2_dict, start2=p+1)
#
#             if len(comm_take) > len(comm_no_take):
#                 return comm_take
#             else:
#                 return comm_no_take
#     max_comm = commonRec(s1, s2_dict, start2=0)
#     print(max_comm)
#     return len(max_comm)