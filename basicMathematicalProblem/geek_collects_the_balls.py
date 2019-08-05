# -*- coding: utf-8 -*-
"""
 Geek collects the balls 
"""

solutions = []
for j in range(num_test):
    [n, m] = input().split()
    n = int(n)
    m = int(m)
    s = 0
    n_array = [int(i) for i in input().split()]
    m_array = [int(i) for i in input().split()]
    same_n = [0]
    same_m = [0]
    for ind_n, number_n in enumerate(n_array):
        for ind_m, number_m in enumerate(m_array):
            if number_n == number_m:
                same_n.append(ind_n)
                same_m.append(ind_m)
    same_n.append(len(n_array))
    same_m.append(len(m_array))
    slices_n = []
    for i in range(len(same_n) - 1):
        slices_n.append(sum(n_array[same_n[i]: same_n[i+1]]))
    slices_m = []
    for i in range(len(same_m) - 1):
        slices_m.append(sum(m_array[same_m[i]: same_m[i+1]]))
    for i in range(len(slices_n)):
        s += max(slices_n[i], slices_m[i])
    solutions.append(s)
for solution in (solutions):
    print (solution)
            