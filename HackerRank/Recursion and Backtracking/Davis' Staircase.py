# Complete the stepPerms function below.
# def stepPerms(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     if n == 2:
#         return stepPerms(n-1) + stepPerms(n-2)
#     return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3) % 10000000007

def stepPerms(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    stepsPre3 = 1
    stepsPre2 = 1
    stepsPre1 = 2
    for i in range(3, n+1):
            steps =  stepsPre1 + stepsPre2 + stepsPre3 % 10000000007
            stepsPre3 = stepsPre2
            stepsPre2 = stepsPre1
            stepsPre1 = steps
    return steps
