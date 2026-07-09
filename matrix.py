matrix=[[1,2,3],[4,5,6]]
def convert_rtc(matrix):
    newmatrix=[]
    for i in range(len(matrix[0])):
        newrow=[]
        for j in range(len(matrix)):
            newrow.append(matrix[j][i])
        newmatrix.append(newrow)
    return newmatrix
print(convert_rtc(matrix))
