A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
result = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def flip_matrix(A):
    """

    :param A:
    :return:
    """
    # 1. flip horizontally = reverse the elements in the sublists.
    # reversed returns a iterator object vs .reverse() = inplace
    # 2. 1-num gives us the compliment for a binary number
    return [[1-num for num in A[i][::-1]] for i in range(len(A))]

#print(A)
op = flip_matrix(A)
#print(op)


def flipAndInvertImage(A):
    for row in A:
        print(row)
        for i in range(len(row)):
            """
            In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
            helps us find the i-th value of the row, counting from the right.
            """
            #row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
            print("i: ", i)
            print(row[i], row[-i],row[~i] ^ 1, row[i] ^ 1 )
        break

    return A

print(flipAndInvertImage(A))