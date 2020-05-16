for i in range(2):

    a = int(input('Enter no.of rows::'))
    b = int(input('Enter no.of columns::'))

    matrix = []

    for i in range(a):
        c = []
        for j in range(b):
            j = int(input(f'Enter values for Matrix:: {i}  {j} '))
            c.append(j)

        matrix.append(c)

    for i in range(a):
        for j in range(b):
            print(matrix[i][j], end=" ")
        print()
