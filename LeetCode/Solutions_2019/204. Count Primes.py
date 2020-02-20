import math

def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
        """
    if n <= 1: return 0
    if n == 2: return 0
    count = 1
    is_prime = [True for _ in range(n-1)]
    is_prime[0] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        # all the mults of the factor i are marked as non-prime
        if is_prime[i-1]:
            k = 2*i
            while k < n:
                is_prime[k-1] = False
                k += i
    count = sum(is_prime, 0)
    # # for deubg:
    # for i in range(n-1):
    #     if is_prime[i]:
    #         print(i+1)
    return count


self = None
n = 10
out = countPrimes(self, n)
print('Final out:')
print(out)

#
# def countPrimes(self, n):
#     """
#     :type n: int
#     :rtype: int
#         """
#     if n <= 1: return 0
#     if n == 2: return 0
#     count = 1
#     primes = set([2])
#     # max_prime = 2  #
#     for i in range(3, n, 2):
#         is_prime = True
#         for j in primes:
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.add(i)
#             count += 1
#     print(primes)
#     return count