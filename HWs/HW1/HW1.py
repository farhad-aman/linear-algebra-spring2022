import numpy as np
np.set_printoptions(suppress=True)
elements = input().split()
s = input()
s1 = s.split(' -> ')[0]
s2 = s.split(' -> ')[1]
mols1 = s1.split(' + ')  
mols2 = s2.split(' + ')  
sz = len(mols1) + len(mols2)
co = np.zeros((len(elements),sz))
for j in range(len(mols1)):
    for e in mols1[j].split():
        if len(e) == 1:
            for i in range(len(elements)):
                if elements[i] == e:
                    co[i][j] = 1 
        else: 
            for i in range(len(elements)):
                if elements[i] == e[0]:
                    co[i][j] = int(e[1:])
for j in range(len(mols2)):
    for e in mols2[j].split():
        if len(e) == 1:
            for i in range(len(elements)):
                if elements[i] == e:
                    co[i][j+len(mols1)] = -1 
        else: 
            for i in range(len(elements)):
                if elements[i] == e[0]:
                    co[i][j+len(mols1)] =  -1 * int(e[1:])
z = np.zeros(shape=(len(elements),1))
augmented = np.append(co, z, axis=1)
print('\nAugmented:\n',augmented)
r = augmented.shape[0]
c = augmented.shape[1]
curr_row = 0
curr_col = 0
pivot_rows = []
pivot_cols = []
while curr_row < r and curr_col < c:
    is_zero = 1
    while is_zero == 1:
        for i in range(curr_row, r):
            if augmented[i][curr_col] != 0:
                is_zero = 0
        if is_zero == 1:
            curr_col += 1
        if curr_col == c:
            break
    if curr_col == c:
        break
    for i in range(curr_row,r):
        if augmented[i][curr_col] != 0:
            augmented[[curr_row, i]] = augmented[[i, curr_row]]
            break
    for i in range(curr_row+1, r):
        if augmented[i][curr_col] !=0:
            augmented[i] -= (augmented[i][curr_col] / augmented[curr_row][curr_col]) * augmented[curr_row]
    pivot_rows.append(curr_row)
    pivot_cols.append(curr_col)
    curr_row += 1
    augmented = np.around(augmented, decimals=8)
echelon = augmented
print('\nEchelon Form:\n',echelon)
reduced = echelon.copy()
pivot_cols.reverse()
pivot_rows.reverse()
for i in range(len(pivot_cols)):
    reduced[pivot_rows[i]] /= (reduced[pivot_rows[i]][pivot_cols[i]])
    for j in range(pivot_rows[i]):
        reduced[j] -= (reduced[j][pivot_cols[i]] / reduced[pivot_rows[i]][pivot_cols[i]]) * reduced[pivot_rows[i]]
print('\nReduced Echelon Form:\n', reduced)
answers = [1 for i in range(c-1)]
for i in pivot_cols:
    answers[i] = 0
for i in range(len(pivot_cols)):
    sum = 0
    for j in range(pivot_cols[i]+1, c-1):
        sum -= reduced[pivot_rows[i]][j]
    sum += reduced[pivot_rows[i]][c-1]
    answers[pivot_cols[i]] = sum
print('\nFinal Answer:')
answers = np.around(answers, decimals=6)
for i in range(len(answers)):
    if i == 0:
        print('X1 = ',answers[0],end='',sep='')
    else:
        print(', X',i+1,' = ',answers[i],sep='',end='')