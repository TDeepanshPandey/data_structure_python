omega = {(i, j) for i in range(6) for j in range(6)}

""" count_set = 0
for i in omega:
    m,n = i
    if(m ** 2 + n ** 2) > 25 :
        count_set += 1
prob = str(round(count_set / len(omega) * 100, 2))+'%'

print(prob) """

a = {(i, j) for i, j in omega if i ** 2 + j ** 2 > 25}
prob = len(a) / len(omega)
print(f'{100 * prob:.2f}%')