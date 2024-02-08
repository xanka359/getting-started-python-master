def create_matrix(size = 3, up_fill = 0, down_fill = 0):
    m = []
    x = 1
    for i in range(size):
        m.append([0]*size)
    for i in range(size):
        for j in range(size):
            if i == j:
                m[i][j] = x
                x+=1
            elif i>j:
                m[i][j] = up_fill
            elif i<j:
                m[i][j] = down_fill
    for i in m:
        return i
create_matrix()