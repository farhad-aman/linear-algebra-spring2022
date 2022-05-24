import numpy as np
r = np.array([25,-22,123,0,-1])
c = np.array([1,42,13,7,91])
s = len(r)
toeplitz = np.zeros((r.shape[0], r.shape[0]))
for i in range(toeplitz.shape[0]):
    for j in range(toeplitz.shape[1]):
        delta = i - j
        if delta >= 0:
            toeplitz[i][j] = r[i-j]
        else:
            toeplitz[i][j] = c[j-i]
curr_row = 0
curr_col = 0
pivot_rows = []
pivot_cols = []
while curr_row < s and curr_col < s:
    is_zero = 1
    while is_zero == 1:
        for i in range(curr_row, s):
            if toeplitz[i][curr_col] != 0:
                is_zero = 0
        if is_zero == 1:
            curr_col += 1
        if curr_col == s:
            break
    if curr_col == s:
        break
    for i in range(curr_row,s):
        if toeplitz[i][curr_col] != 0:
            toeplitz[[curr_row, i]] = toeplitz[[i, curr_row]]
            break
    for i in range(curr_row+1, s):
        if toeplitz[i][curr_col] !=0:
            toeplitz[i] -= (toeplitz[i][curr_col] / toeplitz[curr_row][curr_col]) * toeplitz[curr_row]
    pivot_rows.append(curr_row)
    pivot_cols.append(curr_col)
    curr_row += 1
    toeplitz = np.around(toeplitz, decimals=8)
print(toeplitz)
det = 1
for i in range(s):
    det *= toeplitz[i][i]
print(det)
