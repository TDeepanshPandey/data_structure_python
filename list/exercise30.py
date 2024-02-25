def identity_matrix(n: int):
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]

a1 = identity_matrix(5)
print(a1)