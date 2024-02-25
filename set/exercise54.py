A = {-4, -1, 1, 5, 6}
B = {-3, -2, 2, 3, 4}

omega = {(i,j) for i in A for j in B if i * j >= 0}

prb = len(omega) /(len(A)*len(B))

print(f'{100*prb:.2f}%')

