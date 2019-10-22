import copy

d = {'a' : 0.20,
     'b' : 0.10,
     'c' : 0.15,
     'd' : 0.25,
     'e' : 0.30}
r = {'a' : '',
     'b' : '',
     'c' : '',
     'd' : '',
     'e' : ''}

def h(data, result):
    if len(data) == 1:
        print(result)
        return
    else:
        left = min(data, key = data.get)
        left_value = data[left]
        for i in left:
            result[i] = '0' + result[i]
        del data[left]
        
        right = min(data, key = data.get)
        right_value = data[right]
        for i in right:
            result[i] = '1' + result[i]
        del data[right]

        data[left + right] = left_value + right_value

        h(data, result)

        
        
    
    
     
