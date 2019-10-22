def booleanPower(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(0)
        result.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                result[j][i] = any([all([matrix[j][k], matrix[k][i]]), result[j][i]])
    for i in range(len(result)):
        for j in range(len(result)):
            if result[j][i] == True:
                result[j][i] = 1
            else:
                result[j][i] = 0
    print(result)

    
            
    
