class Matrix():
    def __init__(self, strk):
        self.strk = strk
    def __add__(self, other):
        return[[self.strk[i][j] + other.strk[i][j] for j in range(len(self.strk[0]))] for i in range(len(self.strk))]
    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(i) for i in x]) for x in self.strk])
m1 = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[6,5,4],[3,2,1]])
m3 = m1 + m2
print('\n'.join([''.join(['{:4}'.format(i) for i in x]) for x in m3]))
