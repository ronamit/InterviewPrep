from typing import List, Dict, Tuple, Sequence
import string

def solution(A: int, B: int, C: int):
    return solution_aux(A, B, C, "", {})


def diversity_friendly(new_leter, last_two):
    if len(last_two) < 2:
        return True

    return not(new_leter == last_two[0] == last_two[1])

def get_canonical(A, B, C, last_two):
    let_counts = [A, B, C]
    counts_ordered = sorted(enumerate(let_counts), key=lambda x: x[1])
    A_t, B_t, C_t = [cnt for i, cnt in counts_ordered]
    trans = {k: 'abc'[counts_ordered[i][0]] for i, k in enumerate('abc')}
    inv_trans = {trans[let]: let for let in 'abc'}
    last_two_t = last_two.translate(trans)
    return A_t, B_t, C_t, last_two_t, trans, inv_trans



def solution_aux(A, B, C, last_two, cache):

    A_t, B_t, C_t, last_two_t, trans, inv_trans = get_canonical(A, B, C, last_two)

    if (A_t, B_t, C_t, last_two_t) in cache:
        best_res_t = cache[(A_t, B_t, C_t, last_two_t)]
        best_res = best_res_t.translate(inv_trans)
        return best_res

    best_res = ''
    letters_counts = {'a': A, 'b': B, 'c': C}

    for letter, count in letters_counts.items():
        if count == 0 or not diversity_friendly(letter, last_two):
            continue

        letters_counts[letter] -= 1
        cur_res = letter + solution_aux(letters_counts['a'], letters_counts['b'], letters_counts['c'],
                                        last_two[-1] + letter if last_two else letter,
                                        cache)

        if len(cur_res) > len(best_res):
            best_res = cur_res

        letters_counts[letter] += 1

    cache[(A_t, B_t, C_t, last_two_t)] = best_res.translate(trans)
    return best_res


if __name__ == '__main__':
    A = 100
    B = 100
    C = 100
    print(f'A={A}, B={B}, C={C}')
    from time import perf_counter
    start = perf_counter()
    sol = solution(A, B, C)
    total = perf_counter() - start
    print(sol)
    print(f'time = {total}s')