omega_set = {(i,j,k) for i in range(6) for j in range(6) for k in range(6)}

poss_set = {(i,j,k) for (i,j,k) in omega_set if i+j+k == 12}

prob = len(poss_set) / len(omega_set)

print(f'{100*prob:.2f}%')